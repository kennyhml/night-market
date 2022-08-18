from threading import Thread
from captcha import CaptchaSolver
from item import Item
from screen import mask, process_tess_image
from tarkov import Discord, TarkovBot, lg
import pyautogui as pg
import time
from PIL import Image
import pytesseract as tes

tes.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class MarketUI(TarkovBot):
    """Main flea market ui handle
    ---------------------------
    Inherits from TarkovBot
    Has all methods needed in order to buy items from the flea market.

    Raises:
    --------
    - `MarketDidntOpenError` if the market could not be opened.
    """

    purchase_grid = [(1678, y_axis, 192, 73) for y_axis in range(143, 937, 72)]
    price_grid = [(1333, y_axis, 172, 26) for y_axis in range(160, 951, 72)]

    def __init__(self) -> None:
        super().__init__()
        self.discord = Discord()

    def is_open(self) -> bool:
        """Checks if the market is open"""
        return (
            pg.locateOnScreen(
                "images/filter_settings.png", region=(462, 66, 38, 36), confidence=0.7
            )
            is not None
        )

    def await_market_open(self):
        """Awaits the market to open to idle less"""
        start = time.time()

        while not self.is_open():
            self.sleep(0.1)

            if self.has_timedout(start, 3):
                return

    def open(self):
        """Opens the flea market tab"""
        self.check_status()
        self.notify("Opening flea market...")
        start = time.time()

        # check if flea market is currently open (mostly will be the case)
        if self.is_open():
            self.notify("Flea market is open.")
            return

        # open the market tab
        while not self.is_open():
            self.move_to(1251, 1063)
            self.click()
            self.await_market_open()

            if self.has_timedout(start, 30):
                self.notify("Unable to open the flea market after 30s!")
                raise MarketDidntOpenError

        self.notify("Opened the flea market!")

    def search_item(self, item: Item) -> None:
        """Searches for an item and sets the filter given the items properties

        Parameters:
        ------------
        item: :class:`Item`
            The item object to search and buy if possible
        """
        self.check_status()
        self.notify(f"Searching for {item.name}...")
        start = time.time()

        # searches items name
        searchbar = SearchBar(item)
        searchbar.search_item()

        # set filter
        filter = Filter(item)
        filter.configurate()

        while self.items_listed():
            pass

        # await items listed
        while not self.items_listed():
            pass

        self.notify(f"Searching for {item.name} took {round(time.time() - start, 2)}s")

    def items_listed(self) -> bool:
        """Checks if items are already listed"""
        return (
            pg.locateOnScreen(
                "images/price_sort_arrow.png",
                region=(1419, 112, 28, 22),
                confidence=0.7,
            )
            is not None
        )

    def get_amount(self):
        """Gets the amount of items that can be bought"""
        self.check_status()
        self.notify("Checking item amount...")

        # get image showing the amount, process and pass to tesseract
        pg.screenshot("Images/item_amount.png", region=(1085, 472, 48, 32))
        processed = mask("Images/item_amount.png")
        result = (
            tes.image_to_string(
                processed,
                config="-c tessedit_char_whitelist=1234567890/ --psm 8 -l eng",
            )
            .strip()  # strip to remove blankspaces
            .replace("/", "")  # remove the "/"
        )
        # output ocr result
        self.notify(f"Quantity: {result}")
        return result

    def do_purchase(self, point):
        """Cursor should already be on the purchase button on this point!
        Hits the button, awaits until the confirm prompt loads and gets the
        available amount, if amount > 1 then include pressing all.
        """
        self.check_status()
        self.notify("Buying available item...")
        self.move_to(point)
        self.click(0.2)
        self.move_to(1779, 118)

        # Wait for the red exit button of the prompt
        while not pg.pixelMatchesColor(1171, 460, (64, 13, 11), tolerance=20):
            if self.captcha_appeared():
                self.notify("A captcha has appeared!")
                captcha = CaptchaSolver()
                captcha.solve()
                return False, None

        # Grab the amount of items to check if we need to hit the "all" button
        amount = int(self.get_amount())
        if amount > 1:
            self.move_to(1146, 490)
            self.click(0.2)

        # Y to confirm, check purchase succeeded, return item quantity
        self.press("Y")
        success, fixed_amount = self.await_purchase_result()
        return success, fixed_amount if fixed_amount else amount

    def await_purchase_result(self):
        """Checks if a purchase fails, succeeds or errors."""
        self.check_status()
        self.notify("Awaiting purchase result...")

        # wait for either result to show up
        while True:
            success = self.purchase_succeeded()
            failure = self.purchase_failed()
            error = self.purchase_errored()

            # no special error occurred
            if success or failure:
                return success, None

            if error:
                break

            self.sleep(0.1)
            if self.captcha_appeared():
                self.notify("A captcha has appeared!")
                captcha = CaptchaSolver()
                captcha.solve()
                return False, None

        error, new = self.purchase_errored()
        if error:
            self.notify("Purchase result is an error message!")
            if new:
                self.notify(f"The amount bought was {new}")
                self.press("esc")
                self.sleep(0.3)

        return True, new

    def get_error(self):
        pg.screenshot("images/temp/error.png", region=(708, 456, 497, 176))
        processed = mask("images/temp/error.png")

        error = tes.image_to_string(processed, config="--psm 8 -l eng").strip()
        self.discord.send_message(error)
        self.press("esc")
        self.sleep(1)

    def purchase_errored(self):
        if (
            pg.locateOnScreen(
                "images/not_enough_money.png",
                region=(752, 466, 154, 36),
                confidence=0.7,
            )
            is not None
        ):
            raise NoMoneyLeft

        if (new_amount := self.too_many_items_error()) is not None:
            return True, new_amount

    def too_many_items_error(self):
        """Checks whether a purchase resulted in an error. this could be:
        - Tried to buy more items than available
        - Not enough money (should trigger inventory emptying)
        - Other unknwon errors?
        """
        if (
            pg.locateOnScreen(
                "images/too_many_items.png", region=(915, 554, 90, 45), confidence=0.7
            )
            is not None
        ):
            path = "images/temp/amount.png"
            self.notify("Error: Not all items were left!")

            pg.screenshot("images/temp/amount.png", region=(1005, 522, 81, 20))
            img = Image.open("images/temp/amount.png")
            w, h = img.size
            img = img.resize((w * 6, h * 6), 1)
            img.save(path)
            text: str = tes.image_to_string(
                mask(path),
                config="-c tessedit_char_whitelist=1234567890 --psm 10 -l eng",
            ).strip()
            print(text)
            return "".join(char for char in [c for c in text if c.isdigit()])

    def purchase_failed(self):
        """Checks if a purchase failed by matching for the red icon"""
        return (
            pg.locateOnScreen(
                "images/failure.png", region=(1424, 1019, 26, 21), confidence=0.7
            )
            is not None
        )

    def purchase_succeeded(self):
        """Checks if a purchase succeeded by matching for the white icon"""
        return (
            pg.locateOnScreen(
                "images/success.png", region=(1347, 1017, 194, 25), confidence=0.7
            )
            is not None
        )

    def get_item_price(self, img):
        """Processes the image of the item price and ocr's it"""
        self.check_status()
        self.notify("Getting item price...")

        # process passed image and ocr it, remove blankspaces
        processed = process_tess_image(img)
        return tes.image_to_string(
            processed, config="-c tessedit_char_whitelist=1234567890 --psm 8 -l eng"
        ).strip()

    def captcha_appeared(self):
        return (
            pg.locateOnScreen(
                "Images/captcha.png", region=(577, 45, 775, 1007), confidence=0.7
            )
            is not None
        )

    def post_profit(self, item: Item, purchases: list[(str, int)]):
        """Sends all previously bought items to discord, the thread is started
        after all items have been purchased to avoid slowdowns and errors.

        Parameters:
        -----------
        item: :class:`Item`
            The item that was being purchased

        purchases: :class:`List`
            The list of purchases containing image path and purchase quantity
        """
        self.check_status()
        self.notify("Posting gains to discord...")

        # post each purchase as a seperate message (probably combine it later on?)
        for purchase in purchases:
            try:
                # get price from image, amount from data
                price = self.get_item_price(purchase[0])
                amount = purchase[1]

                # post the data
                self.discord.send_message(
                    f"Purchased {amount} x `{item.name}` for **{price}** ₽!\n"
                    f"Profit: {(int(item.price) - int(price)) * int(amount)} ₽!"
                )
            except Exception as e:
                self.notify(f"Unhandled exception posting to discord!\n{e}")

    def topslot_is_loaded(self) -> bool:
        """Checks if the topmost slot has an item in it"""
        return (
            pg.locateOnScreen(
                "images/available.png", region=(1845, 139, 28, 25), confidence=0.8
            )
            is not None
        )

    def refresh(self):

        while not pg.pixelMatchesColor(1833, 121, (207, 217, 222), tolerance=30):
            self.sleep(0.1)
            self.notify("Waiting to be able to refresh...")

        self.move_to(1839, 118)
        self.click(0.2)

        while not self.items_listed():
            self.sleep(0.01)
            self.notify("Waiting for listed items...")

    def item_available(self, region):
        return pg.locateOnScreen("images/purchase.png", region=region, confidence=0.7)

    def item_out_of_stock(self, region):
        return pg.locateOnScreen(
            "images/out of stock.png", region=region, confidence=0.7
        )

    def get_available_purchases(self, item: Item):
        """Main purchase finding function, checks the status of each item slot
        to determine if theres any available purchases.

        Parameters:
        -----------
        item: :class:`Item`
            The item we want to buy
        """
        self.check_status()
        self.notify("Getting available purchases...")

        # prepare variables
        box_nr = 0
        purchases = []

        for attempt in range(item.refreshes + 1):
            # attempt is > 0
            if attempt:
                self.refresh()

            # loop over slots, avoided for loop because may need the same slot twice
            while box_nr < 9:

                # get region of the status and price
                status_region = self.purchase_grid[box_nr]
                price_region = self.price_grid[box_nr]

                # get item status
                if self.item_available(status_region):

                    # screenshot the price and move to the purchase button
                    pg.screenshot(f"images/{box_nr}_price.png", region=price_region)

                    # attempt to purchase the item, get success state and quantity
                    success, amount = self.do_purchase(
                        self.rect_to_center(status_region)
                    )
                    self.notify(f"Purchase succeeded: {success}\nQuanitity: {amount}")

                    # add the purchase to our purchases to post to discord later
                    if success:
                        purchases.append((f"images/{box_nr}_price.png", amount))
                        box_nr = 0

                        # wait for the items to refresh...
                        counter = 0
                        while not self.topslot_is_loaded():
                            self.sleep(0.1)
                            counter += 1
                            if counter > 3:
                                break
                        else:
                            self.notify("Another item took the top slot!")
                            continue
                        break

                    # someone was faster, continue to next slot
                    self.notify("Purchase failed!")

                # item is already out of stock, just skip and get the next instead
                elif self.item_out_of_stock(status_region):
                    self.notify(f"Box {box_nr + 1} is out of stock! Skipping...")
                    box_nr += 1

                else:
                    self.notify(f"No items available for purchase!")
                    break

        # post purchases to discord if there were any
        if purchases:
            Thread(target=lambda: self.post_profit(item, purchases)).start()


class SearchBar(TarkovBot):
    """Flea market ui search bar
    -------------------------------
    Searches for the passed image, awaits changes for fastest speed,
    uses clipboard to paste names instead of writing it out.

    Parameters:
    ------------
    item: :class:`Item`
        The Item object we want to find

    Raises:
    ------------
    """

    def __init__(self, item):
        super().__init__()
        self.item: Item = item

    def is_searching(self) -> bool:
        """Checks if the search bar is currently searching"""
        return (
            pg.locateOnScreen(
                "images/searching.png", region=(572, 102, 30, 34), confidence=0.7
            )
            is not None
        )

    def disable_price_filter(self):
        """Disables the price filter, otherwise items cant be found"""
        if x := pg.locateCenterOnScreen(
            "images/max_price.png", region=(753, 51, 40, 21), confidence=0.7
        ):
            self.move_to(x)
            self.click(0.3)

    def search_item(self):
        """Searches for the items name"""
        self.check_status()

        # disable the old price filter
        self.disable_price_filter()

        # move into searchbar
        self.move_to(197, 124)
        self.click(0.3)

        # put name into clipboard and paste it into searchbar
        self.set_clipboard(self.item.name)
        pg.hotkey("ctrl", "v")
        self.sleep(0.2)
        self.move_to(84, 165)
        self.sleep(0.2)

        # await items found
        while self.is_searching():
            pass

        while (
            not pg.pixelMatchesColor(85, 163, (206, 205, 195), tolerance=15)
            and not pg.pixelMatchesColor(85, 166, (199, 198, 188), tolerance=15)
            and not pg.pixelMatchesColor(85, 161, (221, 221, 215), tolerance=15)
            and not pg.pixelMatchesColor(90, 164, (200, 199, 190), tolerance=15)
        ):
            pass

        # click the found item bar to make them display
        self.notify("Item found!")
        self.click(0.4)


class Filter(TarkovBot):
    """Flea market filter ui
    ---------------------------
    Handles the flea markets filter tool by filtering for for the passed
    items properties.

    Paramter:
    ----------
    item: :class:`Item`
        The item to filter for


    Raises:
    ---------
    `FilterDidntOpen` if the filter tool could not be opened
    """

    CURRENCIES = {
        "Any": (663, 149),
        "RUB": (662, 180),
        "USD": (662, 208),
        "EUR": (662, 239),
    }

    def __init__(self, item) -> None:
        super().__init__()
        self.item: Item = item

    def filter_is_open(self) -> bool:
        """Checks if the menu is open"""
        return pg.pixelMatchesColor(859, 81, (174, 106, 81), tolerance=20)

    def currency_is_set(self) -> bool:
        """Checks if a currency is already set"""
        return pg.pixelMatchesColor(515, 148, (191, 198, 194), tolerance=20)

    def open(self):
        """Opens the filter ui"""
        self.check_status()
        start = time.time()

        self.notify("Opening the filter ui...")
        self.move_to(481, 86)
        self.click(0.2)

        while not self.filter_is_open():
            self.sleep(0.1)

            if self.has_timedout(start, 10):
                raise FilterDidntOpen

        self.notify("Filter ui opened!")

    def set_currency(self):
        """Sets the filter to the items currency"""
        self.check_status()

        # check if currency is set correctly, bad currency > errors
        if self.currency_is_set():
            self.notify("Currency is already set.")
            return

        self.notify(f"Setting currency to: {self.item.currency}")

        # get currency point from currency dict and set it
        self.move_to(654, 124)
        self.click(0.2)
        self.move_to(self.CURRENCIES[self.item.currency])
        self.click(0.2)

    def set_price(self):
        """Sets the max price of the item"""
        self.check_status()
        self.notify(f"Setting price to: {self.item.buy_at}")

        # set price, again by using copy paste to speed things up
        self.move_to(797, 153)
        self.click(0.1)
        self.set_clipboard(str(self.item.buy_at))
        pg.hotkey("ctrl", "v")

    def confirm_search(self):
        """Confirm the filter"""
        self.move_to(611, 439)
        self.click(0.1)

    def configurate(self):
        """Sets all filter settings."""
        self.open()
        self.set_currency()
        self.set_price()
        self.confirm_search()

        self.notify("Filter set!")


class MarketDidntOpenError(Exception):
    """Raised when the market could not be opened"""


class FilterDidntOpen(Exception):
    """Raised when the filter ui could not be opened"""


class NoMoneyLeft(Exception):
    """Raised when out of money"""

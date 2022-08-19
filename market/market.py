from threading import Thread
from item import Database, Item
from market.filter import Filter
from market.searchbar import SearchBar
from market.purchase import Purchase, PurchaseHandler
from screen import mask, process_tess_image
from tarkov import Discord, TarkovBot, BotTerminated
import pyautogui as pg
import time
from PIL import Image
import pytesseract as tes
import cv2 as cv

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
        self.started_searching = time.time()

    def check_status(self) -> None:
        """Checks if the bot is terminated or paused"""
        if not self.running:
            raise BotTerminated

        while self.paused:
            time.sleep(0.1)

        if self.has_timedout(self.started_searching, 20):
            raise TimeoutError

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

        self.sleep(0.2)
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

    def get_error(self):
        self.get_screenshot("images/temp/error.png", region=(708, 456, 497, 176))
        processed = mask("images/temp/error.png")

        error = tes.image_to_string(processed, config="--psm 8 -l eng").strip()
        self.discord.send_message(error)
        self.press("esc")
        self.sleep(1)

    def get_item_price(self, item, img):
        """Processes the image of the item price and ocr's it"""
        self.check_status()
        self.notify("Getting item price...")

        img = process_tess_image(img)
        cv.imwrite("images/temp/sample.png", img)
        # process passed image and ocr it, remove blankspaces
        price = tes.image_to_string(
            img, config="-c tessedit_char_whitelist=1234567890 --psm 8 -l eng"
        ).strip()

        return self.validate_price(item, price)

    def captcha_appeared(self):
        return (
            pg.locateOnScreen(
                "Images/captcha.png", region=(577, 45, 775, 1007), confidence=0.7
            )
            is not None
        )

    def validate_price(self, item: Item, price: int):
        """Takes an item and the price we think we bought it for and checks
        if that could be a valid price.
        """
        allowed_profit = 0.9
        profit_limit = int(item.price) * allowed_profit

        if (
            int(price) > int(item.buy_at)
            or (int(item.price) - int(price)) > profit_limit
        ):
            return item.buy_at

        return price

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
                bought_for = self.get_item_price(item, purchase[0])
                profit = (int(item.price) - int(bought_for)) * purchase[1]

                purchase = Purchase(
                    item=item,
                    bought_at=bought_for,
                    amount=purchase[1],
                    profit=profit,
                    image=item.image,
                )
                self.discord.send_purchase_embed(purchase)
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
        purchases = []
        purchase_ui = PurchaseHandler()
        items_bought = 0

        for attempt in range(item.refreshes + 1):

            box_nr = 0
            self.started_searching = time.time()

            # attempt is > 0
            if attempt:
                self.refresh()

            # loop over slots, avoided for loop because may need the same slot twice
            while box_nr < 9:

                # get region of the status and price
                status_region = self.purchase_grid[box_nr]
                price_region = self.price_grid[box_nr]

                # get item status
                if purchase_ui.is_available(status_region):

                    # screenshot the price and move to the purchase button
                    self.get_screenshot(
                        f"images/temp/{items_bought}_price.png", region=price_region
                    )

                    if not item.image:
                        data = Database()
                        data.add_image(item)

                    # attempt to purchase the item, get success state and quantity
                    success, amount = purchase_ui.do_purchase(
                        self.rect_to_center(status_region)
                    )
                    self.notify(f"Purchase succeeded: {success}\nQuanitity: {amount}")

                    # add the purchase to our purchases to post to discord later
                    if success:
                        purchases.append(
                            (f"images/temp/{items_bought}_price.png", amount)
                        )
                        box_nr = 0
                        items_bought += 1

                        # wait for the status to refresh...
                        while purchase_ui.is_pending(status_region):
                            pass

                        self.sleep(0.1)

                        if self.topslot_is_loaded():
                            self.notify("Another item took the top slot!")
                            continue
                        break

                    # someone was faster, continue to next slot
                    self.notify("Purchase failed!")

                # item is already out of stock, just skip and get the next instead
                elif purchase_ui.is_out_of_stock(status_region):
                    self.notify(f"Box {box_nr + 1} is out of stock! Skipping...")
                    box_nr += 1

                else:
                    self.notify(f"No items available for purchase!")
                    break

        if purchases:
            self.notify(f"Posting profits: {purchases}")
            Thread(target=lambda: self.post_profit(item, purchases)).start()


class MarketDidntOpenError(Exception):
    """Raised when the market could not be opened"""

from threading import Thread
from data.items import Database, Inventory, Item
from market.filter import Filter
from market.searchbar import SearchBar
from market.purchase import PurchaseHandler
from tarkov import TarkovBot, BotTerminated
import pyautogui as pg
from nightmart_bot import Discord
import time
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

    def captcha_appeared(self) -> bool:
        return (
            pg.locateOnScreen(
                "Images/captcha.png", region=(577, 45, 775, 1007), confidence=0.7
            )
            is not None
        )

    def topslot_is_loaded(self) -> bool:
        """Checks if the topmost slot has an item in it"""
        return (
            pg.locateOnScreen(
                "images/available.png", region=(1845, 139, 28, 25), confidence=0.8
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

    def refresh(self):

        while not pg.pixelMatchesColor(1833, 121, (207, 217, 222), tolerance=30):
            self.sleep(0.1)
            self.notify("Waiting to be able to refresh...")

        self.move_to(1839, 118)
        self.click(0.2)

        while not self.items_listed():
            self.sleep(0.01)
            self.notify("Waiting for listed items...")

    def get_available_purchases(self, item: Item, inventory: Inventory):
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
        purchase_ui = PurchaseHandler()
        purchases = []

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
                path = "images/temp/price.png"

                # get item status
                if purchase_ui.is_available(status_region):

                    # screenshot the price and move to the purchase button
                    self.get_screenshot(path, region=price_region)
                    data = Database()
                    if not data.has_image(item):
                        data.add_image(item)

                    # attempt to purchase the item, get success state and quantity
                    success, amount = purchase_ui.do_purchase(
                        self.rect_to_center(status_region)
                    )
                    self.notify(f"Purchase succeeded: {success}\nQuanitity: {amount}")

                    # add the purchase to our purchases to post to discord later
                    if success:
                        inventory.slots_taken += int(amount) * item.size
                        box_nr = 0

                        # wait for the status to refresh...
                        while purchase_ui.is_pending(status_region):
                            pass

                        purchase = purchase_ui.post_profit(
                            item, inventory, {"price": path, "quantity": int(amount)}
                        )
                        if purchase:
                            purchases.append(purchase)

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

        return inventory, purchases


class MarketDidntOpenError(Exception):
    """Raised when the market could not be opened"""

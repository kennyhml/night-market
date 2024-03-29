from threading import Thread
from data.items import Database, Inventory, Item
from market.filter import Filter
from market.searchbar import SearchBar
from market.purchase import PurchaseHandler
from tarkov import TarkovBot
import pyautogui as pg
import time
from nightmart_bot import Discord

class MarketUI(TarkovBot):
    """Main flea market ui handle
    ---------------------------
    Inherits from TarkovBot
    Has all methods needed in order to buy items from the flea market.

    Raises:
    --------
    - `MarketDidntOpenError` if the market could not be opened.
    """

    # locations of purchase and price regions from top down
    purchase_grid = [(1678, y_axis, 192, 73) for y_axis in range(143, 937, 72)]
    price_grid = [(1333, y_axis, 172, 26) for y_axis in range(160, 951, 72)]

    def __init__(self) -> None:
        super().__init__()

    def is_open(self) -> bool:
        """Checks if the market is open"""
        return pg.locateOnScreen(
            "images/filter_settings.png", region=(462, 66, 38, 36), confidence=0.7
        )

    def items_listed(self) -> bool:
        """Checks if items are already listed"""
        return pg.locateOnScreen(
            "images/price_sort_arrow.png",
            region=(1419, 112, 28, 22),
            confidence=0.7,
        )

    def captcha_appeared(self) -> bool:
        """Checks if a captcha has appeared"""
        return pg.locateOnScreen(
            "images/captcha.png", region=(577, 45, 775, 1007), confidence=0.7
        )

    def topslot_is_loaded(self) -> bool:
        """Checks if the topmost slot has an item in it"""
        return pg.locateOnScreen(
            "images/available.png", region=(1845, 139, 28, 25), confidence=0.8
        )

    def await_market_open(self):
        """Awaits the market to open, raises a TimeoutError after 10s"""
        counter = 0
        while not self.is_open():
            self.sleep(0.1)
            counter += 1
            if counter > 100:
                raise TimeoutError

    def await_items_listed(self):
        self.notify("Awaiting items to be listed...")
        c = 0
        while not self.items_listed():
            self.sleep(0.1)
            c += 1
            if c > 100:
                raise TimeoutError(
                    "Could not detect items listed, this could "
                    "be caused by an internet error or the price "
                    "filter being set incorrectly."
                )

    def await_refresh_available(self):
        """Waits to be able to refresh"""
        self.notify("Waiting to refresh again...")
        c = 0
        while not pg.pixelMatchesColor(1833, 121, (207, 217, 222), tolerance=30):
            self.sleep(0.1)
            c += 1
            if c > 100:
                raise TimeoutError("Could not refresh after 5s!")

    def open(self):
        """Opens the flea market tab, most of the time will already be open"""
        if not self.is_open():
            # not already open
            print("Opening...")
            self.move_to(1251, 1063)
            self.click()
            self.await_market_open()

        self.notify("Opened the flea market!")
        self.sleep(1)
        if self.config["use_wishlist"] and pg.pixelMatchesColor(
            161, 83, (188, 188, 164), tolerance=40
        ):
            self.move_to(250, 86)
            self.click()
            print("Opening wishlist tab...")

        elif not pg.pixelMatchesColor(162, 91, (190, 188, 161), tolerance=40):
            self.move_to(112, 86)
            self.click()
            print("Opening purchase tab...")


    def search_item(self, item: Item) -> None:
        """Searches for an item and sets the filter given the items properties

        Parameters:
        ------------
        item: :class:`Item`
            The item object to search and buy if possible
        """
        self.notify(f"Searching for {item.name}...")
        start = time.time()

        # search items name
        searchbar = SearchBar(item)
        searchbar.search_item()

        # set filter
        filter = Filter(item)
        filter.configurate()
        self.sleep(0.2)

        # await items listed
        self.await_items_listed()
        self.notify(f"Searching for {item.name} took {self.get_time(start)}s")
        
    def refresh(self):
        """Refreshes the currently listed item"""
        # get cursor in position for new purchase and await refresh
        self.move_to(1776, 182)
        self.await_refresh_available()

        self.press("F5")
        self.sleep(0.1)

        start = time.time()
        self.await_items_listed()
        self.notify(f"Items listed after {self.get_time(start)}s")

    def check_anomaly(self):
        if not self.config["purchase_failsafe"]:
            return
            
        if pg.pixelMatchesColor(1875, 180, (170, 179, 183), tolerance=40):
            discord = Discord()
            discord.send_image(
                self.get_screenshot("images/temp/anomaly"),
                "**Anomaly detected!** Not purchasing...",
            )
            raise TooManyItems

    def process_price(self, item, region, handler):
        self.notify("Started processing price...")
        get_price = Thread(
            target=handler.get_item_price,
            args=(item, region),
            name="Processing price",
        )
        get_price.start()

    def go_next_purchase(self, region) -> bool:
        while PurchaseHandler.is_pending(region):
            pass
        
        return self.topslot_is_loaded()


    def get_available_purchases(self, item: Item, inventory: Inventory):
        """Main purchase finding function, checks the status of each item slot
        to determine if theres any available purchases.

        Parameters:
        -----------
        item: :class:`Item`
            The item we want to buy

        inventory: :class:`Inventory`
            The instance of the current inventory to add slots to

        Returns:
        -----------
        inventory: :class:`Inventory`
            The updated inventory

        purchases: :class:`list[Purchase]`
            A list of purchases
        """
        self.check_status()
        self.notify("Getting available purchases...")

        # prepare variables
        purchase_ui = PurchaseHandler()
        purchases = []
        founds = set()

        data = Database()
        grab_img = not data.has_image(item)

        for attempt in range(item.refreshes + 1):
            box_nr = 0
            if attempt:
                self.refresh()

            # loop over slots, avoided for loop because may need the same slot twice
            while box_nr < 6:

                # get region of the status and price
                status_region = self.purchase_grid[box_nr]
                price_region = self.price_grid[box_nr]

                # get item status
                if purchase_ui.is_available(status_region):
                    self.check_anomaly()
                    founds.add(attempt)

                    if grab_img:
                        data.add_image(item)
                        grab_img = False

                    # thread the price OCR beforehand so we have the data ready
                    # attempt to purchase the item, get success state and quantity
                    self.process_price(item, price_region, purchase_ui)
                    success, amount, skip = purchase_ui.do_purchase(
                        self.rect_to_center(status_region)
                    )

                    # check if the purchase succeeded
                    if not success:
                        self.notify("Purchase failed!")
                        continue

                    inventory.add_items(int(amount), item.size)
                    purchase = purchase_ui.post_profit(item, inventory, int(amount))
                    if purchase:
                        purchases.append(purchase)
                    box_nr += 1

                    # only skip to next slot if the purchase was full amount
                    if not skip:
                        box_nr = 0

                    if not self.go_next_purchase(status_region):
                        break

                # item is already out of stock, just skip and get the next instead
                elif purchase_ui.is_out_of_stock(status_region):
                    self.notify(f"Box {box_nr + 1} is out of stock! Skipping...")
                    box_nr += 1

                else:
                    break

        return inventory, purchases, len(founds)

    def unstuck(self):
        self.press("esc", 1)
        self.open()
        self.sleep(0.5)


class TooManyItems(Exception):
    """Raised when too many items are listed"""

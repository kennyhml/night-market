from threading import Thread
from data.items import Database, Inventory, Item
from market.filter import Filter
from market.searchbar import SearchBar
from market.purchase import PurchaseHandler
from tarkov import TarkovBot
import pyautogui as pg
from nightmart_bot import Discord
import time


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
        self.discord = Discord()

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
        """Awaits the market to open, raises a TimeoutError after 5 minutes"""
        counter = 0
        while not self.is_open():
            self.sleep(0.1)
            counter += 1
            if counter > 50:
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
        if self.is_open():
            return

        # not already open
        self.move_to(1251, 1063)
        self.click()
        self.await_market_open()

        self.notify("Opened the flea market!")

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
            while box_nr < 9:

                # get region of the status and price
                status_region = self.purchase_grid[box_nr]
                price_region = self.price_grid[box_nr]
                path = "images/temp/price.png"

                # get item status
                if purchase_ui.is_available(status_region):
                    founds.add(attempt)

                    if grab_img:
                        data.add_image(item)
                        grab_img = False

                    # thread the price OCR beforehand so we have the data ready
                    self.get_screenshot(path, region=price_region)
                    get_price = Thread(
                        target=purchase_ui.get_item_price,
                        args=(item, path),
                        name="Processing price",
                    )
                    get_price.start()

                    # attempt to purchase the item, get success state and quantity
                    success, amount = purchase_ui.do_purchase(
                        self.rect_to_center(status_region)
                    )
                    self.notify(f"Purchase succeeded: {success}\nQuanitity: {amount}")

                    # add the purchase to our purchases to post to discord later
                    if not success:
                        # someone was faster, continue to next slot
                        self.notify("Purchase failed!")
                        continue

                    inventory.add_items(int(amount), item.size)
                    purchase = purchase_ui.post_profit(item, inventory, int(amount))

                    if purchase:
                        purchases.append(purchase)

                    # wait for the status to refresh...
                    box_nr = 0
                    while purchase_ui.is_pending(status_region):
                        pass

                    if self.topslot_is_loaded():
                        continue
                    break

                # item is already out of stock, just skip and get the next instead
                elif purchase_ui.is_out_of_stock(status_region):
                    self.notify(f"Box {box_nr + 1} is out of stock! Skipping...")
                    box_nr += 1

                else:
                    break

        return inventory, purchases, len(founds)

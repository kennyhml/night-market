from data.items import Item
from tarkov import TarkovBot, BotTerminated
import pyautogui as pg
import time

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
        "₽": (662, 180),
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

        self.notify("Opening the filter ui...")
        self.move_to(481, 86)
        self.click(0.2)

        c = 0
        while not self.filter_is_open():
            self.sleep(0.1)
            c += 1
            
            if c > 100:
                raise TimeoutError("Filter didnt open within 10s!")

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
        self.click(0.2)
        self.set_clipboard(str(self.item.buy_at))
        pg.hotkey("ctrl", "v")

    def confirm_search(self):
        """Confirm the filter"""
        self.move_to(611, 439)
        self.click(0.2)

    def configurate(self):
        """Sets all filter settings."""
        self.open()
        self.set_currency()
        self.set_price()
        self.confirm_search()

        self.notify("Filter set!")

class FilterDidntOpen(Exception):
    """Raised when the filter ui could not be opened"""



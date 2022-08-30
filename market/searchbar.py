from screen import Screen
from data.items import Item
from tarkov import TarkovBot, lg
import pyautogui as pg


class SearchBar(TarkovBot):
    """Flea market search bar
    -------------------------------
    Searches for the passed image, awaits changes for fastest speed,\n
    uses clipboard to paste names instead of writing it out.

    Parameters:
    ------------
    item: :class:`Item`
        The Item object we want to find

    Raises:
    ------------
    :class:`TimeoutError`
        When something took too long

    :class:`NoItemsListed`
        When no items were listed after 5 seconds
    """

    def __init__(self, item):
        super().__init__()
        self.item: Item = item

    def click(self, delay=0.3, button="left") -> None:
        """Override click method for click delays"""

        self.check_status()
        lg.info(f"Clicking button: {button}; Delay: {delay}")
        multiplier = self.config["search_speed"]
        if multiplier != 1:
            multiplier = 1 + (multiplier * 0.2)
        delay = delay * multiplier

        # split the delay before and after the click
        self.sleep((delay / 2))
        pg.click(button=button)
        self.sleep((delay / 2))

    def done_searching(self) -> bool:
        """Checks if the search bar is done searching"""
        return pg.locateOnScreen(
            "images/searching.png", region=(572, 102, 30, 34), confidence=0.7
        )

    def get_price_filter_position(self) -> None | tuple:
        """Gets position of the price filter"""
        return pg.locateCenterOnScreen(
            "images/max_price.png", region=(753, 51, 70, 21), confidence=0.7
        )

    def disable_price_filter(self):
        """Disables the price filter, otherwise items cant be found"""
        if pos := self.get_price_filter_position():
            self.move_to(pos)
            self.click(0.3)

    def await_item_found(self):
        """Waits for the magnifying glass icon to be visible"""
        self.notify("Awaiting search finished...")
        c = 0
        while not self.done_searching():
            self.sleep(0.1)
            c += 1
            if c > 100:
                raise TimeoutError("More than 10s passed while searching!")

    def await_item_icon(self):
        """Waits for enough white pixels on the icon position"""
        self.notify("Awaiting item icon...")
        c = 0
        while not Screen.icon_loaded():
            self.sleep(0.1)
            c += 1
            if c > 50:
                raise NoItemsListed

    def search_item(self):
        """Searches for the items name in the searchbar"""

        # disable the old price filter
        self.disable_price_filter()

        # move into searchbar
        self.move_to(197, 124)
        self.click(0.4)

        # put name into clipboard and paste it into searchbar
        if self.config["item_searching"] == "Copy & paste":
            self.set_clipboard(self.item.name)
            self.sleep(0.2)
            pg.hotkey("ctrl", "v")
            self.sleep(0.2)
        else:
            pg.typewrite(self.item.name, interval=0.05)
        self.move_to(84, 165)
        self.sleep(0.2)

        # await item found
        self.await_item_found()
        self.await_item_icon()

        # click the found item bar to make them display
        self.notify("Item found!")
        self.click(0.3)


class NoItemsListed(Exception):
    """Raised when no item was listed after 5s"""

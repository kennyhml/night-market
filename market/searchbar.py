from screen import Screen
from data.items import Item
from tarkov import TarkovBot, BotTerminated
import pyautogui as pg


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

    def search_item(self):
        """Searches for the items name"""
        self.check_status()

        # disable the old price filter
        self.disable_price_filter()

        # move into searchbar
        self.move_to(197, 124)
        self.click(0.4)

        # put name into clipboard and paste it into searchbar
        self.set_clipboard(self.item.name)
        pg.hotkey("ctrl", "v")
        self.sleep(0.2)
        self.move_to(84, 165)
        self.sleep(0.2)

        # await items found
        c = 0
        while self.is_searching():
            self.sleep(0.1)
            c += 1

            if c > 100:
                raise TimeoutError("More than 10s passed while searching!")

        c = 0
        while not Screen.icon_loaded():
            self.sleep(0.1)
            c += 1

            if c > 100:
                raise TimeoutError("More than 10s passed awaiting the icon!")

        # click the found item bar to make them display
        self.notify("Item found!")
        self.click(0.3)

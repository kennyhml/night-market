from dataclasses import dataclass
from data.items import Inventory, Item
from tarkov import TarkovBot
import pyautogui as pg
from pytesseract import pytesseract as tes
from screen import Screen
from PIL import Image

@dataclass
class Vendor:
    name: str
    location: tuple


VENDORS = {
    "fence": Vendor(name="Fence", location=(1049, 423)),
    "Therapist": Vendor(name="Therapist", location=(874, 420)),
}


class VendorHandler(TarkovBot):
    """Handles selling items at the vendor
    ------------------------
    Contains all methods needed to open the trader and sell
    all the items. Returns the current money after selling.
    """
    grid = [
        (x_axis, y_axis, 64, 64)
        for y_axis in range(261, 827, 63)
        for x_axis in range(1270, 1900, 63)
    ]

    def is_open(self) -> bool:
        """Checks if the trader is open"""
        return pg.locateOnScreen(
            "images/trader_open.png", region=(1234, 837, 35, 33), confidence=0.7
        )

    def on_sell_tab(self):
        """Checks if the sell tab is open"""
        return pg.pixelMatchesColor(275, 41, (186, 190, 190), tolerance=30)

    def open(self):
        """Opens the main trader window"""
        if not self.is_open():
            self.move_to(1114, 1061)
            self.click(0.5)

    def open_sell_tab(self):
        """Opens the selling tab"""
        if not self.on_sell_tab():
            self.move_to(236, 45)
            self.click(1)

    def open_trader(self, vendor: Vendor):
        """Opens the trader"""
        self.move_to(vendor.location)
        self.click(0.8)

    def sell(self, vendor, inventory: Inventory, items):
        self.open()
        self.open_trader(VENDORS[vendor])
        self.open_sell_tab()
        self.sell_items(inventory, items)
        self.confirm_sell()

        return Screen.read_current_money()

    def sell_items(self, inventory: Inventory, items: list[Item]):
        """Takes a list of items and puts all of them into the sell window"""
        sell_slots = 0

        for i in range(3):
            if i:
                for _ in range(9):
                    pg.scroll(-8)
                    self.sleep(0.01)
                self.sleep(1)
            
            for item in items:
                image = item.name.replace('"', '')
                
                points = set(pg.locateAllOnScreen(f"images/inv/{image}.png", region=(1270, 259, 643, 748), confidence=0.6))

                if item.size in [2, 3, 5, 7]:
                    turned = Image.open(f"images/inv/{image}.png")
                    turned = turned.rotate(270, expand=True)
                    points.union(set(pg.locateAllOnScreen(turned, region=(1270, 259, 643, 748), confidence=0.85)))

                occurrences = Screen.filter_close_points(points, diff=10)
                points = [Screen.rect_to_center(point) for point in occurrences]

                for point in points:
                    if sell_slots > 64:
                        self.confirm_sell()
                        sell_slots = 0

                    pg.moveTo(point)
                    with pg.hold("ctrl"):
                        for _ in range(2):
                            self.click(0.05)
                        sell_slots += item.size

    def confirm_sell(self):
        self.move_to(964, 182)
        self.click(2)
        
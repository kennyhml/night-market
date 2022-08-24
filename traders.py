from dataclasses import dataclass
from data.items import Inventory
import screen
from tarkov import TarkovBot
import pyautogui as pg
from pytesseract import pytesseract as tes
from PIL import Image
from screen import Screen

@dataclass
class Vendor:
    name: str
    location: tuple


VENDORS = {
    "fence": Vendor(name="Fence", location=(1049, 423)),
    "Therapist": Vendor(name="Therapist", location=(874, 420)),
}


class VendorUi(TarkovBot):

    grid = [
        (x_axis, y_axis, 64, 64)
        for y_axis in range(261, 827, 63)
        for x_axis in range(1270, 1900, 63)
    ]

    def is_open(self) -> bool:
        return pg.locateOnScreen(
            "images/trader_open.png", region=(1234, 837, 35, 33), confidence=0.7
        )

    def on_sell_tab(self):
        return pg.pixelMatchesColor(275, 41, (186, 190, 190), tolerance=20)

    def open(self):
        """Opens the main trader window"""
        if not self.is_open():
            self.move_to(1114, 1061)
            self.click(0.5)

    def open_sell_tab(self):
        """Opens the selling tab"""
        self.move_to(236, 45)
        self.click(1)

    def open_trader(self, vendor: Vendor):
        self.move_to(vendor.location)
        self.click(0.8)

    def sell(self, vendor, inventory: Inventory):
        self.open()
        self.open_trader(VENDORS[vendor])
        self.open_sell_tab()
        self.sell_items(inventory)
        self.confirm_sell()
        self.sleep(1)
        
        return Screen.read_current_money()

    def sell_items(self, inventory: Inventory):
        """Takes a list of items and puts all of them into the sell window"""

        for i, box in enumerate(self.grid):
            if i >= inventory.total_slots:
                return

            self.move_to(
                (
                    round(box[0] + (0.5 * box[2])),
                    round(box[1] + (0.5 * box[3])),
                )
            )
            if not i:
                self.sleep(1)

            with pg.hold("ctrl"):
                self.click(0.05)

            if i == 60:
                self.confirm_sell()
                self.sleep(0.5)

    def confirm_sell(self):
        self.move_to(964, 182)
        self.click(0.4)
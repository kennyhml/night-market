from dataclasses import dataclass
from data.items import Inventory, Item, Database
from tarkov import TarkovBot, lg
import pyautogui as pg
from screen import Screen
from PIL import Image


@dataclass
class Vendor:
    name: str
    location: tuple


VENDORS = {
    "Fence": Vendor(name="Fence", location=(1049, 423)),
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

    def click(self, delay=0.3, button="left") -> None:
        """Override click method for click delays"""
        self.check_status()

        multiplier = self.config["sell_speed"]
        if multiplier != 1:
            multiplier = 1 + (multiplier * 0.2)
        delay = delay * multiplier

        # split the delay before and after the click
        self.sleep((delay / 2))
        pg.click(button=button)
        self.sleep((delay / 2))

    def is_open(self) -> bool:
        """Checks if the trader is open"""
        return pg.locateOnScreen(
            "images/trader_open.png", region=(1234, 837, 35, 33), confidence=0.7
        )

    def on_sell_tab(self) -> bool:
        """Checks if the sell tab is open"""
        return pg.pixelMatchesColor(275, 41, (186, 190, 190), tolerance=30)

    def open(self) -> None:
        """Opens the main trader window"""
        if not self.is_open():
            self.move_to(1114, 1061)
            self.click(0.5)

    def open_sell_tab(self) -> None:
        """Opens the selling tab"""
        if not self.on_sell_tab():
            self.move_to(236, 45)
            self.click(1)

    def open_trader(self, vendor: Vendor) -> None:
        """Opens the trader"""
        self.move_to(vendor.location)
        self.click(0.8)

    def sell(self, items: list[Item], inventory: Inventory) -> int:
        """Sells the item at their respective vendors"""
        # open the main vendor tab
        self.open()

        # generate a dictionary of vendors with the items to sell at them
        sell_at = {
            vendor: [item for item in items if item.vendor == vendor]
            for vendor in VENDORS
        }

        # for each vendor that has items, open it and sell those items
        for i, vendor in enumerate(sell_at):
            # check that the vendor actually has items
            if not sell_at[vendor]:
                continue
            # sell all the items at the vendor
            self.notify(f"Selling at {vendor}: {sell_at[vendor]}")
            self.open_trader(VENDORS[vendor])
            self.open_sell_tab()
            self.sell_items(sell_at[vendor], inventory)
            self.confirm_sell()

            # check if its the last vendor in the list to not leave the tab
            if i + 1 == len(sell_at):
                self.notify("Reached the last vendor...")
                break

            self.press("esc")
            self.sleep(2)

        return Screen.read_current_money()

    def scroll_down(self) -> None:
        """Scrolls down approx. one page"""
        for _ in range(9):
            pg.scroll(-8)
            self.sleep(0.01)

    def locate_all_occurences(self, item: Item) -> list[tuple]:
        """Finds all occurrences of an item in the inventory"""
        # find all points of the image
        image = item.name.replace('"', "")
        database = Database()
        if not database.has_image(item):
            return
        points = set(
            pg.locateAllOnScreen(
                f"images/inv/{image}.png",
                region=(1270, 259, 643, 748),
                confidence=0.7,
            )
        )
        # if item could be rotated, check for the flipped image
        if not item.size in [1, 4]:
            original = Image.open(f"images/inv/{image}.png")
            w,h = original.size
            no_price = original.crop((20, 20, w, h))
            turned = no_price.rotate(270, expand=True)
            points = points.union(
                set(
                    pg.locateAllOnScreen(
                        turned, region=(1270, 259, 643, 748), confidence=0.7
                    )
                )
            )

        # filte the occurrences by close points (multipel matches on same slot)
        occurrences = Screen.filter_close_points(points, diff=10)
        return [Screen.rect_to_center(point) for point in occurrences]

    def sell_items(self, items: list[Item], inventory: Inventory) -> None:
        """Takes a list of items and sells all of them"""
        sell_slots = 0

        # number of scrolls
        for i in range(inventory.allowed_scrolls):
            # only scroll down if its not the first sale
            if i:
                self.scroll_down()
                self.sleep(1)

            # check each item in the passed items
            for item in items:
                points = self.locate_all_occurences(item)
                if not points:
                    if i == 0:
                        self.move_to(1700, 500)
                    continue
                for point in points:
                    # check if the sell field is nearly full
                    if sell_slots > 64:
                        self.confirm_sell()
                        sell_slots = 0

                    # move to each point and click the item
                    pg.moveTo(point)
                    with pg.hold("ctrl"):
                        for _ in range(2):
                            self.click(0.05)
                        sell_slots += item.size

    def confirm_sell(self) -> None:
        """Confirm the sell"""
        self.move_to(964, 182)
        self.click(2)

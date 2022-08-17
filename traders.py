from dataclasses import dataclass

from tarkov import TarkovBot
import pyautogui as pg


@dataclass
class Therapist:
    name = "Therapist"
    location = (874, 420)


@dataclass
class Fence:
    name = "Fence"
    location = (1049, 423)


str_to_instance = {"Therapist": Therapist, "Fence": Fence}


class SellUi(TarkovBot):

    grid = [
        (x_axis, y_axis, 38, 38)
        for y_axis in range(261, 701, 63)
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

    def sell_items(self):
        """Takes a list of items and puts all of them into the sell window"""

        for i, box in enumerate(self.grid):
            if i >= 70:
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

"""
a = SellUi()
a.sell_items()
"""
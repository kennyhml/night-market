from dataclasses import dataclass
import screen
from tarkov import TarkovBot
import pyautogui as pg
from pytesseract import pytesseract as tes
from PIL import Image

@dataclass
class Therapist:
    name = "Therapist"
    location = (874, 420)


@dataclass
class Fence:
    name = "Fence"
    location = (1049, 423)


str_to_instance = {"Therapist": Therapist, "Fence": Fence}


class TraderUi(TarkovBot):
    last_known = None

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

    def open_trader(self, pos):
        self.move_to(pos)
        self.click(0.8)

    def sell(self, trader):
        self.open()
        self.open_trader(trader)
        self.open_sell_tab()
        self.sell_items()
        self.confirm_sell()

        if self.last_known:
            current_money = self.get_current_money()

            profit = (current_money - self.last_known), current_money
            self.last_known = current_money
            return profit

        self.last_known = self.get_current_money()
        return None, self.last_known

    def sell_items(self):
        """Takes a list of items and puts all of them into the sell window"""

        for i, box in enumerate(self.grid):
            if i >= 80:
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
        self.confirm_sell()
        self.sleep(1)

    def get_current_money(self):

        self.get_screenshot("test.png", region=(1575, 166, 154, 38))

        screen.inv_replace_zeros("test.png")

        res = Image.open("test.png")
        w, h = res.size
        res = res.resize((w * 3, h * 3), 1)
        res.save("test.png")

        img = screen.mask("test.png", (203,200,181))
        res = tes.image_to_string(img, config="-c tessedit_char_whitelist=1234567890 --psm 8 -l eng")

        return int(res)


    def confirm_sell(self):
        self.move_to(964,182)
        self.click(0.4)



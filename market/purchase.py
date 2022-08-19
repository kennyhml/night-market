from dataclasses import dataclass
from item import Item
from screen import mask
from tarkov import Discord, TarkovBot
import pyautogui as pg
from captcha import CaptchaSolver
from pytesseract import pytesseract as tes
from PIL import Image
import cv2 as cv

@dataclass
class Purchase:
    item: Item
    bought_at: int
    amount: int
    profit: int
    image: str

class PurchaseHandler(TarkovBot):
    """Handles purchasing the item"""

    def purchase_window_open(self) -> bool:
        """Checks if the purchase prompt has opened yet"""
        return pg.pixelMatchesColor(1171, 460, (64, 13, 11), tolerance=20)

    def out_of_money(self) -> bool:
        """Checks if we ran out of money"""
        return pg.locateOnScreen(
            "images/not_enough_money.png", region=(752, 466, 154, 36), confidence=0.7
        )

    def purchase_succeeded(self):
        """Checks if a purchase succeeded by matching for the white icon"""
        return pg.locateOnScreen(
            "images/success.png", region=(1347, 1017, 194, 25), confidence=0.7
        )

    def purchase_failed(self):
        """Checks if a purchase failed by matching for the red icon"""
        return pg.locateOnScreen(
            "images/failure.png", region=(1424, 1019, 26, 21), confidence=0.7
        )

    def error_prompt_visible(self):
        """Checks if an error popped up"""
        return pg.locateOnScreen(
            "images/too_many_items.png", region=(915, 554, 90, 45), confidence=0.7
        )

    def item_is_regular_amount(self) -> bool:
        """Checks if the item is only 1"""
        return pg.locateOnScreen(
            "images/regular_amount.png", region=(1089, 473, 48, 31), confidence=0.7
        )

    def captcha_appeared(self):
        return pg.locateOnScreen(
            "Images/captcha.png", region=(577, 45, 775, 1007), confidence=0.7
        )

    def is_available(self, region):
        return (
            pg.locateOnScreen("images/purchase.png", region=region, confidence=0.6)
            is not None
            or pg.locateOnScreen("images/purchase_2.png", region=region, confidence=0.6)
            is not None
        )

    def is_out_of_stock(self, region):
        return pg.locateOnScreen(
            "images/out of stock.png", region=region, confidence=0.7
        )

    def is_pending(self, region):
        return pg.locateOnScreen(
            "Images/pending.png", region=region, confidence=0.5, grayscale=True
        )

    def check_for_captcha(self) -> bool:
        if self.captcha_appeared():
            self.notify("A captcha has appeared!")
            captcha = CaptchaSolver()
            captcha.solve()
            return False, None

    def await_prompt(self):
        """Hits the purchase button and waits for the window"""
        self.check_status()

        # Wait for the red exit button of the prompt
        while not self.purchase_window_open() or self.error_prompt_visible():
            if self.check_for_captcha():
                return False
        return True

    def do_purchase(self, point):
        """Hits the button, awaits until the confirm prompt loads and gets the
        available amount, if amount > 1 then include pressing all.
        """
        self.notify("Buying available item...")
        self.move_to(point)
        self.click(0.2)
        if not self.await_prompt():
            return False, None

        # Grab the amount of items to check if we need to hit the "all" button
        amount = int(self.get_item_amount())
        if amount > 1:
            self.move_to(1146, 490)
            self.click(0.2)

        # Y to confirm, check purchase succeeded, return item quantity
        self.press("Y")
        success, fixed_amount = self.await_purchase_result()
        return success, fixed_amount if fixed_amount else amount

    def purchase_errored(self):
        if self.out_of_money():
            raise NoMoneyLeft

        if (new_amount := self.get_new_amount()) is not None:
            return True, new_amount
        return False, None

    def await_purchase_result(self):
        """Checks if a purchase fails, succeeds or errors.
        Returns success state and a new amount of bought items
        """
        self.check_status()
        self.notify("Awaiting purchase result...")

        # wait for either result to show up
        while True:

            # check captcha
            if self.check_for_captcha():
                return False, None

            # no special error occurred
            if (success := self.purchase_succeeded() is not None) or self.purchase_failed():
                return success, None

            # check for errors
            error, new = self.purchase_errored()
            if error:
                self.notify(f"The amount bought was {new if new else 'not determined'}")
                self.sleep(0.3)
                self.press("esc")
                return True, new
            self.sleep(0.1)

    def get_item_amount(self):
        """Gets the amount of items that can be bought"""
        self.check_status()
        self.notify("Checking item amount...")

        if self.item_is_regular_amount():
            self.notify(f"Quantity: 1")
            return "1"

        # get image showing the amount, process and pass to tesseract
        path = "Images/temp/item_amount.png"
        self.get_screenshot(path, region=(1090, 472, 48, 32))
        processed = mask(path)

        cv.imwrite(path, processed)

        result = (
            tes.image_to_string(
                processed,
                config="-c tessedit_char_whitelist=123/4567890 --psm 8 -l eng",
            )
            .strip()  # remove blankspaces
            .replace("/", "")  # remove the "/"
        )
        # output ocr result
        self.notify(f"Quantity: {result}")
        return result

    def get_new_amount(self):
        """Checks whether a purchase resulted in an error. this could be:
        - Tried to buy more items than available
        - Not enough money (should trigger inventory emptying)
        - Other unknwon errors?
        """
        if self.error_prompt_visible():
            path = "images/temp/amount.png"
            self.notify("Error: Not all items were left!")

            # screenshot the prompt, process and ocr the image
            self.get_screenshot("images/temp/amount.png", region=(1005, 522, 81, 20))
            img = Image.open("images/temp/amount.png")
            w, h = img.size
            img = img.resize((w * 6, h * 6), 1)
            img.save(path)

            # get the new amount
            text: str = tes.image_to_string(
                mask(path),
                config="-c tessedit_char_whitelist=1234567890 --psm 10 -l eng",
            ).strip()
            return "".join(char for char in [c for c in text if c.isdigit()])


class NoMoneyLeft(Exception):
    """Raised when out of money"""

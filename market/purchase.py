from dataclasses import dataclass
from time import time
from data.items import Inventory, Item
from nightmart_bot import Discord
from screen import Screen
from tarkov import TarkovBot
import pyautogui as pg
from data.captcha import CaptchaSolver
from threading import Thread


@dataclass
class Purchase:
    item: Item
    bought_at: int
    amount: int
    profit: int
    image: str


class PurchaseHandler(TarkovBot):
    """Handles purchasing the item"""

    amount = None
    price = None

    def purchase_window_open(self) -> bool:
        """Checks if the purchase prompt has opened yet"""
        return pg.locateOnScreen(
            "images/purchase_prompt.png", region=(815, 416, 556, 130), confidence=0.7
        )

    def out_of_money(self) -> bool:
        """Checks if we ran out of money"""
        return pg.locateOnScreen(
            "images/not_enough_money.png", region=(752, 466, 154, 36), confidence=0.7
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
        return pg.locateOnScreen(
            "images/purchase_3.png", region=region, confidence=0.5, grayscale=True
        ) or pg.locateOnScreen(
            "images/purchase_2.png", region=region, confidence=0.4, grayscale=True
        ) or pg.locateOnScreen(
            "images/purchase.png", region=region, confidence=0.6, grayscale=True
        )

    def is_out_of_stock(self, region):
        return pg.locateOnScreen(
            "images/out of stock.png", region=region, confidence=0.7
        )

    def is_pending(self, region):
        return pg.locateOnScreen(
            "Images/pending.png", region=region, confidence=0.6, grayscale=True
        )

    def amount_changed(self) -> bool:
        return pg.locateOnScreen(
            "images/not_all_items_left.png", region=(716, 458, 120, 45), confidence=0.9
        )

    def inv_full(self) -> bool:
        return pg.locateOnScreen(
            "images/out_of_space.png", region=(716, 458, 120, 45), confidence=0.93
        )

    def offer_sold_out(self) -> bool:
        return pg.locateOnScreen(
            "images/offer_sold_out.png", region=(716, 458, 120, 45), confidence=0.93
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
        self.notify("Awaiting purchase prompt...")

        # Wait for the red exit button of the prompt
        c = 0
        while not self.purchase_window_open() and not self.error_prompt_visible():
            if self.check_for_captcha():
                return False

            c += 1
            if c > 50:
                raise TimeoutError("Timed out awaiting the purchase prompt!")
        return True

    def do_purchase(self, point):
        """Hits the button, awaits until the confirm prompt loads and gets the
        available amount, if amount > 1 then include pressing all.
        """
        self.notify("Buying available item...")
        self.move_to(point)
        self.click()

        self.get_screenshot(("images/temp/pre_purchase.png"), region=(1509, 69, 89, 23))
        if not self.await_prompt():
            return False, None

        # Grab the amount of items to check if we need to hit the "all" button
        self.amount = 1 if self.item_is_regular_amount() else None

        if not self.amount:
            get_amount = Thread(target=lambda: self.get_item_amount())
            get_amount.start()

            self.move_to(1146, 490)
            self.click()
            self.move_to(1780, 118)
        
        # Y to confirm, check purchase succeeded, return item quantity
        self.press("Y")

        while not self.amount:
            self.sleep(0)
        if self.amount > 30:
            self.amount = 10
        success, fixed_amount = self.await_purchase_result()
        return success, fixed_amount if fixed_amount else self.amount

    def await_purchase_result(self):
        """Checks if a purchase fails, succeeds or errors.
        Returns success state and a new amount of bought items
        """
        self.check_status()
        start = time()
        self.notify("Awaiting purchase result...")

        # wait for either result to show up
        while True:

            if not pg.locateOnScreen(
                "images/temp/pre_purchase.png",
                region=(1508, 66, 90, 29),
                confidence=0.98,
            ):
                self.notify(f"Purchase succeeded after {self.get_time(start)}s")
                if self.amount_changed():
                    self.notify("Purchase amount changed!")
                    amount = self.get_new_amount()
                    self.press("esc")
                    return True, amount

                return True, None

            if self.amount_changed():
                    self.notify("Purchase amount changed!")
                    amount = self.get_new_amount()
                    self.press("esc")
                    return True, amount

            elif self.offer_sold_out():
                self.press("esc")
                return False, None

            elif self.inv_full():
                raise InventoryFullError

            elif self.out_of_money():
                raise OutOfMoneyError

            elif self.has_timedout(start, 0.6):
                print("Timedout, no success!")
                return False, None

            if self.check_for_captcha():
                return False, None

    def get_item_amount(self):
        """Gets the amount of items that can be bought"""
        self.check_status()
        self.notify("Checking item amount...")
        start = time()

        if pg.locateOnScreen(
            "images/11.png", region=(1108, 472, 25, 32), confidence=0.8
        ):
             self.amount = 11

        # get image showing the amount, process and pass to tesseract
        for region in [(1108, 472, 25, 32), (969, 514, 30, 24)]:

            result = Screen.read_quantity(region)
            # output ocr result
            if result:
                self.notify(f"Getting amount took {self.get_time(start)}s")
                self.amount = int(result)
                return

        self.amount = 1

    def validate_price(self, item: Item, price: int):
        """Takes an item and the price we think we bought it for and checks
        if that could be a valid price.
        """
        allowed_profit = 0.9
        profit_limit = int(item.price) * allowed_profit
        try:
            if (
                int(price) > int(item.buy_at)
                or (int(item.price) - int(price)) > profit_limit
            ):
                return item.buy_at
        except: pass
        return price

    def get_item_price(self, item: Item, img):
        """Processes the image of the item price and ocr's it"""
        self.price = None
        self.price = self.validate_price(item, Screen.read_price(img))

    def post_profit(self, item: Item, inventory: Inventory, amount):
        """Sends all previously bought items to discord, the thread is started
        after all items have been purchased to avoid slowdowns and errors.

        Parameters:
        -----------
        item: :class:`Item`
            The item that was being purchased

        purchases: :class:`List`
            The list of purchases containing image path and purchase quantity
        """
        discord = Discord()
        try:
            # get price from image, amount from data
            bought_for = self.price
            profit = (int(item.price) - int(bought_for)) * amount

            purchase = Purchase(
                item=item,
                bought_at=bought_for,
                amount=amount,
                profit=profit,
                image=item.name,
            )

            Thread(
                target=lambda: discord.send_purchase_embed(purchase, inventory)
            ).start()
            return purchase

        except Exception as e:
            print(f"Unhandled exception posting to discord!\n{e}")

    def get_new_amount(self):
        """Gets the new amount after a purchase errored"""
        new_amount = Screen.get_new_quantity()

        discord = Discord()
        discord.send_image("images/temp/amount.png", f"Determined as {new_amount}")
        return new_amount


class OutOfMoneyError(Exception):
    """Raised when out of money"""


class InventoryFullError(Exception):
    """Raised when the inventory is full unexpected"""

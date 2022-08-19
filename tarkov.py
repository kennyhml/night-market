from threading import Thread
from pyclick import humanclicker
import pyautogui as pg
import time
import logging as lg
import datetime
import psutil
import inspect
import os
import requests
from mss import mss, tools
import discord


class TarkovBot:
    """Main Tarkov bot handle
    ---------------------------
    Controls the bots workflow with class attributes such as:
    - running: `bool` - bot is active
    - paused: `bool` - bot is paused

    Owns main utility methods such as mouse movements, clicks,
    key presses, sleeps...

    Raises:
    --------
    - Terminated: `Exception` if the bot is no longer running.
    """

    version = "0.1.0"
    running = True
    paused = False

    def check_status(self) -> None:
        """Checks if the bot is terminated or paused"""
        if not self.running:
            raise BotTerminated

        while self.paused:
            time.sleep(0.1)

    def sleep(self, t):
        """Sleep wrapper to check for termination / paused"""
        self.check_status()
        time.sleep(t)

    def move_to(self, x=None, y=None) -> None:
        """Wrapper for humanclickers `move_to_point` method, scales passed
        coordinates by default and corrects them if they are in bad areas.
        Parameters
        -----------
        x, y: :class:`ints` | `tuple`
            The coordinates to move to, normalized by pyautogui
        """
        self.check_status()
        x, y = pg._normalizeXYArgs(x, y)

        pg.moveTo(x, y)
        return
        lg.info(f"Moving to {x, y}")
        humanclicker.move_to_point((x, y), duration=(0.05))

    @staticmethod
    def has_timedout(counter: float, max_time: int) -> bool:
        """Checks if a `time.time()` timer has elapsed"""
        return (time.time() - counter) > max_time

    def click(self, delay=0.3, button="left") -> None:
        """Clicks at the current mouse position"""
        self.check_status()
        lg.info(f"Clicking! Button: {button}; Delay: {delay}")

        # split the delay before and after the click
        self.sleep(delay / 2)
        pg.click(button=button)
        self.sleep(delay / 2)

    def press(self, key) -> None:
        """Presses a passed key"""
        self.check_status()
        lg.info(f"Pressing {key}")

        pg.press(key)

    def get_screenshot(self, path, region):
        x1, y1, x2, y2 = region
        
        with mss() as sct:
            region= {'top': y1, 'left': x1, 'width': x2, 'height': y2}
            # Grab the data
            img = sct.grab(region)

            # Save to the picture file
            tools.to_png(img.rgb, img.size, output=path)

    def game_running(self) -> bool:
        """Checks if tarkov is running"""
        for process in psutil.process_iter():
            if process.name() == "EscapeFromTarkov.exe":
                return True

    def notify(self, message: str, console=True, discord=False):
        """Prints, logs and posts a message"""
        caller = inspect.currentframe().f_back.f_code.co_name
        lg.info(f"{caller} informed: {message}")

        if console:
            print(message)

    def set_clipboard(str, text):
        """Puts the passed text into the clipboard to allow for pasting"""
        command = "echo | set /p nul=" + text.strip() + "| clip"
        os.system(command)

    @staticmethod
    def rect_to_center(rect):
        return (((rect[0] + (0.5 * rect[2])), round(rect[1] + (0.5 * rect[3]))))

    def overlaps(self, C1, C2, eps):
        return all(abs(c2 - c1) < eps for c2, c1 in zip(C2, C1))

    def filter_close_points(self, points: set) -> set:
        diff = 20
        filtered = set()

        while points:
            circle = points.pop()
            for other in points:
                if self.overlaps(circle, other, diff):
                    break
            else:
                filtered.add(circle)

        return filtered


class Discord:
    def __init__(self) -> None:
        self.url = "https://discord.com/api/webhooks/991429513340780626/Hm4wv4-7G9XJaBiIiAN28mU5d79mG9vSmdsj5luutodvRetwJdOD7Z_fFJzB1tg6W3_m"
        self.avatar = "https://lostarkcodex.com/icons/use_9_242.webp"

    def send_message(self, message):
        data = {
            "content": message,
            "avatar_url": self.url,
        }
        requests.post(self.url, data=data)

    def send_image(self, image, message):

        data = {
            "content": message,
            "avatar_url": self.url,
        }

        file = {"file": (image, open(image, "rb"))}
        Thread(
            target=lambda: requests.post(self.url, data=data, files=file),
            name="Posting to discord!",
        ).start()


    def send_purchase_embed(self, purchase):
        embed = discord.Embed(
            type="rich",
            title=f'Purchased {purchase.item.name}!',
            description=f'You just hit a lick on {purchase.item.name}',
            color=0x9807f2,
        )
        print(f"images/items/{purchase.image}.png")
        file = discord.File(f"images/items/{purchase.image}.png", filename="image.png")

        embed.set_thumbnail(url="attachment://image.png")
        embed.add_field(name="Bought for:ㅤㅤㅤ" ,value=purchase.bought_at)
        embed.add_field(name="Item value:ㅤㅤㅤ" ,value=purchase.item.price)
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name="Quantity:ㅤㅤㅤ" ,value=purchase.amount)
        embed.add_field(name="Profit made:ㅤㅤㅤ" ,value=purchase.profit)
        embed.add_field(name='\u200b', value='\u200b')

        embed.set_footer(
            text="Powered by night market"
        )
        webhook = discord.Webhook.from_url(
            self.url, adapter=discord.RequestsWebhookAdapter()
        )
        webhook.send(file=file, avatar_url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg", embed=embed) 

now = datetime.datetime.now()
now_str = now.strftime("%d-%m-%H-%M")
lg.basicConfig(
    level=lg.INFO,
    filename=f"logs\logs - {now_str}.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class BotTerminated(Exception):
    """Raised when the bot is terminated"""

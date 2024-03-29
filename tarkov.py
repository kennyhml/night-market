
from pyclick import humanclicker
import pyautogui as pg
import time
import logging as lg
import datetime
import psutil
import inspect
import os
from mss import mss, tools
import json
from pytesseract import pytesseract as tes
pg.FAILSAFE = False

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
    running = False
    paused = False

    def __init__(self):
        with open("data/data.json") as f:
            self.data = json.load(f)

        with open("data/settings.json") as f:
            self.config = json.load(f)
            tes.tesseract_cmd = self.config["tesseract_path"]

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

        if self.config["mouse_movement"] == "Warping":
            pg.moveTo(x, y)
            return

        humanclicker.move_to_point((x, y), duration=(0.05))

    def click(self, delay=0.3, button="left") -> None:
        """Clicks at the current mouse position"""
        self.check_status()
        lg.info(f"Clicking button: {button}; Delay: {delay}")

        # split the delay before and after the click
        self.sleep(delay / 2)
        pg.click(button=button)
        self.sleep(delay / 2)

    def press(self, key, delay=0) -> None:
        """Presses a passed key"""
        self.check_status()

        lg.info(f"Pressing {key}")
        self.sleep(delay / 2)
        pg.press(key)
        self.sleep(delay / 2)


    @staticmethod
    def sleep_start_delay():
        with open("data/settings.json") as f:
            data = json.load(f)
        print("Bot has been started!")
        time.sleep(data["start_delay"])

    @staticmethod
    def has_timedout(counter: float, max_time: int) -> bool:
        """Checks if a `time.time()` timer has elapsed"""
        return (time.time() - counter) > max_time

    @staticmethod
    def get_screenshot(path, region=(0, 0, 1920, 1080)):
        start = time.time()
        x, y, w, h = region
        x, y, w, h = int(x), int(y), int(w), int(h)

        with mss() as sct:
            region_dict = {'left': x, 'top': y, 'width': w, 'height': h}
            # Grab the data
            img = sct.grab(region_dict)

            # Save to the picture file
            tools.to_png(img.rgb, img.size, output=path.replace('"', ""))
        return path
        
    @staticmethod
    def game_running() -> bool:
        """Checks if tarkov is running"""
        for process in psutil.process_iter():
            if process.name() == "EscapeFromTarkov.exe":
                return True

    @staticmethod
    def set_clipboard(text):
        """Puts the passed text into the clipboard to allow for pasting"""
        command = "echo | set /p nul=" + text.strip() + "| clip"
        os.system(command)

    @staticmethod
    def get_time(timer):
        return round(time.time() - timer, 2)

    @staticmethod
    def rect_to_center(rect):
        return (((rect[0] + (0.5 * rect[2])), round(rect[1] + (0.5 * rect[3]))))

    @staticmethod
    def overlaps(C1, C2, eps):
        return all(abs(c2 - c1) < eps for c2, c1 in zip(C2, C1))

    @staticmethod
    def filter_close_points(points: set, diff=20) -> set:
        filtered = set()

        while points:
            circle = points.pop()
            for other in points:
                if TarkovBot.overlaps(circle, other, diff):
                    break
            else:
                filtered.add(circle)

        return filtered

    def notify(self, message: str, console=True, discord=False):
        """Prints, logs and posts a message"""
        caller = inspect.currentframe().f_back.f_code.co_name
        lg.info(f"{caller} - {message}")

        if console:
            print(message)

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

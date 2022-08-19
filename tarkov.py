
from pyclick import humanclicker
import pyautogui as pg
import time
import logging as lg
import datetime
import psutil
import inspect
import os
from mss import mss, tools


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
        caller = inspect.currentframe().f_back.f_code.co_name
        print(f"{caller} sleeps: {t}")
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

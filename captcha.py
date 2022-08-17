from curses import raw
import difflib
from unittest import TestCase
import pyautogui as pg
from tarkov import Discord, TarkovBot
from PIL import Image
import pytesseract as tes

tes.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class CaptchaSolver(TarkovBot):
    def __init__(self) -> None:
        super().__init__()
        self.discord = Discord()

    path = "images/captcha/"

    CAPTCHA_ITEMS = {
        "Golden neck chain": path + "golden_neck_chain.png",
        "Gas analyzer": path + "gas_analyzer.png",
        "Vaseline balm": path + "vaseline_balm.png",
        "Grizzly medical kit": path + "grizzly_medical_kit.png",
        "Can of Majaica coffee beans": path + "can_of_majaica_coffee_beans.png",
        "Expeditionary fuel tank": path + "expeditionary_fuel_tank.png",
        "AI-2 medkit": path + "AI-2_medkit.png",
        "Zibbo lighter": path + "zibbo_lighter.png",
        "WD-40 (100ml)": path + "WD-40_(100ml).png",
        "Can of beef stew (Large)": path + "can_of_beef_stew (Large).png",
        "Bronze lion": path + "bronze_lion.png",
        '"Fierce Hatchling" moonshine': path + "fierce_hatchling_moonshine.png",
        "Propane tank (5L)": path + "propane_tank (5L).png",
        "Alyonka chocolate bar": path + "alyonka_chocolate_bar.png",
        "Bolts": path + "bolts.png",
        "Analgin painkillers": path + "analgin_painkillers.png",
        "Salewa first aid kit": path + "salewa_first_aid_kit.png"
    }

    def get_captcha_target(self):

        # set configs

        allowed_characters = (
            " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()-"
        )

        config = "--oem 3 --psm 6 -c tessedit_char_whitelist=" + allowed_characters
        path = "images/temp/captcha.png"

        # upscale the image for better matches
        pg.screenshot(path, region=(620, 63, 680, 980))
        img = Image.open(path)
        w, h = img.size
        img = img.resize((w * 2, h * 2), 1)
        img.save(path)

        # read the image and filter the returned text
        raw_text: str = tes.image_to_string(path, config=config)
        item_to_find = self.filter_captcha_target(raw_text)
        self.discord.send_message(f"Captcha target: {item_to_find}")
        image = self.compare_target_to_database(item_to_find)
        self.find_all_occurrences(image)

    def compare_target_to_database(self, target):
        """Tries to determine the item and returns the image"""
        for known_item in self.CAPTCHA_ITEMS:

            if target == known_item:
                self.discord.send_message("This item is known and can be solved!")
                return self.CAPTCHA_ITEMS[target]  # return image

        else:
            self.discord.send_message(
                "Item could not be determined! Looking for close matches..."
            )
            words = list(self.CAPTCHA_ITEMS)
            closest_match = difflib.get_close_matches(target, words, n=1, cutoff=0.3)[0]
            if closest_match:
                self.discord.send_message(f"Found match as: {closest_match}!")
                return self.CAPTCHA_ITEMS[closest_match]

            else:
                self.discord.send_message(
                    "CRITICAL! Item could not be determined whatsoever!!"
                )

    def filter_captcha_target(self, raw_text: str):

        bot = raw_text.find("bot")
        if bot != -1:
            raw_text = raw_text[bot + 3 :]

        text = raw_text.split("\n")
        filtered_text = [string for string in text if len(string) > 3]

        for i, split in enumerate(filtered_text):
            if "all:" in split:
                return filtered_text[i + 1]

    def find_all_occurrences(self, image):

        occurrences = list(
            pg.locateAllOnScreen(image, region=(590, 48, 739, 992), confidence=0.8)
        )

        item_centers = [
            (
                round(item[0] + (0.5 * item[2])),
                round(item[1] + (0.5 * item[3])),
            )
            for item in occurrences
        ]

        filtered_centers = self.filter_close_points(set(item_centers))
        self.check_all_items(filtered_centers)

    def check_all_items(self, positions):
        for position in positions:
            self.move_to(position)
            self.click(0.8)

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


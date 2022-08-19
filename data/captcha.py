import difflib
from time import time
import pyautogui as pg
from screen import mask
from tarkov import TarkovBot
from nightmart_bot import Discord
from PIL import Image
import pytesseract as tes
import cv2 as cv

tes.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
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
    "WD-40 (100ml)": path + "WD-40 (100ml).png",
    "Can of beef stew (Large)": path + "can_of_beef_stew (Large).png",
    "Bronze lion": path + "bronze_lion.png",
    '"Fierce Hatchling" moonshine': path + "fierce_hatchling_moonshine.png",
    "Propane tank (5L)": path + "propane_tank (5L).png",
    "Alyonka chocolate bar": path + "alyonka_chocolate_bar.png",
    "Bolts": path + "bolts.png",
    "Analgin painkillers": path + "analgin_painkillers.png",
    "Salewa first aid kit": path + "salewa_first_aid_kit.png",
    "Horse figurine": path + "horse_figurine.png",
    "Car battery": path + "car_battery.png",
    "Strike cigarettes": path + "strike_cigarettes.png",
    "42 Signature Blend English Tea": path + "42_signature_blend_english_tea.png",
    "Bottle of water (0.6L)": path + "bottle_of_water (0.6L).png",
    "Immobilzing splint": path + "immobilzing_splint.png",
    "Printer paper": path + "printer_paper.png",
    "Red Rebel ice pick": path + "red_rebel_ice_pick.png",
    "Antique Teapot": path + "antique_teapot.png",
    "Freeman crowbar": path + "freeman_crowbar.png",
    "Golen rooster": path + "golden_rooster.png",
    'Gunpoweder "Eagle"': path + "gunpoweder_eagle.png",
    "Morphine injector": path + "morphine_injector.png",
    "Electric drill": path + "electric_drill.png",
    "Pliers": path + "pliers.png",
    "Insulating tape": path + "insulating_tape.png",
    "Broken GPhone X smartphone": path + "broken_gphone_x_smartphone.png",
    "Golden Star balm": path + "golden_star_balm.png",
    "Toilet paper": path + "toilet_paper.png",
    "T-Shaped plug": path + "t-shaped_plug.png",
    "Pack of sodium bicarbonate": path + "pack_of_sodium_bicarbonate.png",
    "Can of hot rod energy": path + "can_of_hot_rod_energy_drink.png",
    "Spark plug": path + "spark_plug.png",
    "Screwdriver": path + "screwdriver.png",
    "Pack of sugar": path + "pack_of_sugar.png",
    "Aseptic bandage": path + "aseptic_bandage.png",
    "Graphics card": path + "graphics_card.png",
    "Wrench": path + "wrench.png",
    "Xenomorph sealing foam": path + "xenomorph_sealing_foam.png",
    "Can of condensed milk": path + "can_of_condensed_milk.png",
    "": path + ".png",
    "": path + ".png",
    "": path + ".png",
    "": path + ".png",
    "": path + ".png",
    "": path + ".png",
    "": path + ".png",
    "": path + ".png",
    "": path + ".png",
}


class CaptchaSolver(TarkovBot):
    def __init__(self) -> None:
        super().__init__()
        self.discord = Discord()

    def solve(self):
        """Solves the captcha"""
        start = time()

        # process the captcha and get the desired item
        target_item = self.get_captcha_target()
        self.discord.send_message(f"Captcha target item: {target_item}")

        # check if the item is in our database, get the image
        image = self.compare_target_to_database(target_item)

        # convert all occurrences into points, tick them all
        filtered_points = self.find_all_occurrences(image)
        self.check_all_items(filtered_points)
        self.discord.send_message(f"Captcha took {round(time() - start, 2)}s to solve.")
        self.confirm()

    def get_captcha_target(self):
        """Processes the image of the captcha and returns the filtered item"""
        # set configs
        allowed_characters = (
            " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()-"
        )
        config = "--oem 3 --psm 6 -c tessedit_char_whitelist=" + allowed_characters
        path = "images/temp/captcha.png"

        # upscale the image for better matches
        self.get_screenshot(path, region=(620, 63, 680, 980))
        self.discord.send_image(path, "A captcha has appeared:")

        # mask the image, upscale it a little
        img = mask(path)
        cv.imwrite(path, img)
        img = Image.open(path)
        w, h = img.size
        img = img.resize((w * 3, h * 3), 1)
        img.save(path)

        # read the image and filter the returned text
        raw_text: str = tes.image_to_string(path, config=config)
        return self.filter_captcha_target(raw_text)

    def compare_target_to_database(self, target):
        """Tries to determine the item and returns the image"""
        self.check_status()
        self.notify("Searching for items image in database...")

        # find the image in our data
        for known_item in CAPTCHA_ITEMS:
            if target == known_item:
                self.discord.send_message("This item is known and can be solved!")
                return CAPTCHA_ITEMS[target]  # return image

        self.discord.send_message(
            "Item could not be determined! Looking for closest match..."
        )

        closest_match = difflib.get_close_matches(
            target, list(CAPTCHA_ITEMS), n=1, cutoff=0.5
        )

        if closest_match:
            self.discord.send_message(f"Found match as: {closest_match}!")
            return CAPTCHA_ITEMS[closest_match[0]]

        self.discord.send_message("CRITICAL! Item could not be determined whatsoever!")

    def filter_captcha_target(self, raw_text: str):
        """Takes the text from the intial scan and filters it to find the target
        item, this is achieved by slicing it with the "bot" just before the item is
        given and then splitting it by new lines alongside filtering out short words.
        """
        # get the index of the "bot" part in the text and slice it from there
        bot = raw_text.find("bot")

        # .find() returns -1 if the word wasnt found
        if bot != -1:
            raw_text = raw_text[bot + 3 :]

        # split the remaining text by newlines
        text = raw_text.split("\n")
        filtered_text = [string for string in text if len(string) > 3]

        # check lines left in the text, find line containing "all:"
        for i, split in enumerate(filtered_text):
            if "all:" in split or "alk:" in split:
                # "all:" occurred > the next index is the word
                return filtered_text[i + 1]

    def find_all_occurrences(self, image):
        """Find all occurences of the item within the captcha"""
        self.check_status()
        self.notify("Checking for occurrences...")

        # get a list of all matches, note that this function will match the same image
        # muliple times on the same location!
        occurrences = list(
            pg.locateAllOnScreen(image, region=(590, 48, 739, 992), confidence=0.85)
        )

        # convert the matched boxes into their center coordinates, this makes it easier to
        # filter out points that are close to each other and click them in the end
        item_centers = [self.rect_to_center(item) for item in occurrences]

        # returns the list of filtered points
        return self.filter_close_points(set(item_centers))

    def check_all_items(self, positions):
        """Check all the items"""
        self.check_status()
        self.notify("Ticking all points...")
        self.notify(f"Checking {len(positions)} items...")

        for position in positions:
            self.move_to(position)
            self.click(0.2)

    def confirm(self):
        """Confirm the captcha"""
        self.check_status()
        self.notify("Confirming captcha...")

        # find the confirm button, remember we dont know the size of the captcha
        confirm = pg.locateCenterOnScreen(
            "images/captcha_confirm.png", region=(590, 48, 739, 992), confidence=0.7
        )

        # hope that the button was found, click it
        if confirm:
            self.move_to(confirm)
            self.click(0.3)
            while pg.locateOnScreen(
                "Images/captcha.png", region=(577, 45, 775, 1007), confidence=0.7, grayscale=True
            ):
                pass

            return

        # now we are in trouble
        self.discord.send_message(
            "WARNING! Could not locate the confirmation button!!!"
        )


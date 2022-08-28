import difflib
from time import time
import pyautogui as pg
from screen import Screen
from tarkov import TarkovBot
from nightmart_bot import Discord

path = "images/captcha/"

# captcha names as tesseract gets them and the corresponding image
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
    "Strike Cigarettes": path + "strike_cigarettes.png",
    "42 Signature Blend English Tea": path + "42_signature_blend_english_tea.png",
    "Bottle of water (0.6L)": path + "bottle_of_water (0.6L).png",
    "Immobilizing splint": path + "immobilizing_splint.png",
    "Printer paper": path + "printer_paper.png",
    "Red Rebel ice pick": path + "red_rebel_ice_pick.png",
    "Antique teapot": path + "antique_teapot.png",
    "Freeman crowbar": path + "freeman_crowbar.png",
    "Golden rooster": path + "golden_rooster.png",
    'Gunpowder "Eagle"': path + "gunpoweder_eagle.png",
    "Morphine injector": path + "morphine_injector.png",
    "Electric drill": path + "electric_drill.png",
    "Pliers": path + "pliers.png",
    "Insulating tape": path + "insulating_tape.png",
    "Broken GPhone X smartphone": path + "broken_gphone_x_smartphone.png",
    "Golden Star balm": path + "golden_star_balm.png",
    "Toilet paper": path + "toilet_paper.png",
    "T-Shaped plug": path + "t-shaped_plug.png",
    "Pack of sodium bicarbonate": path + "pack_of_sodium_bicarbonate.png",
    "Can of Hot Rod energy drink": path + "can_of_hot_rod_energy_drink.png",
    "Spark plug": path + "spark_plug.png",
    "Screwdriver": path + "screwdriver.png",
    "Pack of sugar": path + "pack_of_sugar.png",
    "Aseptic bandage": path + "aseptic_bandage.png",
    "Graphics card": path + "graphics_card.png",
    "Wrench": path + "wrench.png",
    "Xenomorph sealing foam": path + "xenomorph_sealing_foam.png",
    "Can of condensed milk": path + "can_of_condensed_milk.png",
}


class CaptchaSolver(TarkovBot):
    """Captcha handler for purchase attempts
    --------------------------
    Solves captcha popups by OCR'ing the target items name and
    comparing it to a database of known items.

    Uses pyautogui's locateAllOnScreen and some processing to
    tick all the items.
    """

    def __init__(self) -> None:
        super().__init__()
        self.discord = Discord()

    def solve(self):
        """Solves a captcha currently on the screen"""
        start = time()

        # process the captcha and get the desired item
        image_region, item_region = self.get_captcha_boundaries()
        target_item = self.get_captcha_target()
        self.discord.send_message(f"Captcha target item: {target_item}")

        # check if the item is in our database, get the image
        image = self.compare_target_to_database(target_item)

        # convert all occurrences into points, tick them all
        filtered_points = self.find_all_occurrences(image, image_region)
        self.check_all_items(filtered_points)

        # wait for the green blinking and escape to close the captcha instantly
        if self.confirm():
            while not Screen.captcha_succeeded(item_region):
                self.sleep(0.1)
            self.press("esc")
            self.discord.send_message(f"Captcha took {self.get_time(start)}s to solve!")
            return

        # captcha failed, try again
        self.press("esc")
        self.sleep(5)
        self.solve()

    def get_captcha_boundaries(self):
        """Gets the captcha boundaries by locating the "SECURITY CHECK"
        position and the exit button, constructing the item frame from
        the coordinates, then using the distance to the confirm buttons
        y-level to crop out the item region.

        Returns:
        ---------
        image region: :class:`tuple`
            The region of the images that need to be analyzed

        target region: :class:`tuple`
            The region of the target item to process and determine
        """
        # region where the captcha could possibly be
        captcha_region = (577, 45, 775, 1007)
        self.notify("Getting captcha boundaries...")

        # find top left and top right on the captcha prompt
        security_check = pg.locateOnScreen(
            "images/captcha.png", region=captcha_region, confidence=0.7
        )
        exit_button = pg.locateOnScreen(
            "images/purchase_prompt.png", region=captcha_region, confidence=0.7
        )

        try:
            # calculate the boundaries needed
            top_left = security_check[0] - 50, security_check[1]
            top_right = exit_button[0] + exit_button[2], exit_button[1]

            # screenshot the calculated boundaries
            self.get_screenshot(
                "images/temp/captcha_target.png",
                region=(*top_left, top_right[0] - top_left[0], 110),
            )

            # get the upper y axis of confirm button to end the images crop region
            end_y_axis = pg.locateOnScreen(
                "images/captcha_confirm.png", region=captcha_region, confidence=0.7
            )[1]

            # return calculated boundaries of the target and item region
            return (
                (
                    top_left[0],
                    top_left[1] + 105,
                    top_right[0] - top_left[0],
                    end_y_axis - top_right[1] - 105,
                ),
                (*top_left, top_right[0] - top_left[0], 110),
            )

        except Exception as e:
            self.notify(f"Critical exception calculating captcha boundaries!\n{e}")

    def get_captcha_target(self):
        """Processes the image of the captcha and returns the filtered item"""
        self.check_status()
        self.notify("Determining captcha target...")

        raw_text = Screen.read_captcha()
        return self.filter_captcha_target(raw_text)

    def compare_target_to_database(self, target):
        """Tries to determine the item and returns the image"""
        self.check_status()
        self.notify("Searching for items image in database...")

        # try to return the image directly
        try:
            return CAPTCHA_ITEMS[target]

        # target wasnt recognized perfectly
        except KeyError:
            pass

        # get the closest matching item name
        self.discord.send_message("Item not be determined! Checking closest match...")
        closest_match = difflib.get_close_matches(
            target, list(CAPTCHA_ITEMS), n=1, cutoff=0.5
        )
        # return the image of the closest matching item name
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

    def find_all_occurrences(self, image, region):
        """Find all occurences of the item within the captcha"""
        self.check_status()
        self.notify("Checking for occurrences...")

        # get a list of all matches, note that this function will match the same image
        # muliple times on the same location!
        occurrences = list(pg.locateAllOnScreen(image, region=region, confidence=0.85))

        # convert the matched boxes into their center coordinates, this makes it easier to
        # filter out points that are close to each other and click them in the end
        item_centers = [self.rect_to_center(item) for item in occurrences]

        # returns the list of filtered points
        return self.filter_close_points(set(item_centers))

    def check_all_items(self, positions):
        """Check all the items in order"""
        self.notify("Ticking all points...")

        for position in positions:
            self.move_to(position)
            self.click(0.3)

    def confirm(self):
        """Confirm the captcha"""
        self.notify("Confirming captcha...")

        # find the confirm button
        confirm = pg.locateCenterOnScreen(
            "images/captcha_confirm.png", region=(590, 48, 739, 992), confidence=0.7
        )

        # check that the button was found, click it
        if confirm:
            self.move_to(confirm)
            self.click(0.3)
            return True

        # trouble
        self.discord.send_message("WARNING! Could not locate the confirmation button!")

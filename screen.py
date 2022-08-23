from statistics import variance
import numpy as np
import cv2 as cv
from mss import mss
from PIL import Image
import pytesseract as tes
import pyautogui as pg
from nightmart_bot import Discord

from tarkov import TarkovBot


monitor_dict = {"top": 0, "left": 0, "width": 1920, "height": 1080}
sct = mss()

class Screen(TarkovBot):
    """Screen class for any sort of more complex detection"""

    @staticmethod
    def get_screen():
        """Grabs a screenshot of the current screen"""
        return np.array(sct.grab(monitor_dict), dtype=np.uint8)

    @staticmethod
    def process_region(x1, y1, x2, y2):
        """Scales a region to screen and converts it into numpy slices"""
        return (y1, y1 + y2, x1, x1 + x2)

    @staticmethod
    def get_cropped_screen(y1, y2, x1, x2):
        return Screen.get_screen()[y1:y2, x1:x2]

    @staticmethod
    def mask(img, rgb=(168, 166, 151), variance=50):
        """Maks an image given the RGB and variance
        Parameters:
        -----------
        img: `str`
            The path of the image to be masked

        rgb: `tuple`
            The rgb to mask in the image

        variance: `int`
            The variance for the rgb to mask

        Returns:
        -----------
        Image: `Mat`
            The masked image
        """

        if isinstance(img, str):
            img = cv.imread(img, 1)
            img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

        # set color range (filering the color of the chars here)
        lower_bound = (
            max(0, rgb[0] - variance),
            max(0, rgb[1] - variance),
            max(0, rgb[2] - variance),
        )
        upper_bound = (
            min(255, rgb[0] + variance),
            min(255, rgb[1] + variance),
            min(255, rgb[2] + variance),
        )

        return cv.inRange(img, lower_bound, upper_bound)

    @staticmethod
    def inv_replace_zeros(image):
        """Finds all slashed 0s in the price and replaces them with normal 0"""
        zero = cv.imread("images/0_2.png", 1)
        img = cv.imread(image, 1)

        results = set(pg.locateAll(zero, img, confidence=0.7))

        zeros = TarkovBot.filter_close_points(results)
        canvas = Image.open(image)
        zero = Image.open("images/better_0_2.png")

        for spot in zeros:
            canvas.paste(zero, (spot[0], spot[1]))

        canvas.save(image)

    @staticmethod
    def replace_zeros(image):
        """Finds all slashed 0s in the price and replaces them with normal 0"""
        zero = cv.imread("images/0.png", 1)
        zeros = TarkovBot.filter_close_points(
            set(pg.locateAll(zero, image, confidence=0.8)), diff=5
        )

        canvas = Image.open(image)
        zero = Image.open("images/better_0.png")

        for spot in zeros:
            canvas.paste(zero, (spot[0], spot[1]))

        canvas.save(image)


    def crop_inventory_money():
        path = "images/temp/money.png"

        rouble = pg.locate("images/rubel_2.png", path, confidence=0.8)
        euro = pg.locate("images/euro.png", path, confidence=0.8)

        left_bound = rouble[0] + rouble[2] + 3
        right_bound = euro[0] - 15

        img = Image.open(path)
        _, h = img.size
        img = img.crop((left_bound, 0, right_bound, h))

        img.save(path)


    @staticmethod
    def remove_rubel_right(image_path):
        """Replaces zeros, removes the rubel, and masks the image"""
        Screen.replace_zeros(image_path)

        slot = cv.imread(image_path, 1)
        template = cv.imread("images/rubel.png", 1)

        w, h = template.shape[:-1]
        res = cv.matchTemplate(slot, template, cv.TM_CCORR_NORMED)
        _, _, _, max_loc = cv.minMaxLoc(res)
        top_left = max_loc

        right = (1335 + 169, 157 + 32)
        length = right[0] - (1335 + top_left[0] - 5)

        masked = Screen.mask(cv.cvtColor(slot, cv.COLOR_RGB2BGR), rgb=(199, 197, 175), variance=30)

        # apply mask, save image
        cv.imwrite(image_path, masked)

        # crop the image
        res = Image.open(image_path)

        w, h = res.size
        res = res.crop((0, 0, w - length, h))
        res = res.resize((res.size[0] * 10, res.size[1] * 10), 1)
        res.save(image_path)

    @staticmethod
    def process_tess_image(path):
        """Prepares the image for tesseract to evaluate"""

        # removes the ruble and crops the image
        Screen.remove_rubel_right(path)

        # replace all 0s with x
        img = cv.imread(path, 0)

        # Taking a matrix of size 5 as the kernel
        kernel = np.ones((5, 5), np.uint8)
        return cv.dilate(img, kernel, iterations=1)

    @staticmethod
    def get_new_quantity():

        path = "images/temp/amount.png"

        # screenshot the prompt, process and ocr the image
        Screen.get_screenshot("images/temp/amount.png", region=(1005, 522, 81, 20))
        img = Image.open("images/temp/amount.png")
        w, h = img.size
        img = img.resize((w * 6, h * 6), 1)
        img.save(path)

        # get the new amount
        text: str = tes.image_to_string(
            Screen.mask(path),
            config="-c tessedit_char_whitelist=1234567890 --psm 10 -l eng",
        ).strip()

        return "".join(char for char in [c for c in text if c.isdigit()])

    @staticmethod
    def read_price(img):

        img = Screen.process_tess_image(img)
        cv.imwrite("images/temp/sample.png", img)

        # process passed image and ocr it, remove blankspaces
        return tes.image_to_string(
            img, config="-c tessedit_char_whitelist=1234567890 --psm 8 -l eng"
        ).strip()

    @staticmethod
    def replace_ones(image):
        """Finds all slashed 0s in the price and replaces them with normal 0"""
        one = cv.imread("images/1.png", 1)
        ones = TarkovBot.filter_close_points(
            set(pg.locateAll(one, image, confidence=0.9)), diff=2
        )
        canvas = Image.open(image)
        one = Image.open("images/better_1.png")

        for spot in ones:
            canvas.paste(one, (spot[0], spot[1]))

        canvas.save(image)

    @staticmethod
    def read_quantity(region):
        path = "Images/temp/item_amount.png"

        Screen.get_screenshot(path, region=region)
        Screen.replace_ones(path)

        processed = Screen.mask(path)
        cv.imwrite(path, processed)
        img = Image.open(path)
        w, h = img.size
        img = img.resize((w * 13, h * 13), 1)
        img.save(path)

        return (
            tes.image_to_string(
                processed,
                config="-c tessedit_char_whitelist=0123456789ilTa --psm 6 --oem 3 -l eng",
            )
            .strip()  # remove blankspaces
            .replace("(", "")
            .replace(")", "")
            .replace("t", "1")
            .replace("Ta", "17")
            .replace("i", "6")
        )

    @staticmethod
    def read_captcha():
        # set configs
        allowed_characters = (
            " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()-"
        )
        config = "--oem 3 --psm 6 -c tessedit_char_whitelist=" + allowed_characters
        path = "images/temp/captcha.png"

        # upscale the image for better matches
        Screen.get_screenshot(path, region=(620, 63, 680, 980))
        discord = Discord()
        discord.send_image(path, "A captcha has appeared:")

        # mask the image, upscale it a little
        img = Screen.mask(path)
        cv.imwrite(path, img)
        img = Image.open(path)
        w, h = img.size
        img = img.resize((w * 3, h * 3), 1)
        img.save(path)

        return tes.image_to_string(path, config=config)

    @staticmethod
    def read_current_money():

        path = "images/temp/money.png"
        Screen.get_screenshot(path, region=(1471, 173, 366, 24))
        Screen.crop_inventory_money()

        Screen.inv_replace_zeros(path)

        res = Image.open(path)
        w, h = res.size
        res = res.resize((w * 3, h * 3), 1)
        res.save(path)

        img = Screen.mask(path, (203, 200, 181))
        cv.imwrite(path, img)
        
        res = tes.image_to_string(
            img, config="-c tessedit_char_whitelist=1234567890 --psm 8 -l eng"
        )

        return int(res)

    @staticmethod
    def icon_loaded():

        path = "images/temp/item_icon.png"
        Screen.get_screenshot(path, (61, 144, 41, 37))
        img = cv.imread(path, 1)

        image = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        rgb=(205,204,194)
        variance=20

        lower_bound = (
            max(0, rgb[0] - variance),
            max(0, rgb[1] - variance),
            max(0, rgb[2] - variance),
        )
        upper_bound = (
            min(255, rgb[0] + variance),
            min(255, rgb[1] + variance),
            min(255, rgb[2] + variance),
        )

        # image, lower_bound, upper_bound. CARE THEY ARE IN BGR
        mask = cv.inRange(image, lower_bound, upper_bound)
        matches = cv.findNonZero(mask)

        if matches is None:
            return

        return len(matches) > 3
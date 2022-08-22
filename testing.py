from threading import Thread
from time import sleep, time
from tracemalloc import Statistic
from data.captcha import CaptchaSolver
from data.statistics import Statistics
from market.market import MarketUI
from market.purchase import Purchase, PurchaseHandler
import screen
import pytesseract as tess
import cv2 as cv
from PIL import Image, ImageEnhance
import pyautogui as pg

from tarkov import TarkovBot

from screen import Screen

{
    "Toilet paper": {
        "total_quantity": 106,
        "average_profit": 721,
        "total_profit": 76377,
    },
    "OFZ 30x160mm shell": {
        "total_quantity": 17,
        "average_profit": 2355,
        "total_profit": 40035,
    },
    "Old firesteel": {
        "total_quantity": 54,
        "average_profit": 2043,
        "total_profit": 110346,
    },
    "Golden egg": {"total_quantity": 28, "average_profit": 3413, "total_profit": 95571},
    "Can of Dr. Lupo's coffee beans": {
        "total_quantity": 38,
        "average_profit": 1684,
        "total_profit": 63983,
    },
    "Golden rooster": {
        "total_quantity": 33,
        "average_profit": 1304,
        "total_profit": 43041,
    },
}


a = PurchaseHandler()
a.running = True
a.get_item_amount()


"""
NORMAL DETECTION SAME SCALE

img = Image.open("images/items/Can of Dr. Lupo's coffee beans.png")
w, h = img.size

img = img.crop((0, 15, w, h - 10))
items = list(pg.locateAllOnScreen(img, confidence=0.7))

for item in items:
    pg.moveTo(item)
    sleep(0.5)
"""

"""
img = Image.open("images/items/OFZ 30x160mm shell.png")

img = img.resize((64, 164))
w, h = img.size

img = img.crop((0, 25, w, h - 10))

items = Screen.filter_close_points(set(pg.locateAllOnScreen(img, confidence=0.55, region=(1235, 283, 664, 789))), diff=10)

for item in items:
    pg.moveTo(Screen.rect_to_center(item))
    sleep(0.5)
"""

quit()

a = PurchaseHandler()
while 1:
    print(a.is_available((1678, 143, 192, 73)))

pg.screenshot("nigga.png", region=(620, 63, 680, 980))

img = Image.open("nigga.png")

w, h = img.size
img = img.resize((w * 2, h * 2), 1)
img.save("nigga.png")
txt = tes.image_to_string("nigga.png")

print(txt)

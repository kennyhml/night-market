

from threading import Thread
from time import sleep, time
from tracemalloc import Statistic
from data.captcha import CaptchaSolver
from data.statistics import Statistics
from market.market import MarketUI
from market.purchase import PurchaseHandler
import screen
import pytesseract as tess
import cv2 as cv
from PIL import Image
import pyautogui  as pg

from tarkov import TarkovBot

from screen import Screen

Screen.process_tess_image("images/temp/test.png")


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

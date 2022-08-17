import cv2 as cv 
import pytesseract as tes
from PIL import Image
import pyautogui as pg
import json
import mss
from market import MarketUI

sct = mss.mss()


custom_config = "--oem 3 --psm 6"
a = MarketUI()
while 1:
    print(a.purchase_errored())

pg.screenshot("nigga.png", region=(620, 63, 680, 980))

img = Image.open("nigga.png")

w, h = img.size
img = img.resize((w * 2, h * 2), 1)
img.save("nigga.png")
txt = tes.image_to_string("nigga.png")

print(txt)
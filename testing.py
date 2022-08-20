

from tracemalloc import Statistic
from data.statistics import Statistics
from market.market import MarketUI
from market.purchase import PurchaseHandler
import screen
import pytesseract as tess
import cv2 as cv
from PIL import Image
import pyautogui  as pg

a = PurchaseHandler()
a.await_prompt()

quit()

from nightmart_bot import Discord

a = Discord()
a.send_statistics(aa, sum([aa[item]["total_profit"] for item in aa]))

quit()




pg.screenshot("nigga.png", region=(620, 63, 680, 980))

img = Image.open("nigga.png")

w, h = img.size
img = img.resize((w * 2, h * 2), 1)
img.save("nigga.png")
txt = tes.image_to_string("nigga.png")

print(txt)

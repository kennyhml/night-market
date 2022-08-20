
from time import sleep, time
import numpy as np
import cv2 as cv
from mss import mss
from PIL import Image
import pytesseract as tess
import pyautogui as pg

monitor_dict = {"top": 0, "left": 0, "width": 1920, "height": 1080}

sct = mss()


def get_screen():
    """Grabs a screenshot of the current screen"""
    return np.array(sct.grab(monitor_dict), dtype=np.uint8)


def process_region(x1, y1, x2, y2):
    """Scales a region to screen and converts it into numpy slices"""
    return (y1, y1 + y2, x1, x1 + x2)


def get_cropped_screen(y1, y2, x1, x2):
    return get_screen()[y1:y2, x1:x2]


def overlaps(C1, C2, eps):
    return all(abs(c2 - c1) < eps for c2, c1 in zip(C2, C1))


def filter_close_points(points: set) -> set:

    diff = 5
    filtered = set()

    while points:
        circle = points.pop()
        for other in points:
            if overlaps(circle, other, diff):
                break
        else:
            filtered.add(circle)

    return filtered

def mask(img, rgb=(168,166,151)):

    variance = 50

    img = cv.imread(img, cv.COLOR_RGB2BGR)
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

    # image, lower_bound, upper_bound. CARE THEY ARE IN BGR
    return cv.inRange(img, lower_bound, upper_bound)
    # apply mask, save image
    

def inv_replace_zeros(image):
    """Finds all slashed 0s in the price and replaces them with normal 0"""
    zero = cv.imread("images/0_2.png", 1)
    img = cv.imread(image, 1)

    results = set(pg.locateAll(zero, img, confidence=0.7))

    zeros = filter_close_points(results)
    canvas = Image.open(image)
    zero = Image.open("images/better_0_2.png")

    for spot in zeros:
        canvas.paste(zero, (spot[0], spot[1]))

    canvas.save(image)


def replace_zeros(image):
    """Finds all slashed 0s in the price and replaces them with normal 0"""
    zero = cv.imread("images/0.png", 1)
    zeros = filter_close_points(set(pg.locateAll(zero, image, confidence=0.8)))
    canvas = Image.open(image)
    zero = Image.open("images/better_0.png")

    for spot in zeros:
        canvas.paste(zero, (spot[0], spot[1]))

    canvas.save(image)


def remove_rubel(image_path):
    """Replaces zeros, removes the rubel, and masks the image"""
    replace_zeros(image_path)

    slot = cv.imread(image_path, 1)
    template = cv.imread("images/rubel.png", 1)

    w, h = template.shape[:-1]
    res = cv.matchTemplate(slot, template, cv.TM_CCORR_NORMED)
    _, _, _, max_loc = cv.minMaxLoc(res)
    top_left = max_loc

    right = (1335 + 169, 157 + 32)
    length = right[0] - (1335 + top_left[0] - 5)
    rgb = (199, 197, 175)
    variance = 30

    slot = cv.cvtColor(slot, cv.COLOR_RGB2BGR)
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

    # image, lower_bound, upper_bound. CARE THEY ARE IN BGR
    mask = cv.inRange(slot, lower_bound, upper_bound)
    # apply mask, save image
    cv.imwrite(image_path, mask)

    # crop the image
    res = Image.open(image_path)
    w, h = res.size
    res = res.crop((0, 0, w - length, h))
    res = res.resize((res.size[0] * 10, res.size[1] * 10), 1)
    res.save(image_path)


def process_tess_image(path):
    """Prepares the image for tesseract to evaluate"""
    start = time()
    # removes the ruble and crops the image
    remove_rubel(path)

    # replace all 0s with x
    img = cv.imread(path, 0)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
    return cv.dilate(img, kernel, iterations=1)


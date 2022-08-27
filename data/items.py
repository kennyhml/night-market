from dataclasses import dataclass
import json
import glob
from screen import Screen
from PIL import Image
from tarkov import TarkovBot
import pyautogui as pg

@dataclass
class Item:
    name: str
    price: float
    buy_at: int
    currency: str
    vendor: str
    refreshes: int
    size: int


@dataclass
class Inventory(TarkovBot):
    """Inventory class containing slots to empty, amount of slots at
    which to empty and amount of slots currently taken, alongside methods
    to request the state
    """
    def __init__(self):
        super().__init__()
        self.total_slots = self.config["allowed_inv_slots"]
        self.max_slots = self.config["empty_inv_at"]
        self.slots_taken = 0

    def is_full(self) -> bool:
        """Checks if the inventory is full"""
        return self.slots_taken > self.max_slots

    def reset(self) -> None:
        """Resets the taken slots"""
        self.slots_taken = 0

    def add_items(self, amount, size):
        self.slots_taken += amount * int(size)

class Database(TarkovBot):
    def __init__(self) -> None:
        self.load_items()
        self.images = glob.glob("images/*.png")

    def load_config(self):
        with open("data/data.json") as f:
            self.item_data = json.load(f)

    def load_images(self):
        self.images = glob.glob("images/items/*.png")

    def has_image(self, target):
        self.load_images()
        images = [
            image.removeprefix("images/items\\").removesuffix(".png")
            for image in self.images
        ]
        return target.name in images

    def add_image(self, item: Item):
        path = item.name.replace('"', "")
        self.get_screenshot(f"images/items/{path}.png", region=(879, 147, 64, 64))
        img = Image.open(f"images/items/{path}.png")
        bottom_corner = img.crop((60, 48, 61, 49))
        for x in range(53, 63):
            for y in range(51, 63):
                img.paste(bottom_corner, (x, y, x + 1, y + 1))
        img.save(f"images/items/{path}.png")

    def slot_is_empty(self, slot) -> bool:
        return pg.locateOnScreen("images/empty.png", region=slot, confidence=0.7)

    @staticmethod
    def load_inventory_image(item):
        directory = "images/inv"
        all_items = [
            image.removeprefix("images/inv\\").removesuffix(".png")
            for image in glob.glob("images/inv/*.png")
        ]
        img = item.replace('"', "")

        if img in all_items:
            return directory + "/" + img
        return "No image, please take one!"

    def add_inventory_image(self, item):
        item_size = self.item_data[item]["size"].split("x")
        path = item.replace('"', "")
        size = int(item_size[0]) * 64, int(item_size[1]) * 64
        Screen.get_screenshot(f"images/inv/{path}.png", region=(1270, 260, *size))

    def get_items_to_purchase(self):
        return [
            self.data_to_item(item)
            for item in self.get_items()
            if self.item_data[item]["enabled"]
        ]
        
    def load_items(self):
        self.load_config()

    def get_items(self):
        return self.item_data

    def items_sold_at(self, vendor):
        return [item for item in self.item_data if item["trader"] == vendor]

    def get_size(self, size):
        size = size.split("x")
        return int(size[0]) * int(size[1])

    def data_to_item(self, entry) -> Item:
        return Item(
            name=entry,
            price=self.item_data[entry]["price"].replace(" ", ""),
            buy_at=self.item_data[entry]["buy_at"].replace(" ", ""),
            currency=self.item_data[entry]["currency"],
            vendor=self.item_data[entry]["trader"],
            refreshes=self.item_data[entry]["refresh"],
            size=self.get_size(self.item_data[entry]["size"])
        )


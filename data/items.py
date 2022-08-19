from dataclasses import dataclass
import json
import glob
from PIL import Image
from tarkov import TarkovBot


@dataclass
class Item:
    name: str
    price: float
    buy_at: int
    currency: str
    trader: str
    refreshes: int
    size: int

@dataclass
class Inventory:
    total_slots: int
    slots_taken: int


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
        return target in images

    def add_image(self, item: Item):
        self.get_screenshot(f"images/items/{item.name}.png", region=(879, 147, 64, 64))
        img = Image.open(f"images/items/{item.name}.png")
        bottom_corner = img.crop((60, 48, 61, 49))
        for x in range(53, 63):
            for y in range(51, 63):
                img.paste(bottom_corner, (x, y, x + 1, y + 1))
        img.save(f"images/items/{item.name}.png")

    def get_image(self):
        return

    def load_items(self):
        self.load_config()
        for item in self.item_data:
            print(f"Loaded {item}")

    def get_items(self):
        return self.item_data

    def items_sold_at(self, vendor):
        return [item for item in self.item_data if item["trader"] == vendor]

    def data_to_item(self, entry) -> Item:
        return Item(
            name=entry,
            price=self.item_data[entry]["price"],
            buy_at=self.item_data[entry]["buy_at"],
            currency=self.item_data[entry]["currency"],
            trader=self.item_data[entry]["trader"],
            refreshes=self.item_data[entry]["refresh"],
            size=self.item_data[entry]["size"]
        )

from dataclasses import dataclass
import json
import glob
from screen import Screen
from PIL import Image
from tarkov import TarkovBot


@dataclass
class Item:
    """Stores item properties, created by database"""

    name: str
    price: float
    buy_at: int
    currency: str
    vendor: str
    refreshes: int
    size: int
    buy_amount: int


@dataclass
class Inventory(TarkovBot):
    """Inventory class containing slots to empty, amount of slots at
    which to empty and amount of slots currently taken, alongside methods
    to request the state
    """

    def __init__(self):
        super().__init__()
        self.allowed_scrolls = self.config["allowed_scrolls"]
        self.max_slots = self.config["empty_inv_at"]
        self.slots_taken = 0

    def is_full(self) -> bool:
        """Checks if the inventory is full"""
        return self.slots_taken >= self.max_slots

    def reset(self) -> None:
        """Resets the taken slots"""
        self.slots_taken = 0

    def add_items(self, amount, size):
        self.slots_taken += amount * int(size)


class Database(TarkovBot):
    """Database handler
    ---------------------
    Handles all the information about items from the data files,
    creates instances of :class:`Item` from their json values.
    Checks if items have images and adds item images.
    """

    def __init__(self) -> None:
        self.load_config()
        self.images = glob.glob("images/*.png")

    def load_config(self):
        """Read from data"""
        with open("data/data.json") as f:
            self.item_data = json.load(f)

    def load_images(self):
        """Get a list of all images in the items folder"""
        self.images = glob.glob("images/items/*.png")

    def get_items(self):
        return self.item_data

    def has_image(self, target):
        """Checks if an item already has an image"""
        self.load_images()
        target = target.name.replace('"', "")
        images = [
            image.removeprefix("images/items\\").removesuffix(".png")
            for image in self.images
        ]
        return target in images

    def add_image(self, item: Item):
        """Adds the image of an item to the image database"""
        self.notify(item, "does not have an image yet, adding...")

        # remove the " from the name to avoid path errors
        path = item.name.replace('"', "")
        self.get_screenshot(
            f"images/items/{path}.png", region=(879, 147, 64, 64))

        # edit the bottom right corner to paint over any numbers shown
        img = Image.open(f"images/items/{path}.png")
        bottom_corner = img.crop((60, 48, 61, 49))
        for x in range(53, 63):
            for y in range(51, 63):
                img.paste(bottom_corner, (x, y, x + 1, y + 1))
        img.save(f"images/items/{path}.png")

    @staticmethod
    def load_inventory_image(item):
        """Checks if an item already has an inventory image"""

        # get list of all images in the directory
        directory = "images/inv"
        all_items = [
            image.removeprefix("images/inv\\").removesuffix(".png")
            for image in glob.glob("images/inv/*.png")
        ]

        # check if the item is in the images
        img = item.replace('"', "")
        if img in all_items:
            return "Available"
        return "Missing"

    def add_inventory_image(self, item):
        """Adds an items inventory image to database"""
        # get the items x and y axis by size
        item_size = self.item_data[item]["size"].split("x")
        path = item.replace('"', "")

        # 1270, 260 = topleft corner, now get width & height of item by size
        size = int(item_size[0]) * 64, int(item_size[1]) * 64
        Screen.get_screenshot(
            f"images/inv/{path}.png", region=(1270, 260, *size))

    def get_items_to_purchase(self):
        """Returns a list of items from the data dict"""
        self.load_config()
        return [
            self.data_to_item(item)
            for item in self.get_items()
            if self.item_data[item]["enabled"]
        ]

    def items_sold_at(self, vendor):
        """Returns a list of all items sold at a certain vendor"""
        return [item for item in self.item_data if item["trader"] == vendor]

    def get_size(self, size):
        """Gets the size of an item as integer"""
        size = size.split("x")
        return int(size[0]) * int(size[1])

    def data_to_item(self, entry) -> Item:
        """Converts an item dict to an Item instance"""
        return Item(
            name=entry,
            price=self.item_data[entry]["price"].replace(" ", ""),
            buy_at=self.item_data[entry]["buy_at"].replace(" ", ""),
            currency=self.item_data[entry]["currency"],
            vendor=self.item_data[entry]["trader"],
            refreshes=self.item_data[entry]["refresh"],
            size=self.get_size(self.item_data[entry]["size"]),
            buy_amount=self.item_data[entry]["buy_amount"],
        )

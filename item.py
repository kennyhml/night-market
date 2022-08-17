from dataclasses import dataclass
import json


@dataclass
class Item:
    name: str
    price: float
    buy_at: int
    currency: str
    trader: str
    refreshes: int


class Database:
    def __init__(self) -> None:
        self.load_items()

    def load_config(self):
        with open("data/data.json") as f:
            self.item_data = json.load(f)

    def load_items(self):
        self.load_config()
        for item in self.item_data:
            print(f"Loaded {item}")

    def get_items(self):
        return self.item_data

    def data_to_item(self, entry) -> Item:
        return Item(
            name=entry,
            price=self.item_data[entry]["price"],
            buy_at=self.item_data[entry]["buy_at"],
            currency=self.item_data[entry]["currency"],
            trader=self.item_data[entry]["trader"],
            refreshes=self.item_data[entry]["refresh"],
        )

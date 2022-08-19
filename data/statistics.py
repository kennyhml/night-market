
import json

from nightmart_bot import Discord

class Statistics:
    def __init__(self, items) -> None:
        self.items = self.get_data(items)
        self.total_profit = 0

    def add_purchase(self, purchases):
        added_item = purchases[0].item.name
        items_profits = [(purchase.profit, purchase.amount) for purchase in purchases]

        for profit in items_profits:
            self.items[added_item]["total_quantity"] += int(profit[1])
            self.items[added_item]["total_profit"] += int(profit[0])
            self.total_profit += int(profit[0])

        self.items[added_item]["average_profit"] = round(
            self.items[added_item]["total_profit"]
            / self.items[added_item]["total_quantity"]
        )

        print(json.dumps(self.items, indent=4))

    def get_data(self, items):
        data = {}
        for item in items:
            data[item.name] = {
                "total_quantity": 0,
                "average_profit": 0,
                "total_profit": 0,
            }
        return data

    def send_stats(self):
        discord = Discord()
        discord.send_statistics(self.items, self.total_profit)
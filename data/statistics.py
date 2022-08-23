import json
import time

from nightmart_bot import Discord


class Statistics:
    def __init__(self, items) -> None:
        self.items = self.data_to_dict(items)
        self.last_sent = time.time()
        self.inventories_emptied = 0
        self.session_start = time.time()
        self.last_profit = None
        self.start_money = None

        with open("data\statistics.json", "r") as json_file:
            self.stats_data = json.load(json_file)

    def add_purchase(self, purchases, founds, item):
        with open("data\statistics.json", "r") as json_file:
            self.stats_data = json.load(json_file)
        added_item = item.name

        if not purchases:
            self.stats_data[added_item]["times_searched"] += item.refreshes + 1
            with open("data\statistics.json", "w") as json_file:
                json.dump(self.stats_data, json_file, indent=4)
            return

        profits = [(purchase.profit, purchase.amount) for purchase in purchases]

        for profit in profits:
            self.items[added_item]["total_quantity"] += int(profit[1])
            self.items[added_item]["total_profit"] += int(profit[0])

            self.stats_data[added_item]["total_quantity"] += int(profit[1])
            self.stats_data[added_item]["total_profit"] += int(profit[0])

        self.stats_data[added_item]["times_searched"] += purchases[0].item.refreshes + 1
        self.stats_data[added_item]["times_found"] += founds

        self.items[added_item]["average_profit"] = round(
            self.items[added_item]["total_profit"]
            / self.items[added_item]["total_quantity"]
        )

        with open("data\statistics.json", "w") as json_file:
            json.dump(self.stats_data, json_file, indent=4)


    def shorten_name(self, name):
        if len(name.split(" ")) > 4:
            return " ".join(part for part in name.split(" ")[:4])
        return name

    def get_special_items(self, best=True):
        """Returns three dictionaries of items containing name, quanitity and profit.
        Can return either the top three or the bottom three items.
        """
        profits = set([self.items[val]["total_profit"] for val in self.items])
        profits = sorted(list(profits), reverse=True)

        for item in self.items:
            if self.items[item]["total_profit"] == profits[0 if best else -1]:
                item_1 = {
                    "name": self.shorten_name(item),
                    "quantity": self.items[item]["total_quantity"],
                    "profit": self.items[item]["total_profit"],
                }

            elif self.items[item]["total_profit"] == profits[1 if best else -2]:
                item_2 = {
                    "name": self.shorten_name(item),
                    "quantity": self.items[item]["total_quantity"],
                    "profit": self.items[item]["total_profit"],
                }

            elif self.items[item]["total_profit"] == profits[2 if best else -3]:
                item_3 = {
                    "name": self.shorten_name(item),
                    "quantity": self.items[item]["total_quantity"],
                    "profit": self.items[item]["total_profit"],
                }

        return [item_1, item_2, item_3]

    def get_data(self):
        return self.items


    def data_to_dict(self, items):
        data = {}
        for item in items:
            data[item.name] = {
                "total_quantity": 0,
                "average_profit": 0,
                "total_profit": 0,
            }
        return data

    def get_session_time(self):
        return time.strftime(
            "%H:%M:%S", time.gmtime((time.time() - self.session_start))
        )

    def get_cycle_time(self):
        time_taken = time.strftime("%H:%M:%S", time.gmtime((time.time() - self.last_sent)))
        self.last_sent = time.time()
        return time_taken

    def get_total_profit(self):
        return sum([self.items[item]["total_profit"] for item in self.items])

    def profit_to_money(self):
        return "~" + str(round(self.get_total_profit() / 480_000, 2)) + " €"

    def send_stats(self, current_money):

        if not self.last_profit:
            profit = self.get_total_profit()
            self.last_profit = profit

        else:
            profit = self.get_total_profit() - self.last_profit
            self.last_profit = self.get_total_profit()

        if not self.start_money:
            self.start_money = current_money - profit

        data = {
            "top_items": self.get_special_items(),
            "bot_items": self.get_special_items(False),
            "total_profit": current_money - self.start_money,
            "emptying_profit": profit,
            "current_money": current_money,
            "session_time": self.get_session_time(),
            "empty_time": self.get_cycle_time(),
            "profit_in_euro": self.profit_to_money()
        }
        self.last_money = current_money

        discord = Discord()
        discord.send_statistics(data)

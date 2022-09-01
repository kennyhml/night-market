import json
import time
from data.items import Item

from nightmart_bot import Discord
from datetime import datetime


class Statistics:
    """Statistics management
    ------------------------
    Handles all items statistics, stored in statistics.json, adds new
    statistics or gives requested information. Plays a big role displaying
    statistics or sending them as discord embed.
    """

    def __init__(self, items) -> None:
        self.items = self.data_to_dict(items)
        self.last_sent = time.time()
        self.inventories_emptied = 0
        self.session_start = time.time()
        self.last_profit = None
        self.start_money = None
        self.load_data()

    def load_data(self):
        with open("data\statistics.json", "r") as json_file:
            self.stats_data = json.load(json_file)

        with open("data\data.json", "r") as json_file:
            self.data = json.load(json_file)

    def save_data(self):
        with open("data\statistics.json", "w") as json_file:
            json.dump(self.stats_data, json_file, indent=4)
            
        with open("data\data.json", "w") as json_file:
            json.dump(self.data, json_file, indent=4)
            
    def get_data(self):
        return self.stats_data

    def add_purchase(self, purchases, founds, item: Item):
        """Adds a purchase to the statistics"""
        self.load_data()
        added_item = item.name

        # theres no purchases recorded so just add the searches
        if not purchases:
            self.stats_data[added_item]["times_searched"] += item.refreshes + 1
            self.save_data()
            return

        # get total profit and quantity of all purchases
        profit = sum([purchase.profit for purchase in purchases])
        quantity = sum([purchase.amount for purchase in purchases])

        # add purchase to the internal stats and statistics.json
        self.items[added_item]["total_quantity"] += int(quantity)
        self.items[added_item]["total_profit"] += int(profit)

        self.stats_data[added_item]["total_quantity"] += int(quantity)
        self.stats_data[added_item]["total_profit"] += int(profit)

        # add the overall purchase data
        self.stats_data[added_item]["times_searched"] += item.refreshes + 1
        self.stats_data[added_item]["times_found"] += founds

        # calculate the new average profit for the item
        self.items[added_item]["average_profit"] = round(
            self.items[added_item]["total_profit"]
            / self.items[added_item]["total_quantity"]
        )

        if item.buy_amount and quantity >= item.buy_amount:
            self.data[added_item]["enabled"] = False
            print(added_item, " has reached its maximum purchases and has been disabled!")

        self.save_data()
       
    def shorten_name(self, name):
        """Shortens a name with more than 4 segments"""
        if len(name.split(" ")) > 4:
            return " ".join(part for part in name.split(" ")[:4])
        return name

    def get_special_items(self, best=True):
        """Returns three dictionaries of items containing name, quanitity and profit.
        Can return either the top three or the bottom three items.
        """
        profits = set([self.items[val]["total_profit"] for val in self.items])
        profits = sorted(list(profits), reverse=True)

        try:
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
        except:
            return [None, None, None]

    def data_to_dict(self, items):
        """Converts a list of items into a data dict"""
        data = {}
        for item in items:
            data[item.name] = {
                "total_quantity": 0,
                "average_profit": 0,
                "total_profit": 0,
            }
        return data

    def get_session_time(self):
        """Gets the current session time"""
        return time.strftime(
            "%H:%M:%S", time.gmtime((time.time() - self.session_start))
        )

    def get_cycle_time(self):
        """Gets the current empty cycles time"""
        time_taken = time.strftime(
            "%H:%M:%S", time.gmtime((time.time() - self.last_sent))
        )

        # set new time
        self.last_sent = time.time()
        return time_taken

    def get_total_profit(self):
        """Gets the sum of all items"""
        return sum([self.items[item]["total_profit"] for item in self.items])

    def profit_to_money(self):
        """Gets the real money value of the current profit"""
        return "~" + str(round(self.get_total_profit() / 480_000, 2)) + " €"

    def get_emptying_profit(self):
        """Gets the emptying profit"""
        total_profit = self.get_total_profit()
        # if theres no prior profit, the current total profit is the profit
        # and the current profit will be the prior profit for next time
        if not self.last_profit:
            profit = total_profit
            self.last_profit = profit

        # there already is a profit so this times profit is the difference of
        # this times total profit - last times total profit
        else:
            profit = total_profit - self.last_profit
            self.last_profit = total_profit

        return profit

    def get_profit_per_hour(self):
        """Gets the current hourly profit"""
        # get session time and current profit
        session = self.get_session_time()
        profit = self.get_total_profit()

        # get hours and minutes by slicing time string
        hours = int(session[:2])
        minutes = int(session[3:5])

        # get total minutes and calculate the hourly profit
        total_min = hours * 60 + minutes
        return round(profit / total_min) * 60

    def send_stats(self, current_money):
        """Calculates and sends the stats to discord, refreshes
        the timeline statistics.
        """
        profit = self.get_emptying_profit()

        # starting money is first empty money - the empty profit
        if not self.start_money:
            self.start_money = current_money - profit

        data = {
            "top_items": self.get_special_items(),
            "bot_items": self.get_special_items(False),
            "total_profit": (current_money - self.start_money, self.get_total_profit()),
            "emptying_profit": profit,
            "current_money": current_money,
            "session_time": self.get_session_time(),
            "empty_time": self.get_cycle_time(),
            "profit_in_euro": self.profit_to_money(),
            "hourly_profit": self.get_profit_per_hour(),
        }
        # update the timeline
        self.last_money = current_money
        self.update_timeline(data)

        # send stats to discord
        discord = Discord()
        discord.send_statistics(data)

    def update_timeline(self, data):
        """Updates the timeline of profits, the timeline only ever includes
        the last 3 days. The timeline entries contain the time they have
        been added in HH:MM:SS format and the hourly rate at the time.
        """
        # get todays date
        self.load_data()
        timeline = self.stats_data["timeline"]
        today = datetime.today()
        today_str = datetime.strftime(today, "%Y-%m-%d")

        # check if today is in timeline, create if its not
        if today_str not in timeline:
            self.stats_data["timeline"][today_str] = {}

        # remove any entries older than 3 days
        to_rm = []
        for date in timeline:
            data_day = datetime.strptime(str(date), "%Y-%m-%d")

            diff = today - data_day
            if diff.days > 2:
                to_rm.append(date)

        for date in to_rm:
            self.stats_data["timeline"].pop(date)
            print(f"{date} has been removed from the timeline!")

        # add a new entry for the current time with the current hourly profit
        current_time = datetime.now().strftime("%H:%M:%S")
        self.stats_data["timeline"][today_str][current_time] = data["hourly_profit"]

        self.save_data()

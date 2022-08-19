from tracemalloc import Statistic
from data.statistics import Statistics
from market.market import MarketUI
from data.items import Database, Inventory
from tarkov import BotTerminated, TarkovBot
import time

from traders import SellUi, Therapist
from market.purchase import NoMoneyLeft

market = MarketUI()









def main():

    # initialize database from data file
    data = Database()
    vendor = SellUi()
    inventory = Inventory(60, 0)

    start = time.time()
    # vendor.post_current_money()
    items_to_buy = [data.data_to_item(item) for item in data.get_items()]
    statistics = Statistics(items_to_buy)

    while TarkovBot.running:

        for item in items_to_buy:

            try:
                market.open()
                market.search_item(item)

                # new inventory value and list of purchchases
                inventory, purchases = market.get_available_purchases(item, inventory)

                if inventory.total_slots - inventory.slots_taken < 5:
                    market.discord.send_message(f"The inventory needs to be emptied!")
                    empty_inventory(vendor, Therapist.location)
                    inventory = Inventory(70, 0)
                    continue

                if purchases:
                    statistics.add_purchase(purchases)

                if market.has_timedout(start, 1800):
                    print("30 mins passed!")
                    statistics.send_stats()



            except NoMoneyLeft:
                pass

            except BotTerminated:
                pass

            except TimeoutError:
                market.started_searching = time.time()
                market.press("esc")


def empty_inventory(vendor: SellUi, trader_loc):
    vendor.open()
    vendor.open_trader(trader_loc)
    vendor.open_sell_tab()
    vendor.sell_items()
    vendor.post_current_money()


main()

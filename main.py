
from data.statistics import Statistics
from market.market import MarketUI
from data.items import Database, Inventory
from tarkov import BotTerminated, TarkovBot
import time

from traders import TraderUi, Therapist, TraderUi
from market.purchase import NoMoneyLeft

market = MarketUI()









def main():

    # initialize database from data file
    data = Database()
    vendor = TraderUi()
    inventory = Inventory(60, 0)

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

                # add the purchase to stats
                statistics.add_purchase(purchases)

                if inventory.total_slots - inventory.slots_taken < 5:
                    market.discord.send_message(f"The inventory needs to be emptied!")
                    profit, current_money = vendor.sell(Therapist.location)
                    statistics.send_stats(profit, current_money)
                    inventory = Inventory(60, 0)

            except Exception:
                market.started_searching = time.time()
                market.press("esc")
                

main()

from market import MarketUI, NoMoneyLeft
from item import Database, Item
from tarkov import BotTerminated, TarkovBot
import time

from traders import SellUi, Therapist

market = MarketUI()


def main():

    # initialize database from data file
    data = Database()
    vendor = SellUi()

    items_to_buy = [data.data_to_item(item) for item in data.get_items()]
    start = time.time()
    vendor.post_current_money()

    while TarkovBot.running:

        for item in items_to_buy:

            market.open()
            market.search_item(item)

            try:
                market.get_available_purchases(item)

            except NoMoneyLeft:
                pass

            except BotTerminated:
                pass

            if TarkovBot.has_timedout(start, 300):
    
                vendor.open()
                vendor.open_trader(Therapist.location)
                vendor.open_sell_tab()
                vendor.sell_items()
                vendor.post_current_money()
                start = time.time()

        market.notify("Completed a cycle of all items!")
        market.discord.send_message(f"{round(300 - (time.time() - start))} seconds left until selling...")

main()
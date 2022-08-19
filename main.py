from market.market import MarketUI
from item import Database, Item
from tarkov import BotTerminated, TarkovBot
import time
import pyautogui as pg
from threading import Thread
from traders import SellUi, Therapist
from market.purchase import NoMoneyLeft
market = MarketUI()


def main():

    # initialize database from data file
    data = Database()
    vendor = SellUi()

    items_to_buy = [data.data_to_item(item) for item in data.get_items()]
    print(items_to_buy)
    start = time.time()
    vendor.post_current_money()

    while TarkovBot.running:

        for item in items_to_buy:

            try:
                market.open()
                market.search_item(item)
                market.get_available_purchases(item)

                # send the purchases to discord if there are any

            except NoMoneyLeft:
                pass

            except BotTerminated:
                pass

            except TimeoutError:
                market.started_searching = time.time()
                market.press("esc")

            if TarkovBot.has_timedout(start, 180):
    
                vendor.open()
                vendor.open_trader(Therapist.location)
                vendor.open_sell_tab()
                vendor.sell_items()
                vendor.post_current_money()
                start = time.time()

        market.notify("Completed a cycle of all items!")
        market.discord.send_message(f"{round(180 - (time.time() - start))} seconds left until selling...")

main()
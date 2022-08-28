from screen import Screen
from data.statistics import Statistics
from gui.main_ui_handle import MainUi
from market.market import MarketUI
from market.purchase import OutOfMoneyError
from market.searchbar import NoItemsListed
from data.items import Database, Inventory, Item
from nightmart_bot import Discord
from tarkov import BotTerminated, TarkovBot

from traders import VendorHandler
from threading import Thread
from pynput import keyboard
import time

def on__key_press(key):
    """Connets inputs from listener thread to their corresponding function"""

    if key == keyboard.Key.f1:  # started
        # make sure bot is not already active
        if not (TarkovBot.paused or TarkovBot.running):

            ui.save_changes = False  # disable changes
            TarkovBot.running = True  # set active
            time.sleep(5)
            bot = Thread(target=main, daemon=True, name="Main bot Thread")
            bot.start()

    elif key == keyboard.Key.f3:  # terminated
        ui.set_bot_status("Idle - Press F1 to start!")

        if TarkovBot.running:
            TarkovBot.paused = False
            TarkovBot.running = False  # stop the bot
            ui.save_changes = True  # allow config changes again

    elif key == keyboard.Key.f2:  # paused
        if TarkovBot.running and not TarkovBot.paused:  # not currently paused
            TarkovBot.paused = True  # pause the bot

        elif TarkovBot.running and TarkovBot.paused:  # already paused (so resume)
            TarkovBot.paused = False

def main():
    """
    Main loop for the bots workflow. Continues to loop over all items
    enabled in the current session, handles exceptions directly
    """
    # initialize database from data file
    data = Database()
    items = data.get_items_to_purchase()
    statistics = Statistics(items)
    inventory = Inventory()
    market = MarketUI()
    discord = Discord()

    while True:
        # iterate over all items checking each
        for item in items:
            try:
                try:
                    # search for the current item
                    market.open()
                    market.search_item(item)
                    
                except NoItemsListed:
                    continue

                try:
                    # get new inventory, purchases and amount founds
                    inventory, purchases, founds = market.get_available_purchases(
                        item, inventory
                    )
                except OutOfMoneyError:
                    empty_inventory(statistics, item.vendor, inventory, item, items)

                # add the purchase to stats
                statistics.add_purchase(purchases, founds, item)
                if inventory.is_full():
                    empty_inventory(statistics, item.vendor, inventory, item, items)

            except BotTerminated:
                return

            except TimeoutError:
                discord.send_image(
                    Screen.get_screenshot("images/temp/error.png"), f"Timed out!"
                )
                market.press("esc")

            except Exception as e:
                discord.send_image(
                    Screen.get_screenshot("images/temp/error.png"),
                    f"Unhandled error!\n{e}",
                )
                market.press("esc")


def empty_inventory(
    statistics: Statistics, inventory: Inventory, item: Item, items: list[Item]
):
    vendor = VendorHandler()
    current_money = vendor.sell(item.vendor, inventory, items)
    statistics.send_stats(current_money)
    inventory.reset()
    ui.display_timeline_profits()


if __name__ == "__main__":

    listener = keyboard.Listener(on_press=on__key_press)
    listener.start()  # start listener thread

    ui = MainUi()
    ui.display()

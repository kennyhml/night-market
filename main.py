from screen import Screen
from data.statistics import Statistics
from gui.main_ui_handle import MainUi
from market.market import MarketUI
from data.items import Database, Inventory
from nightmart_bot import Discord
from tarkov import BotTerminated, TarkovBot

import json
from traders import VendorUi
from threading import Thread
from pynput import keyboard


def on__key_press(key):
    """Connets inputs from listener thread to their corresponding function"""

    if key == keyboard.Key.f1:  # started
        # make sure bot is not already active
        if not (TarkovBot.paused or TarkovBot.running):

            ui.save_changes = False  # disable changes
            TarkovBot.running = True  # set active
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

    # initialize database from data file
    data = Database()
    items = data.get_items_to_purchase()
    statistics = Statistics(items)
    inventory = Inventory()

    while TarkovBot.running:
        market = MarketUI()

        for item in items:
            try:
                market.open()
                market.search_item(item)

                # new inventory value and list of purchchases
                inventory, purchases, founds = market.get_available_purchases(
                    item, inventory
                )

                # add the purchase to stats
                statistics.add_purchase(purchases, founds, item)

                if inventory.is_full():
                    vendor = VendorUi()
                    current_money = vendor.sell(item.vendor, inventory)
                    statistics.send_stats(current_money)
                    inventory.reset()
                    ui.display_timeline_profits()
                    
            except BotTerminated:
                return

            except TimeoutError:
                discord = Discord()
                discord.send_image(
                    Screen.get_screenshot("images/temp/error.png"), f"Timed out!"
                )
                market.press("esc")

            except Exception as e:
                discord = Discord()
                discord.send_image(
                    Screen.get_screenshot("images/temp/error.png"),
                    f"Unhandled error!\n{e}",
                )
                market.press("esc")

        print(json.dumps(statistics.get_data()))


if __name__ == "__main__":

    listener = keyboard.Listener(on_press=on__key_press)
    listener.start()  # start listener thread

    ui = MainUi()

    ui.display()

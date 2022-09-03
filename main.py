
from data.statistics import Statistics
from gui.login_ui_handle import Login
from gui.main_ui_handle import MainUi
from market.market import MarketUI, TooManyItems
from market.purchase import OutOfMoneyError, InventoryFullError
from market.searchbar import NoItemsListed
from data.items import Database, Inventory, Item
from tarkov import BotTerminated, TarkovBot, lg

from traders import VendorHandler
from threading import Thread
from pynput import keyboard

def on__key_press(key):
    """Connets inputs from listener thread to their corresponding function"""

    if key == keyboard.Key.f1:  # started
        # make sure bot is not already active
        if not (TarkovBot.paused or TarkovBot.running):
            ui.set_bot_status("Active - Farming money!")

            ui.save_changes = False  # disable changes
            TarkovBot.running = True  # set active
            TarkovBot.sleep_start_delay()
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
            ui.set_bot_status("Paused - Press F2 to resume!")

        elif TarkovBot.running and TarkovBot.paused:  # already paused (so resume)
            TarkovBot.paused = False
            ui.set_bot_status("Active - Farming money!")

def main():
    """
    Main loop for the bots workflow. Continues to loop over all items
    enabled in the current session, handles exceptions directly
    """
    # initialize database from data file
    data = Database()
    statistics = Statistics(data.get_items_to_purchase())
    inventory = Inventory()
    market = MarketUI()

    while True:
        
        items = data.get_items_to_purchase()
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
                except (OutOfMoneyError, InventoryFullError):
                    market.press("esc", 1)
                    empty_inventory(statistics, inventory, items)

                except TooManyItems:
                    continue

                # add the purchase to stats
                statistics.add_purchase(purchases, founds, item)
                if inventory.is_full():
                    empty_inventory(statistics, inventory, items)

            except BotTerminated:
                return
                
            except Exception:
                lg.exception("Unhandled error in main function!")
                market.press("esc")


def empty_inventory(
    statistics: Statistics, inventory: Inventory, items: list[Item]
):
    """Empties the inventory at the vendors

    Parameters
    -------------
    statistics: :class:`Statistics`
        The statistics instance of the current run to add the profit to

    inventory: :class:`Inventory`
        The inventory configuration dataclass
        
    items: :class:`list[Item]`
        A list of the items to check if there are any to sell
    """

    vendor = VendorHandler()
    current_money = vendor.sell(items, inventory)
    statistics.send_stats(current_money)
    inventory.reset()
    ui.display_timeline_profits()

if __name__ == "__main__":

    login = Login()
    login.display()

    listener = keyboard.Listener(on_press=on__key_press)
    listener.start()  # start listener thread

    ui = MainUi()
    ui.display()

from market import MarketUI
from item import Database, Item
import traders
import tarkov

market = MarketUI()


def main():

    # initialize database from data file
    data = Database()
    database = data.get_items()

    for entry in database:
        
        # create item object with the data
        item: Item = data.data_to_item(entry)

        market.open()
        market.search_item(item)
        market.get_available_purchases(item)







    market.notify("Completed a cycle of all items!")



while 1:
    main()

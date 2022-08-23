import re
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui
import json
import datetime
import sys
import ctypes
from gui.main_ui import Ui_Form

app = QApplication()
main_win = QtWidgets.QMainWindow()


class MainUi(QMainWindow, Ui_Form):

    raw_data_dict = {
        "enabled": True,
        "price": "10 000",
        "buy_at": "9 000",
        "currency": "₽",
        "trader": "Therapist",
        "refresh": 3,
        "size": 1,
    }

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(main_win)
        self.populate_ui()
        self.open_tab(2)
        self.connect_buttons()
        self.connect_changes()
        self.save_changes = True
        print(self.data)

    def display(self):
        main_win.show()
        sys.exit(app.exec())

    def open_tab(self, index):
        self.main_tab.setCurrentIndex(index)

    def start_key_refresh_timer(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.refresh_key)
        timer.start(600000)

    def set_bot_status(self, status):
        """Updates the ui bot status text to the passed status."""
        self.bot_status.setText(
            f'<html><head/><body><p><span style="color:#55ffff;">Bot Status: </span>{status}</p></body></html>'
        )

    def read_files(self):
        with open("data\settings.json", "r") as json_file:
            self.settings = json.load(json_file)

        with open("data\data.json", "r") as json_file:
            self.data = json.load(json_file)

        with open("data\statistics.json", "r") as json_file:
            self.stats = json.load(json_file)

    def save_files(self):
        with open("data\settings.json", "w") as json_file:
            json.dump(self.settings, json_file, indent=4)

        with open("data\data.json", "w") as json_file:
            json.dump(self.data, json_file, indent=4)

        with open("data\statistics.json", "w") as json_file:
            json.dump(self.stats, json_file, indent=4)

    def add_item_data(self):
        """Adds a preset to the config, the preset will hold static default value."""

        # get preset name and confirm
        item_name, confirmed = QtWidgets.QInputDialog.getText(
            self, "Add item", "Please enter the name of the item!"
        )

        if not (confirmed or item_name):  # confirmed and name is valid
            print("Invalid preset name, preset must contain characters or numbers!")
            return

        # make sure the name doesnt already exist
        if item_name in self.data:
            QtWidgets.QMessageBox.about(
                self,
                "Item not added!",
                (
                    "This item could not be added."
                    "\nItem already exists with this name."
                    "\n\nPlease switch to that item with the drop-down menu."
                    "\nOr delete that item and try again."
                    "\nItem names must be unique!"
                ),
            )
            return

        item_value, confirmed = QtWidgets.QInputDialog.getText(
            self,
            "Add item properties",
            "Please enter the value of the item!\n\n"
            "The value is how much the Therapist buys it for.",
        )

        if not confirmed:
            return

        max_price, confirmed = QtWidgets.QInputDialog.getText(
            self,
            "Add item properties",
            "Please enter the max price of the item!\n\n"
            "The max price is what the bot will\n"
            "set in the filter to find the item.",
        )
        if not confirmed:
            return

        if int(item_value.replace(" ", "")) < int(max_price.replace(" ", "")):
            QtWidgets.QMessageBox.about(
                self,
                "Item not added!",
                (
                    "This item could not be added."
                    "\nItem's value is smaller than the max price."
                    "\n\nPlease make sure to get the values correct!"
                    "\n Double check the values and try again."
                ),
            )
            return

        data = {
            "enabled": True,
            "price": item_value,
            "buy_at": max_price,
            "currency": "₽",
            "trader": "Therapist",
            "refresh": 3,
            "size": 1,
        }

        self.data[item_name] = data
        self.save_files()
        print(f"{item_name} was added to your items!")
        self.populate_ui()  # update ui
        self.current_item.setCurrentIndex(
            [i for i in range(self.current_item.count())][-1]
        )

    def delete_item_data(self):
        """Deletes the currently active preset"""

        if len(self.data) <= 2:  # make sure there will be a preset left
            print(
                "Could not delete the item, you must"
                "have more than one item in order to delete one!"
            )
            return

        confirm = ctypes.windll.user32.MessageBoxW(
            0,
            f"Are you sure you want to delete '{self.current_item.currentText()}'?\n"
            "\nThis cannot be undone!",
            "Delete preset",
            4,
        )
        if confirm == 6:
            self.data.pop(self.current_item.currentText())
            self.save_files()
            self.populate_ui()

    def sync_stats_data(self):

        raw_data = {
            "total_quantity": 0,
            "total_profit": 0,
            "times_searched": 0,
            "times_found": 0,
        }

        for entry in self.data:
            if entry not in self.stats:
                self.stats[entry] = raw_data

    def populate_ui(self):
        self.save_changes = False

        self.read_files()
        self.mouse_movement_mode.setCurrentText(self.settings["mouse_movement"])
        self.mouse_speed.setValue(self.settings["mouse_speed"])

        self.item_search_mode.setCurrentText(self.settings["item_searching"])
        self.use_wishlist_tab.setChecked(self.settings["use_wishlist"])

        # inventory related
        self.allowed_inv_slots.setValue(self.settings["allowed_inv_slots"])
        self.empty_inv_at.setValue(self.settings["empty_inv_at"])

        # discord related
        self.post_to_discord.setChecked(self.settings["post_discord"])
        self.at_on_events.setChecked(self.settings["discord_mention"])
        self.discord_webhook.setText(self.settings["discord_webhook"])
        self.discord_id.setText(self.settings["discord_id"])

        combobox = [
            self.current_item.itemText(i) for i in range(self.current_item.count())
        ]

        for item in self.data:
            if item not in combobox:
                self.current_item.addItem(item)

        for item in combobox:
            if item not in self.data:
                self.current_item.removeItem(
                    self.current_item.findText(item, QtCore.Qt.MatchFixedString)
                )

        current_item = self.current_item.currentText()

        self.item_value.setText(self.data[current_item]["price"])
        self.item_max_price.setText(self.data[current_item]["buy_at"])

        self.item_currency.setCurrentText(self.data[current_item]["currency"])
        self.item_vendor.setCurrentText(self.data[current_item]["trader"])
        self.item_refreshes.setValue(self.data[current_item]["refresh"])
        self.item_size.setCurrentText(str(self.data[current_item]["size"]))
        self.item_enabled.setChecked(self.data[current_item]["enabled"])

        self.item_profit.setText(
            str(
                int(self.data[current_item]["price"].replace(" ", ""))
                - int(self.data[current_item]["buy_at"].replace(" ", ""))
            )
        )

        self.item_stats_searched.setText(str(self.stats[current_item]["times_searched"]))
        self.item_stats_bought.setText(str(self.stats[current_item]["total_quantity"]))
        self.item_stats_total_profit.setText(str(self.stats[current_item]["total_profit"]))
        self.item_stats_found.setText(str(self.stats[current_item]["times_found"]))
        if int(self.stats[current_item]["total_quantity"]):
            self.item_stats_avg_profit.setText(
                str(
                    int(
                        self.stats[current_item]["total_profit"]
                        / int(self.stats[current_item]["total_quantity"])
                    )
                )
            )
        else:self.item_stats_avg_profit.setText("0")

        self.save_changes = True
        self.sync_stats_data()
        print("Ui populated.")

        self.save_settings()

    def save_item_settings(self):
        if not self.save_changes:
            return

        current_item = self.current_item.currentText()

        self.data[current_item]["price"] = self.item_value.toPlainText()
        self.data[current_item]["buy_at"] = self.item_max_price.toPlainText()
        self.data[current_item]["currency"] = self.item_currency.currentText()
        self.data[current_item]["trader"] = self.item_vendor.currentText()
        self.data[current_item]["refresh"] = self.item_refreshes.value()
        self.data[current_item]["size"] = self.item_size.currentText()
        self.data[current_item]["enabled"] = self.item_enabled.isChecked()
        self.save_files()

    def save_settings(self):
        if not self.save_changes:
            return

        # general searching stuff
        self.settings["mouse_movement"] = self.mouse_movement_mode.currentText()
        self.settings["mouse_speed"] = self.mouse_speed.value()
        self.settings["item_searching"] = self.item_search_mode.currentText()
        self.settings["use_wishlist"] = self.use_wishlist_tab.isChecked()

        # inventory related
        self.settings["allowed_inv_slots"] = self.allowed_inv_slots.value()
        self.settings["empty_inv_at"] = self.empty_inv_at.value()

        # discord related
        self.settings["post_discord"] = self.post_to_discord.isChecked()
        self.settings["discord_mention"] = self.at_on_events.isChecked()
        self.settings["discord_webhook"] = self.discord_webhook.toPlainText()
        self.settings["discord_id"] = self.discord_id.toPlainText()

        self.save_item_settings()
        self.save_files()
        print("New settings applied.")

    def connect_buttons(self):

        self.buttons_general.clicked.connect(lambda: self.open_tab(0))
        self.buttons_license.clicked.connect(lambda: self.open_tab(1))
        self.buttons_database.clicked.connect(lambda: self.open_tab(2))
        self.add_item.clicked.connect(self.add_item_data)
        self.delete_item.clicked.connect(self.delete_item_data)

    def connect_changes(self):

        self.mouse_movement_mode.currentIndexChanged.connect(self.save_settings)
        self.item_search_mode.currentIndexChanged.connect(self.save_settings)
        self.mouse_speed.valueChanged.connect(self.save_settings)
        self.use_wishlist_tab.stateChanged.connect(self.save_settings)

        self.allowed_inv_slots.valueChanged.connect(self.save_settings)
        self.empty_inv_at.valueChanged.connect(self.save_settings)

        self.post_to_discord.stateChanged.connect(self.save_settings)
        self.at_on_events.stateChanged.connect(self.save_settings)
        self.discord_webhook.textChanged.connect(self.save_settings)
        self.discord_id.textChanged.connect(self.save_settings)

        self.item_value.textChanged.connect(self.save_item_settings)
        self.item_max_price.textChanged.connect(self.save_item_settings)
        self.item_currency.currentIndexChanged.connect(self.save_item_settings)
        self.item_vendor.currentIndexChanged.connect(self.save_item_settings)
        self.item_refreshes.valueChanged.connect(self.save_item_settings)
        self.item_size.currentIndexChanged.connect(self.save_item_settings)
        self.item_enabled.clicked.connect(self.save_item_settings)

        self.current_item.currentIndexChanged.connect(self.populate_ui)

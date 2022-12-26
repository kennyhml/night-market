import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui
from gui.login_ui import LoginUi
import json
import webbrowser

app = QApplication()
main_win = QtWidgets.QMainWindow()


class Login(QMainWindow, LoginUi):
    def __init__(self):
        super().__init__()
        self.setupUi(main_win)
        with open("data\settings.json", "r") as json_file:
            self.config = json.load(json_file)
        self.connect_buttons()

    def display(self):
        main_win.setWindowIcon(QtGui.QIcon(("Images\Shard.ico")))
        main_win.show()
        app.exec()

    def connect_buttons(self):
        self.Login_LoginButton.clicked.connect(self.validate_key)
        self.Login_ExitButton.clicked.connect(sys.exit)
        self.Login_EnterKey.setText(self.config["key"])
        self.Login_DiscordButton.clicked.connect(
            lambda: webbrowser.open("https://discord.gg/D8rWvNGnjX")
        )

    def validate_key(self):
        return True


        with open("data\settings.json", "r") as json_file:
            config = json.load(json_file)

        # read the entered key
        config["key"] = self.Login_EnterKey.text()

        with open("data\settings.json", "w") as json_file:
            json.dump(config, json_file, indent=4)

        valid = key.check_key_valid_hwid()
        if valid:
            self.Login_KeyStatus.setText("Key Status - Key Valid")
            main_win.close()

        self.Login_KeyStatus.setText("Key Status - Key Invalid")

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class LoginUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(626, 554)
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 550, 500))
        self.widget.setStyleSheet(u"QPushButton#Login_LoginButton, #Login_DiscordButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Login_LoginButton:hover, #Login_DiscordButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#Login_LoginButton:pressed, #Login_DiscordButton:pressed{\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(40, 30, 230, 430))
        self.label.setStyleSheet(u"border-image: url(Images/background.png);\n"
"border-top-left-radius: 50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 230, 430))
        self.label_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setPixmap(QPixmap(u"images/gui/gui_left.jpg"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 170, 100, 40))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display Light"])
        font.setPointSize(20)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.Login_EnterKey = QLineEdit(self.widget)
        self.Login_EnterKey.setObjectName(u"Login_EnterKey")
        self.Login_EnterKey.setGeometry(QRect(300, 210, 190, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Display"])
        font1.setPointSize(10)
        self.Login_EnterKey.setFont(font1)
        self.Login_EnterKey.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Login_LoginButton = QPushButton(self.widget)
        self.Login_LoginButton.setObjectName(u"Login_LoginButton")
        self.Login_LoginButton.setGeometry(QRect(295, 295, 190, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Small Light"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.Login_LoginButton.setFont(font2)
        self.Login_KeyStatus = QLabel(self.widget)
        self.Login_KeyStatus.setObjectName(u"Login_KeyStatus")
        self.Login_KeyStatus.setGeometry(QRect(300, 250, 371, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Small Light"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        self.Login_KeyStatus.setFont(font3)
        self.Login_KeyStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Login_DiscordButton = QPushButton(self.widget)
        self.Login_DiscordButton.setObjectName(u"Login_DiscordButton")
        self.Login_DiscordButton.setGeometry(QRect(380, 400, 30, 29))
        self.Login_DiscordButton.setMaximumSize(QSize(30, 30))
        font4 = QFont()
        font4.setFamilies([u"Social Media Circled"])
        font4.setPointSize(15)
        self.Login_DiscordButton.setFont(font4)
        icon = QIcon()
        icon.addFile(u"images/gui/discord.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Login_DiscordButton.setIcon(icon)
        self.Login_DiscordButton.setIconSize(QSize(26, 28))
        self.Login_ExitButton = QPushButton(self.widget)
        self.Login_ExitButton.setObjectName(u"Login_ExitButton")
        self.Login_ExitButton.setGeometry(QRect(480, 35, 21, 21))
        icon1 = QIcon()
        icon1.addFile(u"Images/gui/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Login_ExitButton.setIcon(icon1)
        self.Login_ExitButton.setIconSize(QSize(23, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.Login_EnterKey.setPlaceholderText(QCoreApplication.translate("Form", u"License key", None))
        self.Login_LoginButton.setText(QCoreApplication.translate("Form", u"L o g  I n", None))
        self.Login_KeyStatus.setText(QCoreApplication.translate("Form", u"Key Status - Unknown", None))
        self.Login_DiscordButton.setText("")
        self.Login_ExitButton.setText("")
    # retranslateUi


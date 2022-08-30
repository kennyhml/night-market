# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base_ui.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QTabWidget,
    QTextEdit, QWidget)

from gui.mplwidget import MplWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1020, 619)
        Form.setMinimumSize(QSize(1020, 619))
        Form.setMaximumSize(QSize(1020, 900))
        Form.setStyleSheet(u"\n"
"QPushButton#buttons_other_bots:pressed, #buttons_info:pressed, #buttons_discord:pressed, #buttons_chaos_bot:pressed, #buttons_rotation:pressed, #buttons_keybinds:pressed, #buttons_misc:pressed, #buttons_adv_settings:pressed, #buttons_alt_cycler:pressed{\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"Line#line{\n"
"	color: white;\n"
"}")
        self.MainUi = QWidget(Form)
        self.MainUi.setObjectName(u"MainUi")
        self.background_left = QLabel(self.MainUi)
        self.background_left.setObjectName(u"background_left")
        self.background_left.setEnabled(True)
        self.background_left.setGeometry(QRect(-10, 0, 321, 621))
        self.background_left.setStyleSheet(u"border-image: url(images/gui/gui_left.jpg)\n"
"")
        self.background_left.setPixmap(QPixmap(u"highlightbild-escape-from-tarkov_6005254.jpg"))
        self.background_left.setScaledContents(True)
        self.buttons_general = QPushButton(self.MainUi)
        self.buttons_general.setObjectName(u"buttons_general")
        self.buttons_general.setGeometry(QRect(-20, 30, 271, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.buttons_general.setFont(font)
        self.buttons_general.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-bottom-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"	color:rgba(255, 255, 255, 210);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 120), stop:1 rgba(80, 98, 112, 255));\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {          \n"
"		  background-color: rgb(255, 255,255); \n"
"          border:1px solid rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 160), stop:1 rgba(80, 98, 112, 230));\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Images/SHARD.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.buttons_general.setIcon(icon)
        self.buttons_general.setIconSize(QSize(40, 40))
        self.buttons_database = QPushButton(self.MainUi)
        self.buttons_database.setObjectName(u"buttons_database")
        self.buttons_database.setGeometry(QRect(-20, 100, 271, 41))
        self.buttons_database.setFont(font)
        self.buttons_database.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-bottom-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"	color:rgba(255, 255, 255, 210);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 120), stop:1 rgba(80, 98, 112, 255));\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {          \n"
"		  background-color: rgb(255, 255,255); \n"
"          border:1px solid rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 160), stop:1 rgba(80, 98, 112, 230));\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Images/LopangSilver.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttons_database.setIcon(icon1)
        self.buttons_database.setIconSize(QSize(40, 40))
        self.buttons_license = QPushButton(self.MainUi)
        self.buttons_license.setObjectName(u"buttons_license")
        self.buttons_license.setGeometry(QRect(-20, 240, 271, 41))
        self.buttons_license.setFont(font)
        self.buttons_license.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-bottom-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"	color:rgba(255, 255, 255, 210);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 120), stop:1 rgba(80, 98, 112, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {          \n"
"		  background-color: rgb(255, 255,255); \n"
"          border:1px solid rgb(255, 255, 255);}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 160), stop:1 rgba(80, 98, 112, 230));\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../Images/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttons_license.setIcon(icon2)
        self.buttons_license.setIconSize(QSize(40, 40))
        self.main_tab = QTabWidget(self.MainUi)
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setGeometry(QRect(310, -20, 781, 571))
        font1 = QFont()
        font1.setPointSize(6)
        self.main_tab.setFont(font1)
        self.main_tab.setStyleSheet(u"border: none;\n"
"background-color: rgb(35,35,40);\n"
"color: rgb(255,255,255);\n"
"\n"
"")
        self.maintab_general_config = QWidget()
        self.maintab_general_config.setObjectName(u"maintab_general_config")
        self.use_wishlist_tab = QCheckBox(self.maintab_general_config)
        self.use_wishlist_tab.setObjectName(u"use_wishlist_tab")
        self.use_wishlist_tab.setGeometry(QRect(20, 310, 261, 21))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Display Light"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        self.use_wishlist_tab.setFont(font2)
        self.use_wishlist_tab.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.mouse_movements = QLabel(self.maintab_general_config)
        self.mouse_movements.setObjectName(u"mouse_movements")
        self.mouse_movements.setGeometry(QRect(20, 60, 141, 41))
        self.mouse_movements.setFont(font2)
        self.mouse_movements.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.mouse_movements.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mouse_movement_mode = QComboBox(self.maintab_general_config)
        self.mouse_movement_mode.addItem("")
        self.mouse_movement_mode.addItem("")
        self.mouse_movement_mode.setObjectName(u"mouse_movement_mode")
        self.mouse_movement_mode.setGeometry(QRect(170, 60, 121, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Display Light"])
        font3.setPointSize(11)
        self.mouse_movement_mode.setFont(font3)
        self.mouse_movement_mode.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.mouse_movement_mode.setInsertPolicy(QComboBox.InsertAtBottom)
        self.label_61 = QLabel(self.maintab_general_config)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(724, 202, 20, 20))
        self.label_61.setStyleSheet(u"")
        self.label_61.setPixmap(QPixmap(u"../Images/shared.png"))
        self.label_61.setScaledContents(True)
        self.label_78 = QLabel(self.maintab_general_config)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(707, 303, 20, 20))
        self.label_78.setStyleSheet(u"")
        self.label_78.setPixmap(QPixmap(u"../Images/shared.png"))
        self.label_78.setScaledContents(True)
        self.allowed_inv_slots = QSpinBox(self.maintab_general_config)
        self.allowed_inv_slots.setObjectName(u"allowed_inv_slots")
        self.allowed_inv_slots.setGeometry(QRect(236, 210, 51, 21))
        self.allowed_inv_slots.setFont(font3)
        self.allowed_inv_slots.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(255,255,255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"")
        self.allowed_inv_slots.setMinimum(1)
        self.allowed_inv_slots.setMaximum(10)
        self.allowed_inv_slots.setSingleStep(1)
        self.allowed_inv_slots.setValue(1)
        self.inventory_allowed_slots = QLabel(self.maintab_general_config)
        self.inventory_allowed_slots.setObjectName(u"inventory_allowed_slots")
        self.inventory_allowed_slots.setGeometry(QRect(20, 210, 211, 21))
        self.inventory_allowed_slots.setFont(font2)
        self.inventory_allowed_slots.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.inventory_allowed_slots.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.inventory_empty_at_slots = QLabel(self.maintab_general_config)
        self.inventory_empty_at_slots.setObjectName(u"inventory_empty_at_slots")
        self.inventory_empty_at_slots.setGeometry(QRect(20, 260, 211, 21))
        self.inventory_empty_at_slots.setFont(font2)
        self.inventory_empty_at_slots.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.inventory_empty_at_slots.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.empty_inv_at = QSpinBox(self.maintab_general_config)
        self.empty_inv_at.setObjectName(u"empty_inv_at")
        self.empty_inv_at.setGeometry(QRect(236, 260, 51, 21))
        self.empty_inv_at.setFont(font3)
        self.empty_inv_at.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(255,255,255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"")
        self.empty_inv_at.setMinimum(0)
        self.empty_inv_at.setMaximum(120)
        self.empty_inv_at.setSingleStep(10)
        self.empty_inv_at.setValue(60)
        self.item_searching = QLabel(self.maintab_general_config)
        self.item_searching.setObjectName(u"item_searching")
        self.item_searching.setGeometry(QRect(20, 130, 141, 41))
        self.item_searching.setFont(font2)
        self.item_searching.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.item_searching.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.item_search_mode = QComboBox(self.maintab_general_config)
        self.item_search_mode.addItem("")
        self.item_search_mode.addItem("")
        self.item_search_mode.setObjectName(u"item_search_mode")
        self.item_search_mode.setGeometry(QRect(170, 130, 121, 41))
        self.item_search_mode.setFont(font3)
        self.item_search_mode.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.item_search_mode.setInsertPolicy(QComboBox.InsertAtBottom)
        self.lb_AdcanvedOptions_50 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_50.setObjectName(u"lb_AdcanvedOptions_50")
        self.lb_AdcanvedOptions_50.setGeometry(QRect(20, 470, 271, 21))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Variable Display Light"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setKerning(False)
        self.lb_AdcanvedOptions_50.setFont(font4)
        self.lb_AdcanvedOptions_50.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.lb_AdcanvedOptions_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_44 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_44.setObjectName(u"lb_AdcanvedOptions_44")
        self.lb_AdcanvedOptions_44.setGeometry(QRect(110, 510, 21, 31))
        self.lb_AdcanvedOptions_44.setFont(font4)
        self.lb_AdcanvedOptions_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_25 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_25.setObjectName(u"lb_AdcanvedOptions_25")
        self.lb_AdcanvedOptions_25.setGeometry(QRect(63, 510, 30, 31))
        self.lb_AdcanvedOptions_25.setFont(font4)
        self.lb_AdcanvedOptions_25.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.lb_AdcanvedOptions_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mouse_speed = QSlider(self.maintab_general_config)
        self.mouse_speed.setObjectName(u"mouse_speed")
        self.mouse_speed.setGeometry(QRect(18, 490, 251, 22))
        self.mouse_speed.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.mouse_speed.setMinimum(1)
        self.mouse_speed.setMaximum(6)
        self.mouse_speed.setSingleStep(1)
        self.mouse_speed.setPageStep(1)
        self.mouse_speed.setValue(1)
        self.mouse_speed.setSliderPosition(1)
        self.mouse_speed.setTracking(True)
        self.mouse_speed.setOrientation(Qt.Horizontal)
        self.mouse_speed.setInvertedAppearance(False)
        self.mouse_speed.setInvertedControls(False)
        self.mouse_speed.setTickPosition(QSlider.TicksBelow)
        self.mouse_speed.setTickInterval(1)
        self.lb_AdcanvedOptions_53 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_53.setObjectName(u"lb_AdcanvedOptions_53")
        self.lb_AdcanvedOptions_53.setGeometry(QRect(160, 510, 20, 31))
        self.lb_AdcanvedOptions_53.setFont(font4)
        self.lb_AdcanvedOptions_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_54 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_54.setObjectName(u"lb_AdcanvedOptions_54")
        self.lb_AdcanvedOptions_54.setGeometry(QRect(206, 510, 31, 31))
        self.lb_AdcanvedOptions_54.setFont(font4)
        self.lb_AdcanvedOptions_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_26 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_26.setObjectName(u"lb_AdcanvedOptions_26")
        self.lb_AdcanvedOptions_26.setGeometry(QRect(19, 510, 20, 31))
        self.lb_AdcanvedOptions_26.setFont(font4)
        self.lb_AdcanvedOptions_26.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.lb_AdcanvedOptions_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_4 = QFrame(self.maintab_general_config)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(340, 150, 371, 101))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(35, 35, 40, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.frame_4.setPalette(palette)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.label_123 = QLabel(self.frame_4)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(0, -10, 741, 51))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(False)
        self.label_123.setFont(font5)
        self.label_123.setWordWrap(True)
        self.label_175 = QLabel(self.frame_4)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setGeometry(QRect(0, 70, 721, 41))
        self.label_175.setFont(font5)
        self.label_175.setWordWrap(True)
        self.label_124 = QLabel(self.frame_4)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(0, 24, 741, 51))
        self.label_124.setFont(font5)
        self.label_124.setWordWrap(True)
        self.label_123.raise_()
        self.label_124.raise_()
        self.label_175.raise_()
        self.at_on_events = QCheckBox(self.maintab_general_config)
        self.at_on_events.setObjectName(u"at_on_events")
        self.at_on_events.setGeometry(QRect(340, 70, 301, 21))
        self.at_on_events.setFont(font2)
        self.lb_AdcanvedOptions_16 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_16.setObjectName(u"lb_AdcanvedOptions_16")
        self.lb_AdcanvedOptions_16.setGeometry(QRect(340, 114, 131, 21))
        self.lb_AdcanvedOptions_16.setFont(font2)
        self.lb_AdcanvedOptions_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.discord_id = QTextEdit(self.maintab_general_config)
        self.discord_id.setObjectName(u"discord_id")
        self.discord_id.setGeometry(QRect(470, 110, 171, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Variable Display Light"])
        font6.setPointSize(13)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        font6.setKerning(False)
        self.discord_id.setFont(font6)
        self.discord_id.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: white;\n"
"}\n"
"")
        self.discord_id.setInputMethodHints(Qt.ImhNone)
        self.discord_id.setFrameShape(QFrame.StyledPanel)
        self.discord_id.setFrameShadow(QFrame.Sunken)
        self.discord_id.setLineWidth(1)
        self.discord_id.setMidLineWidth(0)
        self.discord_id.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.discord_id.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.discord_id.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.discord_id.setAutoFormatting(QTextEdit.AutoBulletList)
        self.discord_id.setLineWrapMode(QTextEdit.NoWrap)
        self.discord_id.setAcceptRichText(False)
        self.test_discord_id_2 = QPushButton(self.maintab_general_config)
        self.test_discord_id_2.setObjectName(u"test_discord_id_2")
        self.test_discord_id_2.setGeometry(QRect(650, 110, 51, 31))
        self.test_discord_id_2.setFont(font3)
        self.test_discord_id_2.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgb(100,30,30);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}")
        self.lb_AdcanvedOptions_6 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_6.setObjectName(u"lb_AdcanvedOptions_6")
        self.lb_AdcanvedOptions_6.setGeometry(QRect(340, 300, 101, 21))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Variable Display Light"])
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        font7.setKerning(False)
        self.lb_AdcanvedOptions_6.setFont(font7)
        self.lb_AdcanvedOptions_6.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.lb_AdcanvedOptions_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.discord_webhook = QTextEdit(self.maintab_general_config)
        self.discord_webhook.setObjectName(u"discord_webhook")
        self.discord_webhook.setGeometry(QRect(340, 330, 331, 31))
        self.discord_webhook.setFont(font6)
        self.discord_webhook.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"\n"
"}\n"
"")
        self.discord_webhook.setInputMethodHints(Qt.ImhNone)
        self.discord_webhook.setFrameShape(QFrame.StyledPanel)
        self.discord_webhook.setFrameShadow(QFrame.Sunken)
        self.discord_webhook.setLineWidth(1)
        self.discord_webhook.setMidLineWidth(0)
        self.discord_webhook.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.discord_webhook.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.discord_webhook.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.discord_webhook.setAutoFormatting(QTextEdit.AutoBulletList)
        self.discord_webhook.setLineWrapMode(QTextEdit.NoWrap)
        self.discord_webhook.setAcceptRichText(False)
        self.discord_webhook_valid = QPushButton(self.maintab_general_config)
        self.discord_webhook_valid.setObjectName(u"discord_webhook_valid")
        self.discord_webhook_valid.setGeometry(QRect(340, 370, 91, 30))
        self.discord_webhook_valid.setFont(font3)
        self.discord_webhook_valid.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgb(100,30,30);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(30,30,30);\n"
"}")
        self.discord_webhook_status = QLabel(self.maintab_general_config)
        self.discord_webhook_status.setObjectName(u"discord_webhook_status")
        self.discord_webhook_status.setGeometry(QRect(440, 370, 181, 31))
        self.discord_webhook_status.setFont(font7)
        self.discord_webhook_status.setStyleSheet(u"color: rgb(255, 0, 4)")
        self.frame_5 = QFrame(self.maintab_general_config)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(330, 410, 401, 131))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.frame_5.setPalette(palette1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.label_126 = QLabel(self.frame_5)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(10, 0, 741, 51))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setKerning(False)
        self.label_126.setFont(font8)
        self.label_176 = QLabel(self.frame_5)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setGeometry(QRect(10, 80, 721, 51))
        self.label_176.setFont(font8)
        self.label_127 = QLabel(self.frame_5)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(10, 40, 741, 51))
        self.label_127.setFont(font8)
        self.post_to_discord = QCheckBox(self.maintab_general_config)
        self.post_to_discord.setObjectName(u"post_to_discord")
        self.post_to_discord.setGeometry(QRect(170, 310, 141, 21))
        self.post_to_discord.setFont(font2)
        self.post_to_discord.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.label_7 = QLabel(self.maintab_general_config)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 721, 561))
        self.label_7.setStyleSheet(u"QLabel{\n"
"\n"
"background-color: rgb(35,35,40)\n"
"}")
        self.label_8 = QLabel(self.maintab_general_config)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 701, 51))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(27)
        self.label_8.setFont(font9)
        self.label_8.setStyleSheet(u"\n"
"\n"
"background-color: rgb(35,35,40)")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.lb_AdcanvedOptions_55 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_55.setObjectName(u"lb_AdcanvedOptions_55")
        self.lb_AdcanvedOptions_55.setGeometry(QRect(260, 510, 31, 31))
        self.lb_AdcanvedOptions_55.setFont(font4)
        self.lb_AdcanvedOptions_55.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mouse_speed_2 = QSlider(self.maintab_general_config)
        self.mouse_speed_2.setObjectName(u"mouse_speed_2")
        self.mouse_speed_2.setGeometry(QRect(19, 420, 251, 22))
        self.mouse_speed_2.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.mouse_speed_2.setMinimum(1)
        self.mouse_speed_2.setMaximum(6)
        self.mouse_speed_2.setSingleStep(1)
        self.mouse_speed_2.setPageStep(1)
        self.mouse_speed_2.setValue(1)
        self.mouse_speed_2.setSliderPosition(1)
        self.mouse_speed_2.setTracking(True)
        self.mouse_speed_2.setOrientation(Qt.Horizontal)
        self.mouse_speed_2.setInvertedAppearance(False)
        self.mouse_speed_2.setInvertedControls(False)
        self.mouse_speed_2.setTickPosition(QSlider.TicksBelow)
        self.mouse_speed_2.setTickInterval(1)
        self.lb_AdcanvedOptions_27 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_27.setObjectName(u"lb_AdcanvedOptions_27")
        self.lb_AdcanvedOptions_27.setGeometry(QRect(64, 440, 30, 31))
        self.lb_AdcanvedOptions_27.setFont(font4)
        self.lb_AdcanvedOptions_27.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.lb_AdcanvedOptions_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_56 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_56.setObjectName(u"lb_AdcanvedOptions_56")
        self.lb_AdcanvedOptions_56.setGeometry(QRect(161, 440, 20, 31))
        self.lb_AdcanvedOptions_56.setFont(font4)
        self.lb_AdcanvedOptions_56.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_57 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_57.setObjectName(u"lb_AdcanvedOptions_57")
        self.lb_AdcanvedOptions_57.setGeometry(QRect(207, 440, 31, 31))
        self.lb_AdcanvedOptions_57.setFont(font4)
        self.lb_AdcanvedOptions_57.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_45 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_45.setObjectName(u"lb_AdcanvedOptions_45")
        self.lb_AdcanvedOptions_45.setGeometry(QRect(111, 440, 21, 31))
        self.lb_AdcanvedOptions_45.setFont(font4)
        self.lb_AdcanvedOptions_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_51 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_51.setObjectName(u"lb_AdcanvedOptions_51")
        self.lb_AdcanvedOptions_51.setGeometry(QRect(21, 400, 271, 21))
        self.lb_AdcanvedOptions_51.setFont(font4)
        self.lb_AdcanvedOptions_51.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.lb_AdcanvedOptions_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_58 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_58.setObjectName(u"lb_AdcanvedOptions_58")
        self.lb_AdcanvedOptions_58.setGeometry(QRect(261, 440, 31, 31))
        self.lb_AdcanvedOptions_58.setFont(font4)
        self.lb_AdcanvedOptions_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_AdcanvedOptions_28 = QLabel(self.maintab_general_config)
        self.lb_AdcanvedOptions_28.setObjectName(u"lb_AdcanvedOptions_28")
        self.lb_AdcanvedOptions_28.setGeometry(QRect(20, 440, 20, 31))
        self.lb_AdcanvedOptions_28.setFont(font4)
        self.lb_AdcanvedOptions_28.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.lb_AdcanvedOptions_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.main_tab.addTab(self.maintab_general_config, "")
        self.label_7.raise_()
        self.use_wishlist_tab.raise_()
        self.mouse_movements.raise_()
        self.mouse_movement_mode.raise_()
        self.label_61.raise_()
        self.label_78.raise_()
        self.allowed_inv_slots.raise_()
        self.inventory_allowed_slots.raise_()
        self.inventory_empty_at_slots.raise_()
        self.empty_inv_at.raise_()
        self.item_searching.raise_()
        self.item_search_mode.raise_()
        self.lb_AdcanvedOptions_50.raise_()
        self.lb_AdcanvedOptions_44.raise_()
        self.lb_AdcanvedOptions_25.raise_()
        self.mouse_speed.raise_()
        self.lb_AdcanvedOptions_53.raise_()
        self.lb_AdcanvedOptions_54.raise_()
        self.lb_AdcanvedOptions_26.raise_()
        self.frame_4.raise_()
        self.at_on_events.raise_()
        self.lb_AdcanvedOptions_16.raise_()
        self.discord_id.raise_()
        self.test_discord_id_2.raise_()
        self.lb_AdcanvedOptions_6.raise_()
        self.discord_webhook.raise_()
        self.discord_webhook_valid.raise_()
        self.discord_webhook_status.raise_()
        self.frame_5.raise_()
        self.post_to_discord.raise_()
        self.label_8.raise_()
        self.lb_AdcanvedOptions_55.raise_()
        self.mouse_speed_2.raise_()
        self.lb_AdcanvedOptions_27.raise_()
        self.lb_AdcanvedOptions_56.raise_()
        self.lb_AdcanvedOptions_57.raise_()
        self.lb_AdcanvedOptions_45.raise_()
        self.lb_AdcanvedOptions_51.raise_()
        self.lb_AdcanvedOptions_58.raise_()
        self.lb_AdcanvedOptions_28.raise_()
        self.maintab_license = QWidget()
        self.maintab_license.setObjectName(u"maintab_license")
        self.label_6 = QLabel(self.maintab_license)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 90, 151, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_6.setPalette(palette2)
        font10 = QFont()
        font10.setPointSize(12)
        self.label_6.setFont(font10)
        self.label_6.setStyleSheet(u"")
        self.label_6.setLineWidth(1)
        self.label_84 = QLabel(self.maintab_license)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(10, 150, 151, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_84.setPalette(palette3)
        self.label_84.setFont(font10)
        self.label_84.setStyleSheet(u"")
        self.label_84.setLineWidth(1)
        self.subscription_type = QLabel(self.maintab_license)
        self.subscription_type.setObjectName(u"subscription_type")
        self.subscription_type.setGeometry(QRect(170, 90, 71, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.subscription_type.setPalette(palette4)
        self.subscription_type.setFont(font10)
        self.subscription_type.setStyleSheet(u"")
        self.subscription_type.setLineWidth(1)
        self.registered_devices = QLabel(self.maintab_license)
        self.registered_devices.setObjectName(u"registered_devices")
        self.registered_devices.setGeometry(QRect(170, 150, 71, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.registered_devices.setPalette(palette5)
        self.registered_devices.setFont(font10)
        self.registered_devices.setStyleSheet(u"")
        self.registered_devices.setLineWidth(1)
        self.label_85 = QLabel(self.maintab_license)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(10, 30, 151, 31))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_85.setPalette(palette6)
        self.label_85.setFont(font10)
        self.label_85.setStyleSheet(u"")
        self.label_85.setLineWidth(1)
        self.registered_name = QLabel(self.maintab_license)
        self.registered_name.setObjectName(u"registered_name")
        self.registered_name.setGeometry(QRect(170, 30, 121, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.registered_name.setPalette(palette7)
        self.registered_name.setFont(font10)
        self.registered_name.setStyleSheet(u"")
        self.registered_name.setLineWidth(1)
        self.registered_name.setScaledContents(False)
        self.label_86 = QLabel(self.maintab_license)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(10, 210, 151, 31))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_86.setPalette(palette8)
        self.label_86.setFont(font10)
        self.label_86.setStyleSheet(u"")
        self.label_86.setLineWidth(1)
        self.first_logged_in = QLabel(self.maintab_license)
        self.first_logged_in.setObjectName(u"first_logged_in")
        self.first_logged_in.setGeometry(QRect(170, 210, 121, 31))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.first_logged_in.setPalette(palette9)
        self.first_logged_in.setFont(font10)
        self.first_logged_in.setStyleSheet(u"")
        self.first_logged_in.setLineWidth(1)
        self.label_87 = QLabel(self.maintab_license)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(300, 16, 361, 61))
        self.label_87.setWordWrap(True)
        self.label_88 = QLabel(self.maintab_license)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(300, 85, 361, 41))
        self.label_88.setWordWrap(True)
        self.label_89 = QLabel(self.maintab_license)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(300, 146, 361, 41))
        self.label_89.setWordWrap(True)
        self.label_90 = QLabel(self.maintab_license)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(300, 207, 361, 41))
        self.label_90.setWordWrap(True)
        self.label_91 = QLabel(self.maintab_license)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(10, 270, 151, 31))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_91.setPalette(palette10)
        self.label_91.setFont(font10)
        self.label_91.setStyleSheet(u"")
        self.label_91.setLineWidth(1)
        self.license_expires = QLabel(self.maintab_license)
        self.license_expires.setObjectName(u"license_expires")
        self.license_expires.setGeometry(QRect(170, 270, 121, 31))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.license_expires.setPalette(palette11)
        self.license_expires.setFont(font10)
        self.license_expires.setStyleSheet(u"")
        self.license_expires.setLineWidth(1)
        self.label_93 = QLabel(self.maintab_license)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(300, 262, 361, 41))
        self.label_93.setWordWrap(True)
        self.label_117 = QLabel(self.maintab_license)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(10, 330, 721, 71))
        self.label_117.setFont(font5)
        self.label_117.setWordWrap(True)
        self.label_118 = QLabel(self.maintab_license)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(10, 400, 741, 21))
        self.label_118.setFont(font5)
        self.label_118.setWordWrap(True)
        self.label_119 = QLabel(self.maintab_license)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(10, 430, 741, 51))
        self.label_119.setFont(font5)
        self.label_119.setWordWrap(True)
        self.label_120 = QLabel(self.maintab_license)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(10, 490, 731, 41))
        self.label_120.setFont(font5)
        self.label_120.setWordWrap(True)
        self.main_tab.addTab(self.maintab_license, "")
        self.maintab_database = QWidget()
        self.maintab_database.setObjectName(u"maintab_database")
        self.maintab_database.setFont(font10)
        self.select_item = QLabel(self.maintab_database)
        self.select_item.setObjectName(u"select_item")
        self.select_item.setGeometry(QRect(20, 59, 71, 41))
        self.select_item.setFont(font6)
        self.select_item.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.select_item.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.current_item = QComboBox(self.maintab_database)
        self.current_item.setObjectName(u"current_item")
        self.current_item.setGeometry(QRect(110, 55, 211, 50))
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setPointSize(11)
        self.current_item.setFont(font11)
        self.current_item.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.current_item.setLayoutDirection(Qt.LeftToRight)
        self.current_item.setAutoFillBackground(False)
        self.current_item.setStyleSheet(u"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"")
        self.current_item.setInputMethodHints(Qt.ImhNone)
        self.current_item.setEditable(False)
        self.current_item.setMaxVisibleItems(12)
        self.current_item.setInsertPolicy(QComboBox.InsertAtBottom)
        self.current_item.setDuplicatesEnabled(False)
        self.delete_item = QPushButton(self.maintab_database)
        self.delete_item.setObjectName(u"delete_item")
        self.delete_item.setGeometry(QRect(590, 60, 91, 41))
        font12 = QFont()
        font12.setPointSize(10)
        self.delete_item.setFont(font12)
        self.delete_item.setCursor(QCursor(Qt.ArrowCursor))
        self.delete_item.setMouseTracking(False)
        self.delete_item.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgb(141,124,102);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(118,111,102);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(25,25,25);\n"
"	color: rgb(255,0,0);\n"
"}")
        self.add_item = QPushButton(self.maintab_database)
        self.add_item.setObjectName(u"add_item")
        self.add_item.setGeometry(QRect(470, 60, 91, 41))
        self.add_item.setFont(font12)
        self.add_item.setCursor(QCursor(Qt.ArrowCursor))
        self.add_item.setMouseTracking(False)
        self.add_item.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgb(141,124,102);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(118,111,102);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(25,25,25);\n"
"	color: rgb(0,255,0);\n"
"}")
        self.item_currency = QComboBox(self.maintab_database)
        self.item_currency.addItem("")
        self.item_currency.addItem("")
        self.item_currency.addItem("")
        self.item_currency.setObjectName(u"item_currency")
        self.item_currency.setGeometry(QRect(150, 205, 71, 41))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.item_currency.setPalette(palette12)
        self.item_currency.setFont(font3)
        self.item_currency.setStyleSheet(u"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255,0,0);\n"
"}\n"
"\n"
"")
        self.item_currency.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.item_currency.setIconSize(QSize(18, 18))
        self.select_vendor = QLabel(self.maintab_database)
        self.select_vendor.setObjectName(u"select_vendor")
        self.select_vendor.setGeometry(QRect(253, 205, 91, 41))
        self.select_vendor.setFont(font6)
        self.select_vendor.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.select_vendor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.select_currency = QLabel(self.maintab_database)
        self.select_currency.setObjectName(u"select_currency")
        self.select_currency.setGeometry(QRect(20, 205, 91, 41))
        self.select_currency.setFont(font6)
        self.select_currency.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.select_currency.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.item_vendor = QComboBox(self.maintab_database)
        self.item_vendor.addItem("")
        self.item_vendor.addItem("")
        self.item_vendor.setObjectName(u"item_vendor")
        self.item_vendor.setGeometry(QRect(360, 205, 101, 41))
        self.item_vendor.setFont(font3)
        self.item_vendor.setStyleSheet(u"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255,0,0);\n"
"}\n"
"\n"
"")
        self.item_refreshes = QSpinBox(self.maintab_database)
        self.item_refreshes.setObjectName(u"item_refreshes")
        self.item_refreshes.setGeometry(QRect(150, 280, 71, 21))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI Variable Display Light"])
        font13.setPointSize(13)
        self.item_refreshes.setFont(font13)
        self.item_refreshes.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(255,255,255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"")
        self.item_refreshes.setMaximum(120)
        self.set_item_refreshes = QLabel(self.maintab_database)
        self.set_item_refreshes.setObjectName(u"set_item_refreshes")
        self.set_item_refreshes.setGeometry(QRect(20, 280, 91, 21))
        self.set_item_refreshes.setFont(font6)
        self.set_item_refreshes.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.set_item_refreshes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.item_value = QTextEdit(self.maintab_database)
        self.item_value.setObjectName(u"item_value")
        self.item_value.setGeometry(QRect(110, 141, 111, 31))
        font14 = QFont()
        font14.setFamilies([u"Segoe UI Variable Display Light"])
        font14.setPointSize(16)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setUnderline(False)
        font14.setStrikeOut(False)
        font14.setKerning(False)
        self.item_value.setFont(font14)
        self.item_value.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_value.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_value.setLineWidth(1)
        self.item_value.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_value.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_value.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_value.setAutoFormatting(QTextEdit.AutoNone)
        self.item_value.setLineWrapMode(QTextEdit.NoWrap)
        self.set_item_value = QLabel(self.maintab_database)
        self.set_item_value.setObjectName(u"set_item_value")
        self.set_item_value.setGeometry(QRect(20, 135, 91, 41))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value.setPalette(palette13)
        font15 = QFont()
        font15.setPointSize(13)
        self.set_item_value.setFont(font15)
        self.set_item_value.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_max_price = QTextEdit(self.maintab_database)
        self.item_max_price.setObjectName(u"item_max_price")
        self.item_max_price.setGeometry(QRect(350, 141, 111, 31))
        self.item_max_price.setFont(font14)
        self.item_max_price.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_max_price.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_max_price.setLineWidth(1)
        self.item_max_price.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_max_price.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_max_price.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_max_price.setAutoFormatting(QTextEdit.AutoNone)
        self.item_max_price.setLineWrapMode(QTextEdit.NoWrap)
        self.set_item_price = QLabel(self.maintab_database)
        self.set_item_price.setObjectName(u"set_item_price")
        self.set_item_price.setGeometry(QRect(250, 135, 91, 41))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_price.setPalette(palette14)
        self.set_item_price.setFont(font15)
        self.set_item_price.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.set_item_value_2 = QLabel(self.maintab_database)
        self.set_item_value_2.setObjectName(u"set_item_value_2")
        self.set_item_value_2.setGeometry(QRect(490, 135, 91, 41))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_2.setPalette(palette15)
        self.set_item_value_2.setFont(font15)
        self.set_item_value_2.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_profit = QTextEdit(self.maintab_database)
        self.item_profit.setObjectName(u"item_profit")
        self.item_profit.setGeometry(QRect(590, 141, 111, 31))
        self.item_profit.setFont(font14)
        self.item_profit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(0,255,0);\n"
"}\n"
"")
        self.item_profit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_profit.setLineWidth(1)
        self.item_profit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_profit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_profit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_profit.setAutoFormatting(QTextEdit.AutoNone)
        self.item_profit.setLineWrapMode(QTextEdit.NoWrap)
        self.select_vendor_2 = QLabel(self.maintab_database)
        self.select_vendor_2.setObjectName(u"select_vendor_2")
        self.select_vendor_2.setGeometry(QRect(490, 205, 91, 41))
        self.select_vendor_2.setFont(font6)
        self.select_vendor_2.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.select_vendor_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.item_size = QComboBox(self.maintab_database)
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.addItem("")
        self.item_size.setObjectName(u"item_size")
        self.item_size.setGeometry(QRect(620, 205, 81, 41))
        self.item_size.setFont(font3)
        self.item_size.setStyleSheet(u"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255,0,0);\n"
"}\n"
"\n"
"")
        self.label_2 = QLabel(self.maintab_database)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 30, 721, 281))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"background-color: rgb(35,35,40)\n"
"}")
        self.label_3 = QLabel(self.maintab_database)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 721, 51))
        self.label_3.setFont(font9)
        self.label_3.setStyleSheet(u"\n"
"\n"
"background-color: rgb(35,35,40)")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.maintab_database)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 350, 721, 201))
        self.label_4.setStyleSheet(u"QLabel{\n"
"background-color: rgb(35,35,40)\n"
"\n"
"}")
        self.set_item_value_3 = QLabel(self.maintab_database)
        self.set_item_value_3.setObjectName(u"set_item_value_3")
        self.set_item_value_3.setGeometry(QRect(20, 380, 81, 41))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_3.setPalette(palette16)
        self.set_item_value_3.setFont(font15)
        self.set_item_value_3.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_stats_searched = QTextEdit(self.maintab_database)
        self.item_stats_searched.setObjectName(u"item_stats_searched")
        self.item_stats_searched.setGeometry(QRect(110, 385, 121, 31))
        self.item_stats_searched.setFont(font14)
        self.item_stats_searched.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_searched.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_searched.setLineWidth(1)
        self.item_stats_searched.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_searched.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_searched.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_searched.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_searched.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_searched.setReadOnly(True)
        self.item_stats_found = QTextEdit(self.maintab_database)
        self.item_stats_found.setObjectName(u"item_stats_found")
        self.item_stats_found.setGeometry(QRect(340, 385, 131, 31))
        self.item_stats_found.setFont(font14)
        self.item_stats_found.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_found.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_found.setLineWidth(1)
        self.item_stats_found.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_found.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_found.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_found.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_found.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_found.setReadOnly(True)
        self.set_item_value_4 = QLabel(self.maintab_database)
        self.set_item_value_4.setObjectName(u"set_item_value_4")
        self.set_item_value_4.setGeometry(QRect(250, 380, 81, 41))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_4.setPalette(palette17)
        self.set_item_value_4.setFont(font15)
        self.set_item_value_4.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_stats_bought = QTextEdit(self.maintab_database)
        self.item_stats_bought.setObjectName(u"item_stats_bought")
        self.item_stats_bought.setGeometry(QRect(340, 440, 131, 31))
        self.item_stats_bought.setFont(font14)
        self.item_stats_bought.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_bought.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_bought.setLineWidth(1)
        self.item_stats_bought.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_bought.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_bought.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_bought.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_bought.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_bought.setReadOnly(True)
        self.set_item_value_5 = QLabel(self.maintab_database)
        self.set_item_value_5.setObjectName(u"set_item_value_5")
        self.set_item_value_5.setGeometry(QRect(250, 435, 81, 41))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_5.setPalette(palette18)
        self.set_item_value_5.setFont(font15)
        self.set_item_value_5.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_stats_avg_profit = QTextEdit(self.maintab_database)
        self.item_stats_avg_profit.setObjectName(u"item_stats_avg_profit")
        self.item_stats_avg_profit.setGeometry(QRect(580, 440, 101, 31))
        self.item_stats_avg_profit.setFont(font14)
        self.item_stats_avg_profit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_avg_profit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_avg_profit.setLineWidth(1)
        self.item_stats_avg_profit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_avg_profit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_avg_profit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_avg_profit.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_avg_profit.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_avg_profit.setReadOnly(True)
        self.set_item_value_6 = QLabel(self.maintab_database)
        self.set_item_value_6.setObjectName(u"set_item_value_6")
        self.set_item_value_6.setGeometry(QRect(490, 435, 81, 41))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_6.setPalette(palette19)
        self.set_item_value_6.setFont(font15)
        self.set_item_value_6.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_stats_total_profit = QTextEdit(self.maintab_database)
        self.item_stats_total_profit.setObjectName(u"item_stats_total_profit")
        self.item_stats_total_profit.setGeometry(QRect(110, 440, 121, 31))
        self.item_stats_total_profit.setFont(font14)
        self.item_stats_total_profit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_total_profit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_total_profit.setLineWidth(1)
        self.item_stats_total_profit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_total_profit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_total_profit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_total_profit.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_total_profit.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_total_profit.setReadOnly(True)
        self.set_item_value_7 = QLabel(self.maintab_database)
        self.set_item_value_7.setObjectName(u"set_item_value_7")
        self.set_item_value_7.setGeometry(QRect(20, 435, 91, 41))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_7.setPalette(palette20)
        self.set_item_value_7.setFont(font15)
        self.set_item_value_7.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_stats_rank = QTextEdit(self.maintab_database)
        self.item_stats_rank.setObjectName(u"item_stats_rank")
        self.item_stats_rank.setGeometry(QRect(110, 495, 121, 31))
        self.item_stats_rank.setFont(font14)
        self.item_stats_rank.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_rank.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_rank.setLineWidth(1)
        self.item_stats_rank.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_rank.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_rank.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_rank.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_rank.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_rank.setReadOnly(True)
        self.item_stats_rank.setPlaceholderText(u"#1")
        self.set_item_value_8 = QLabel(self.maintab_database)
        self.set_item_value_8.setObjectName(u"set_item_value_8")
        self.set_item_value_8.setGeometry(QRect(20, 490, 81, 41))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_8.setPalette(palette21)
        self.set_item_value_8.setFont(font15)
        self.set_item_value_8.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_enabled = QCheckBox(self.maintab_database)
        self.item_enabled.setObjectName(u"item_enabled")
        self.item_enabled.setGeometry(QRect(370, 60, 91, 41))
        self.item_enabled.setFont(font12)
        self.item_enabled.setStyleSheet(u"background-color: rgb(35,35,40)\n"
"")
        self.label_5 = QLabel(self.maintab_database)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 310, 721, 51))
        self.label_5.setFont(font9)
        self.label_5.setStyleSheet(u"\n"
"\n"
"background-color: rgb(35,35,40)")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.item_stats_rarity = QTextEdit(self.maintab_database)
        self.item_stats_rarity.setObjectName(u"item_stats_rarity")
        self.item_stats_rarity.setGeometry(QRect(580, 385, 101, 31))
        self.item_stats_rarity.setFont(font14)
        self.item_stats_rarity.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_rarity.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_rarity.setLineWidth(1)
        self.item_stats_rarity.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_rarity.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_rarity.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_rarity.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_rarity.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_rarity.setReadOnly(True)
        self.set_item_value_9 = QLabel(self.maintab_database)
        self.set_item_value_9.setObjectName(u"set_item_value_9")
        self.set_item_value_9.setGeometry(QRect(490, 380, 81, 41))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_9.setPalette(palette22)
        self.set_item_value_9.setFont(font15)
        self.set_item_value_9.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_stats_efficiency = QTextEdit(self.maintab_database)
        self.item_stats_efficiency.setObjectName(u"item_stats_efficiency")
        self.item_stats_efficiency.setGeometry(QRect(340, 495, 131, 31))
        self.item_stats_efficiency.setFont(font14)
        self.item_stats_efficiency.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_stats_efficiency.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_stats_efficiency.setLineWidth(1)
        self.item_stats_efficiency.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_efficiency.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_stats_efficiency.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_stats_efficiency.setAutoFormatting(QTextEdit.AutoNone)
        self.item_stats_efficiency.setLineWrapMode(QTextEdit.NoWrap)
        self.item_stats_efficiency.setReadOnly(True)
        self.set_item_value_10 = QLabel(self.maintab_database)
        self.set_item_value_10.setObjectName(u"set_item_value_10")
        self.set_item_value_10.setGeometry(QRect(250, 490, 81, 41))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_10.setPalette(palette23)
        self.set_item_value_10.setFont(font15)
        self.set_item_value_10.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.item_image_path = QTextEdit(self.maintab_database)
        self.item_image_path.setObjectName(u"item_image_path")
        self.item_image_path.setGeometry(QRect(590, 274, 81, 31))
        font16 = QFont()
        font16.setFamilies([u"Segoe UI Variable Display Light"])
        font16.setPointSize(15)
        font16.setBold(False)
        font16.setItalic(False)
        font16.setUnderline(False)
        font16.setStrikeOut(False)
        font16.setKerning(False)
        self.item_image_path.setFont(font16)
        self.item_image_path.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(30,30,40);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.item_image_path.setInputMethodHints(Qt.ImhDigitsOnly)
        self.item_image_path.setLineWidth(1)
        self.item_image_path.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_image_path.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_image_path.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.item_image_path.setAutoFormatting(QTextEdit.AutoNone)
        self.item_image_path.setLineWrapMode(QTextEdit.NoWrap)
        self.item_image_path.setReadOnly(True)
        self.set_item_value_11 = QLabel(self.maintab_database)
        self.set_item_value_11.setObjectName(u"set_item_value_11")
        self.set_item_value_11.setGeometry(QRect(490, 268, 101, 41))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.set_item_value_11.setPalette(palette24)
        self.set_item_value_11.setFont(font15)
        self.set_item_value_11.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.add_image = QPushButton(self.maintab_database)
        self.add_image.setObjectName(u"add_image")
        self.add_image.setGeometry(QRect(670, 274, 31, 31))
        self.add_image.setFont(font12)
        self.add_image.setCursor(QCursor(Qt.ArrowCursor))
        self.add_image.setMouseTracking(False)
        self.add_image.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgb(141,124,102);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(118,111,102);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(25,25,25);\n"
"	color: rgb(0,255,0);\n"
"}")
        self.amount_label = QLabel(self.maintab_database)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(250, 280, 91, 21))
        self.amount_label.setFont(font6)
        self.amount_label.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color: rgb(35,35,40)")
        self.amount_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.item_buy_amount = QSpinBox(self.maintab_database)
        self.item_buy_amount.setObjectName(u"item_buy_amount")
        self.item_buy_amount.setGeometry(QRect(380, 280, 71, 21))
        self.item_buy_amount.setFont(font13)
        self.item_buy_amount.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(255,255,255);\n"
"background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"")
        self.item_buy_amount.setMaximum(120)
        self.reset_item_stats = QPushButton(self.maintab_database)
        self.reset_item_stats.setObjectName(u"reset_item_stats")
        self.reset_item_stats.setGeometry(QRect(490, 490, 91, 41))
        self.reset_item_stats.setFont(font12)
        self.reset_item_stats.setCursor(QCursor(Qt.ArrowCursor))
        self.reset_item_stats.setMouseTracking(False)
        self.reset_item_stats.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgb(141,124,102);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(118,111,102);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(25,25,25);\n"
"	color: rgb(255,0,0);\n"
"}")
        self.reset_all_items_stats = QPushButton(self.maintab_database)
        self.reset_all_items_stats.setObjectName(u"reset_all_items_stats")
        self.reset_all_items_stats.setGeometry(QRect(600, 490, 91, 41))
        self.reset_all_items_stats.setFont(font12)
        self.reset_all_items_stats.setCursor(QCursor(Qt.ArrowCursor))
        self.reset_all_items_stats.setMouseTracking(False)
        self.reset_all_items_stats.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgb(141,124,102);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(118,111,102);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(25,25,25);\n"
"	color: rgb(255,0,0);\n"
"}")
        self.main_tab.addTab(self.maintab_database, "")
        self.label_2.raise_()
        self.select_item.raise_()
        self.current_item.raise_()
        self.delete_item.raise_()
        self.add_item.raise_()
        self.item_currency.raise_()
        self.select_vendor.raise_()
        self.select_currency.raise_()
        self.item_vendor.raise_()
        self.item_refreshes.raise_()
        self.set_item_refreshes.raise_()
        self.item_value.raise_()
        self.set_item_value.raise_()
        self.item_max_price.raise_()
        self.set_item_price.raise_()
        self.set_item_value_2.raise_()
        self.item_profit.raise_()
        self.select_vendor_2.raise_()
        self.item_size.raise_()
        self.label_4.raise_()
        self.set_item_value_3.raise_()
        self.item_stats_searched.raise_()
        self.item_stats_found.raise_()
        self.set_item_value_4.raise_()
        self.item_stats_bought.raise_()
        self.set_item_value_5.raise_()
        self.item_stats_avg_profit.raise_()
        self.set_item_value_6.raise_()
        self.item_stats_total_profit.raise_()
        self.set_item_value_7.raise_()
        self.item_stats_rank.raise_()
        self.set_item_value_8.raise_()
        self.item_enabled.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.item_stats_rarity.raise_()
        self.set_item_value_9.raise_()
        self.item_stats_efficiency.raise_()
        self.set_item_value_10.raise_()
        self.item_image_path.raise_()
        self.set_item_value_11.raise_()
        self.add_image.raise_()
        self.amount_label.raise_()
        self.item_buy_amount.raise_()
        self.reset_item_stats.raise_()
        self.reset_all_items_stats.raise_()
        self.maintab_statistics = QWidget()
        self.maintab_statistics.setObjectName(u"maintab_statistics")
        self.statistics_plot = MplWidget(self.maintab_statistics)
        self.statistics_plot.setObjectName(u"statistics_plot")
        self.statistics_plot.setGeometry(QRect(20, 70, 671, 461))
        self.select_statistic = QComboBox(self.maintab_statistics)
        self.select_statistic.addItem("")
        self.select_statistic.addItem("")
        self.select_statistic.addItem("")
        self.select_statistic.addItem("")
        self.select_statistic.setObjectName(u"select_statistic")
        self.select_statistic.setGeometry(QRect(170, 20, 271, 31))
        self.select_statistic.setFont(font3)
        self.select_statistic.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(35,35,40)\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.select_statistic.setInsertPolicy(QComboBox.InsertAtBottom)
        self.mouse_movements_2 = QLabel(self.maintab_statistics)
        self.mouse_movements_2.setObjectName(u"mouse_movements_2")
        self.mouse_movements_2.setGeometry(QRect(20, 20, 141, 31))
        self.mouse_movements_2.setFont(font2)
        self.mouse_movements_2.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.mouse_movements_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.main_tab.addTab(self.maintab_statistics, "")
        self.label = QLabel(self.MainUi)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 0, 721, 621))
        self.label.setStyleSheet(u"background-color: rgb(35,35,40)")
        self.bot_status = QLabel(self.MainUi)
        self.bot_status.setObjectName(u"bot_status")
        self.bot_status.setGeometry(QRect(320, 570, 361, 41))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.bot_status.setPalette(palette25)
        self.bot_status.setFont(font10)
        self.bot_status.setStyleSheet(u"color:rgb(255,255,255)")
        self.buttons_statistics = QPushButton(self.MainUi)
        self.buttons_statistics.setObjectName(u"buttons_statistics")
        self.buttons_statistics.setGeometry(QRect(-20, 170, 271, 41))
        self.buttons_statistics.setFont(font)
        self.buttons_statistics.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-bottom-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"	color:rgba(255, 255, 255, 210);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 120), stop:1 rgba(80, 98, 112, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {          \n"
"		  background-color: rgb(255, 255,255); \n"
"          border:1px solid rgb(255, 255, 255);}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(30, 60, 60, 160), stop:1 rgba(80, 98, 112, 230));\n"
"}")
        self.buttons_statistics.setIcon(icon2)
        self.buttons_statistics.setIconSize(QSize(40, 40))
        Form.setCentralWidget(self.MainUi)
        self.label.raise_()
        self.background_left.raise_()
        self.buttons_general.raise_()
        self.buttons_database.raise_()
        self.buttons_license.raise_()
        self.main_tab.raise_()
        self.bot_status.raise_()
        self.buttons_statistics.raise_()

        self.retranslateUi(Form)

        self.main_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Night market", None))
        self.background_left.setText("")
        self.buttons_general.setText(QCoreApplication.translate("Form", u"General config", None))
        self.buttons_database.setText(QCoreApplication.translate("Form", u"Database config", None))
        self.buttons_license.setText(QCoreApplication.translate("Form", u"My license", None))
#if QT_CONFIG(tooltip)
        self.use_wishlist_tab.setToolTip(QCoreApplication.translate("Form", u"Use the wishlist tab to scrap the market instead", None))
#endif // QT_CONFIG(tooltip)
        self.use_wishlist_tab.setText(QCoreApplication.translate("Form", u"Use wishlist tab", None))
        self.mouse_movements.setText(QCoreApplication.translate("Form", u"Mouse movement:", None))
        self.mouse_movement_mode.setItemText(0, QCoreApplication.translate("Form", u"warping", None))
        self.mouse_movement_mode.setItemText(1, QCoreApplication.translate("Form", u"humanized", None))

#if QT_CONFIG(tooltip)
        self.mouse_movement_mode.setToolTip(QCoreApplication.translate("Form", u"You can either have the mouse warp or use humanized movement.\n"
"\n"
"Personally ive been letting it warp around at supersonic speed for all weeks of development\n"
"without any issues at all, and its very unlikely to even be noticed.\n"
"\n"
"Humanized will be a little bit slower but if you feel safer, its worth it.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_61.setToolTip(QCoreApplication.translate("Form", u"This is a globally shared setting and not \n"
"affected by changing your character.", None))
#endif // QT_CONFIG(tooltip)
        self.label_61.setText("")
#if QT_CONFIG(tooltip)
        self.label_78.setToolTip(QCoreApplication.translate("Form", u"This is a globally shared setting and not \n"
"affected by changing your character.", None))
#endif // QT_CONFIG(tooltip)
        self.label_78.setText("")
#if QT_CONFIG(tooltip)
        self.allowed_inv_slots.setToolTip(QCoreApplication.translate("Form", u"Determine how many times the bot is allowed to scroll (to keep items on bottom safe)", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_allowed_slots.setText(QCoreApplication.translate("Form", u"Allowed scrolls:", None))
        self.inventory_empty_at_slots.setText(QCoreApplication.translate("Form", u"Empty at inventory slots:", None))
#if QT_CONFIG(tooltip)
        self.empty_inv_at.setToolTip(QCoreApplication.translate("Form", u"Determine at how many slots you want the bot to sell, it keeps track of how much it bought.", None))
#endif // QT_CONFIG(tooltip)
        self.item_searching.setText(QCoreApplication.translate("Form", u"Item searching:", None))
        self.item_search_mode.setItemText(0, QCoreApplication.translate("Form", u"Copy & paste", None))
        self.item_search_mode.setItemText(1, QCoreApplication.translate("Form", u"Type out", None))

#if QT_CONFIG(tooltip)
        self.item_search_mode.setToolTip(QCoreApplication.translate("Form", u"When the bot searches an item name or price, you can either let it copy paste it in, or type it out.\n"
"\n"
"Unless you are actively using your clipboard while rdp session runs, \n"
"Id definitely recommend pasting it in, typing is slower.", None))
#endif // QT_CONFIG(tooltip)
        self.lb_AdcanvedOptions_50.setText(QCoreApplication.translate("Form", u"Filter speed delays:", None))
        self.lb_AdcanvedOptions_44.setText(QCoreApplication.translate("Form", u"1.4", None))
        self.lb_AdcanvedOptions_25.setText(QCoreApplication.translate("Form", u"1.2", None))
#if QT_CONFIG(tooltip)
        self.mouse_speed.setToolTip(QCoreApplication.translate("Form", u"Multiplies your delays by the value its on. a 0.3s delay will turn into 0.6s on 2x", None))
#endif // QT_CONFIG(tooltip)
        self.lb_AdcanvedOptions_53.setText(QCoreApplication.translate("Form", u"1.6", None))
        self.lb_AdcanvedOptions_54.setText(QCoreApplication.translate("Form", u"1.8", None))
        self.lb_AdcanvedOptions_26.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_123.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">1. Settings &gt; advanced &gt; enable developer mode</span></p></body></html>", None))
        self.label_175.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">3. Paste the ID into the text bar above.</span></p></body></html>", None))
        self.label_124.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">2. Right click your profile, press '</span><span style=\" color:#00aaff;\">Copy ID</span><span style=\" font-weight:600; color:#00aaff;\">'</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.at_on_events.setToolTip(QCoreApplication.translate("Form", u"Mention you on discord if the bot crashes or something of that sort", None))
#endif // QT_CONFIG(tooltip)
        self.at_on_events.setText(QCoreApplication.translate("Form", u"@ on special events", None))
        self.lb_AdcanvedOptions_16.setText(QCoreApplication.translate("Form", u"Account ID to @:", None))
#if QT_CONFIG(tooltip)
        self.discord_id.setToolTip(QCoreApplication.translate("Form", u"Your discord ID", None))
#endif // QT_CONFIG(tooltip)
        self.discord_id.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:10pt;\"><br /></p></body></html>", None))
        self.discord_id.setPlaceholderText(QCoreApplication.translate("Form", u"153933119928532992", None))
#if QT_CONFIG(tooltip)
        self.test_discord_id_2.setToolTip(QCoreApplication.translate("Form", u"Pings you", None))
#endif // QT_CONFIG(tooltip)
        self.test_discord_id_2.setText(QCoreApplication.translate("Form", u"Test", None))
        self.lb_AdcanvedOptions_6.setText(QCoreApplication.translate("Form", u"Webhook link:", None))
#if QT_CONFIG(tooltip)
        self.discord_webhook.setToolTip(QCoreApplication.translate("Form", u"Your webhook", None))
#endif // QT_CONFIG(tooltip)
        self.discord_webhook.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:10pt;\"><br /></p></body></html>", None))
        self.discord_webhook.setPlaceholderText(QCoreApplication.translate("Form", u"https://discord.com/api/webhook...", None))
#if QT_CONFIG(tooltip)
        self.discord_webhook_valid.setToolTip(QCoreApplication.translate("Form", u"Check if the webhook is valid", None))
#endif // QT_CONFIG(tooltip)
        self.discord_webhook_valid.setText(QCoreApplication.translate("Form", u"Validate", None))
        self.discord_webhook_status.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#008100;\">A weebhook is active.</span></p></body></html>", None))
        self.label_126.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">1. Right click Channel &gt; Edit &gt; Integrations &gt; Create Webhook</span></p></body></html>", None))
        self.label_176.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">3. Paste the into &quot;Webhook Link&quot; Text Field, and validate it!</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">2. Press &quot;Copy Webhook URL&quot;.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.post_to_discord.setToolTip(QCoreApplication.translate("Form", u"Post to discord at all", None))
#endif // QT_CONFIG(tooltip)
        self.post_to_discord.setText(QCoreApplication.translate("Form", u"Post to discord", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Bot configuration", None))
        self.lb_AdcanvedOptions_55.setText(QCoreApplication.translate("Form", u"2", None))
#if QT_CONFIG(tooltip)
        self.mouse_speed_2.setToolTip(QCoreApplication.translate("Form", u"Multiplies your delays by the value its on. a 0.3s delay will turn into 0.6s on 2x", None))
#endif // QT_CONFIG(tooltip)
        self.lb_AdcanvedOptions_27.setText(QCoreApplication.translate("Form", u"1.2", None))
        self.lb_AdcanvedOptions_56.setText(QCoreApplication.translate("Form", u"1.6", None))
        self.lb_AdcanvedOptions_57.setText(QCoreApplication.translate("Form", u"1.8", None))
        self.lb_AdcanvedOptions_45.setText(QCoreApplication.translate("Form", u"1.4", None))
        self.lb_AdcanvedOptions_51.setText(QCoreApplication.translate("Form", u"Sell speed delays:", None))
        self.lb_AdcanvedOptions_58.setText(QCoreApplication.translate("Form", u"2", None))
        self.lb_AdcanvedOptions_28.setText(QCoreApplication.translate("Form", u"1", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.maintab_general_config), QCoreApplication.translate("Form", u"Chaos Bot", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Subscription type:</p></body></html>", None))
        self.label_84.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Registered devices:</p></body></html>", None))
        self.subscription_type.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">Premium</span></p></body></html>", None))
        self.registered_devices.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">0/1</span></p></body></html>", None))
        self.label_85.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Registered name:</p></body></html>", None))
        self.registered_name.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">name</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>First logged in:</p></body></html>", None))
        self.first_logged_in.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">date</span></p></body></html>", None))
        self.label_87.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">Most likely your discord name, if they are incorrect or missing and you would like to correct that please message the support. Nothing will happen if they arent correct though.</span></p></body></html>", None))
        self.label_88.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">Your current subscription, if this is incorrect please do contact the support.</span></p></body></html>", None))
        self.label_89.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">Your current devices registered / your max devices you can register.</span></p></body></html>", None))
        self.label_90.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">The first time you logged in with this license. Mainly for OGs to flex how awesome they are.</span></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Key expires in:</p></body></html>", None))
        self.license_expires.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">N/A</span></p></body></html>", None))
        self.label_93.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00aaff;\">Countdown for your key to expire, not available for lifetime customers. The countdown refreshes every hour. </span></p></body></html>", None))
        self.label_117.setText(QCoreApplication.translate("Form", u"1. You are strictly forbidden from sharing your key with anyone else.  If you get caught using the bot on multiple machines simultaneously on different IPs your key will be blocked without further notice.", None))
        self.label_118.setText(QCoreApplication.translate("Form", u"2. If you see your key will expire soon please message me ahead of time if you would like to extend.", None))
        self.label_119.setText(QCoreApplication.translate("Form", u"3. If you are unhappy with the performance youre almost certainly doing something wrong, please do not hesitate to ask for help and advice in the discord.", None))
        self.label_120.setText(QCoreApplication.translate("Form", u"4. Do not risk showing the bot running to anyone but your closest friends, you will not get banned for using it but player reports with decent evidence may get you suspended.", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.maintab_license), QCoreApplication.translate("Form", u"Help / Info", None))
        self.select_item.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">Item:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.current_item.setToolTip(QCoreApplication.translate("Form", u"The item you would like to select the configuration and statistics for.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.delete_item.setToolTip(QCoreApplication.translate("Form", u"Remove the current displayed item from your database", None))
#endif // QT_CONFIG(tooltip)
        self.delete_item.setText(QCoreApplication.translate("Form", u"Delete item", None))
#if QT_CONFIG(tooltip)
        self.add_item.setToolTip(QCoreApplication.translate("Form", u"Add a new item to the database", None))
#endif // QT_CONFIG(tooltip)
        self.add_item.setText(QCoreApplication.translate("Form", u"Add item", None))
        self.item_currency.setItemText(0, QCoreApplication.translate("Form", u"\u20bd", None))
        self.item_currency.setItemText(1, QCoreApplication.translate("Form", u"\u20ac", None))
        self.item_currency.setItemText(2, QCoreApplication.translate("Form", u"$", None))

#if QT_CONFIG(tooltip)
        self.item_currency.setToolTip(QCoreApplication.translate("Form", u"The items currency", None))
#endif // QT_CONFIG(tooltip)
        self.select_vendor.setText(QCoreApplication.translate("Form", u"Vendor:", None))
        self.select_currency.setText(QCoreApplication.translate("Form", u"Currency:", None))
        self.item_vendor.setItemText(0, QCoreApplication.translate("Form", u"Therapist", None))
        self.item_vendor.setItemText(1, QCoreApplication.translate("Form", u"Fence", None))

#if QT_CONFIG(tooltip)
        self.item_vendor.setToolTip(QCoreApplication.translate("Form", u"The vendor to sell the item at", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.item_refreshes.setToolTip(QCoreApplication.translate("Form", u"The amount of times to refresh on this item", None))
#endif // QT_CONFIG(tooltip)
        self.set_item_refreshes.setText(QCoreApplication.translate("Form", u"Refreshes:", None))
#if QT_CONFIG(tooltip)
        self.item_value.setToolTip(QCoreApplication.translate("Form", u"What the vendor pays for this item, you can see this by buying one and going into the vendor.", None))
#endif // QT_CONFIG(tooltip)
        self.item_value.setPlaceholderText(QCoreApplication.translate("Form", u"32 130", None))
        self.set_item_value.setText(QCoreApplication.translate("Form", u"Value:", None))
#if QT_CONFIG(tooltip)
        self.item_max_price.setToolTip(QCoreApplication.translate("Form", u"The item price the bot will put into the filter.\n"
"If you set it to 32 200, it wont see items for 32 360 for example.", None))
#endif // QT_CONFIG(tooltip)
        self.item_max_price.setPlaceholderText(QCoreApplication.translate("Form", u"30 200", None))
        self.set_item_price.setText(QCoreApplication.translate("Form", u"Max. price:", None))
        self.set_item_value_2.setText(QCoreApplication.translate("Form", u"Min. profit:", None))
#if QT_CONFIG(tooltip)
        self.item_profit.setToolTip(QCoreApplication.translate("Form", u"The least profit a purchase of this item could possibly make.\n"
"\n"
"Results from item value - maximum purchase price.", None))
#endif // QT_CONFIG(tooltip)
        self.item_profit.setPlaceholderText(QCoreApplication.translate("Form", u"1930", None))
        self.select_vendor_2.setText(QCoreApplication.translate("Form", u"Size:", None))
        self.item_size.setItemText(0, QCoreApplication.translate("Form", u"1x1", None))
        self.item_size.setItemText(1, QCoreApplication.translate("Form", u"1x2", None))
        self.item_size.setItemText(2, QCoreApplication.translate("Form", u"1x3", None))
        self.item_size.setItemText(3, QCoreApplication.translate("Form", u"2x2", None))
        self.item_size.setItemText(4, QCoreApplication.translate("Form", u"2x3", None))
        self.item_size.setItemText(5, QCoreApplication.translate("Form", u"3x2", None))
        self.item_size.setItemText(6, QCoreApplication.translate("Form", u"3x3", None))
        self.item_size.setItemText(7, QCoreApplication.translate("Form", u"3x4", None))
        self.item_size.setItemText(8, QCoreApplication.translate("Form", u"4x3", None))

#if QT_CONFIG(tooltip)
        self.item_size.setToolTip(QCoreApplication.translate("Form", u"The dimensions of the item, this is important in two aspects:\n"
"\n"
"1. The bot wants to know how many slots of the inventory are currently filled\n"
"\n"
"2. The bot needs to know it to take the correct screenshot of the items inventory image\n"
"\n"
"Please remember its X by Y, not Y by X", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Item configuration", None))
        self.label_4.setText("")
        self.set_item_value_3.setText(QCoreApplication.translate("Form", u"Searched:", None))
#if QT_CONFIG(tooltip)
        self.item_stats_searched.setToolTip(QCoreApplication.translate("Form", u"The amount of times the item has been searched or refreshed for, regardless of finding hits or not", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_searched.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.item_stats_searched.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
#if QT_CONFIG(tooltip)
        self.item_stats_found.setToolTip(QCoreApplication.translate("Form", u"The amount of times at least 1 item was available for purchase on search", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_found.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.item_stats_found.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.set_item_value_4.setText(QCoreApplication.translate("Form", u"Found:", None))
#if QT_CONFIG(tooltip)
        self.item_stats_bought.setToolTip(QCoreApplication.translate("Form", u"The amount of times this item has been bought", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_bought.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.item_stats_bought.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.set_item_value_5.setText(QCoreApplication.translate("Form", u"Bought:", None))
#if QT_CONFIG(tooltip)
        self.item_stats_avg_profit.setToolTip(QCoreApplication.translate("Form", u"The average profit you make per purchase on this item", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_avg_profit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.item_stats_avg_profit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.set_item_value_6.setText(QCoreApplication.translate("Form", u"Avg. profit:", None))
#if QT_CONFIG(tooltip)
        self.item_stats_total_profit.setToolTip(QCoreApplication.translate("Form", u"The total profit this item has netted you", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_total_profit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.item_stats_total_profit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.set_item_value_7.setText(QCoreApplication.translate("Form", u"Total profit:", None))
#if QT_CONFIG(tooltip)
        self.item_stats_rank.setToolTip(QCoreApplication.translate("Form", u"The rank of this item compared to your other items, criteria is the efficiency", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_rank.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.set_item_value_8.setText(QCoreApplication.translate("Form", u"Rank:", None))
#if QT_CONFIG(tooltip)
        self.item_enabled.setToolTip(QCoreApplication.translate("Form", u"Enable to add the item to the list of items the bot will search", None))
#endif // QT_CONFIG(tooltip)
        self.item_enabled.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Item statistics", None))
#if QT_CONFIG(tooltip)
        self.item_stats_rarity.setToolTip(QCoreApplication.translate("Form", u"The rarity of the item, if the rarity is 10% you can expect to find at least one item in 10 searches", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_rarity.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.item_stats_rarity.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.set_item_value_9.setText(QCoreApplication.translate("Form", u"Rarity:", None))
#if QT_CONFIG(tooltip)
        self.item_stats_efficiency.setToolTip(QCoreApplication.translate("Form", u"The items efficiency is a little maths we came up with on our own, its determined as follows:\n"
"\n"
"Lets assume the optimal profit is 500 000 RUB / hour, one hour holds roughly 1200 searches / refreshes.\n"
"The maximum efficiency would be roughly 400 RUB per search, this means the items efficiency will be:\n"
"\n"
"((items profit / times searched) / max efficiency) * 100 ", None))
#endif // QT_CONFIG(tooltip)
        self.item_stats_efficiency.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.item_stats_efficiency.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.set_item_value_10.setText(QCoreApplication.translate("Form", u"Efficiency:", None))
#if QT_CONFIG(tooltip)
        self.item_image_path.setToolTip(QCoreApplication.translate("Form", u"Displays if the item has an image already or not, if it does not, the item will not be sold.", None))
#endif // QT_CONFIG(tooltip)
        self.item_image_path.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Display Light'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.item_image_path.setPlaceholderText(QCoreApplication.translate("Form", u"Missing", None))
        self.set_item_value_11.setText(QCoreApplication.translate("Form", u"Image:", None))
#if QT_CONFIG(tooltip)
        self.add_image.setToolTip(QCoreApplication.translate("Form", u"Add this items image, please refer to the discord guide.", None))
#endif // QT_CONFIG(tooltip)
        self.add_image.setText(QCoreApplication.translate("Form", u"Add", None))
        self.amount_label.setText(QCoreApplication.translate("Form", u"Buy amount:", None))
#if QT_CONFIG(tooltip)
        self.item_buy_amount.setToolTip(QCoreApplication.translate("Form", u"The amount of items to buy to stop buying any more in the current session.\n"
"\n"
"This can be useful if you dont intend to sell the item and just want to stock up on them\n"
"\n"
"Leave at 0 to just continue buying at any amount.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.reset_item_stats.setToolTip(QCoreApplication.translate("Form", u"Reset the statistics of the current item", None))
#endif // QT_CONFIG(tooltip)
        self.reset_item_stats.setText(QCoreApplication.translate("Form", u"Reset item", None))
#if QT_CONFIG(tooltip)
        self.reset_all_items_stats.setToolTip(QCoreApplication.translate("Form", u"Resets the stats of all items INLUDING TIMELINE", None))
#endif // QT_CONFIG(tooltip)
        self.reset_all_items_stats.setText(QCoreApplication.translate("Form", u"Reset all items", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.maintab_database), QCoreApplication.translate("Form", u"Seite", None))
        self.select_statistic.setItemText(0, QCoreApplication.translate("Form", u"Average profit timeline - plot chart", None))
        self.select_statistic.setItemText(1, QCoreApplication.translate("Form", u"Total item profits - bar chart", None))
        self.select_statistic.setItemText(2, QCoreApplication.translate("Form", u"Item efficiency - bar chart", None))
        self.select_statistic.setItemText(3, QCoreApplication.translate("Form", u"Total profit - pie chart", None))

#if QT_CONFIG(tooltip)
        self.select_statistic.setToolTip(QCoreApplication.translate("Form", u"Select what button you move with", None))
#endif // QT_CONFIG(tooltip)
        self.mouse_movements_2.setText(QCoreApplication.translate("Form", u"Statistic:", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.maintab_statistics), QCoreApplication.translate("Form", u"Seite", None))
        self.label.setText("")
        self.bot_status.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#55ffff;\">Bot Status:</span> Idle - Press F1 to start.</p></body></html>", None))
        self.buttons_statistics.setText(QCoreApplication.translate("Form", u"Statistics", None))
    # retranslateUi


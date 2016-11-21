# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_tab.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 631)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/asmm_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    top: -1px;\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border-top: 1px solid rgb(180,180,180);\n"
"    border-left: 1px solid rgb(180,180,180);\n"
"    border-right: 1px solid rgb(180,180,180);\n"
"    border-top-right-radius: 5px;\n"
"    border-top-left-radius: 5px;\n"
"    padding: 2px 10px 2px 10px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(210,210,210);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px; \n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    background-color: rgb(240,240,240);\n"
"}\n"
"\n"
"QTabBar QToolButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(icons/right_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(icons/left_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.fi_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage1)
        self.fi_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.fi_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fi_scrollArea.setWidgetResizable(True)
        self.fi_scrollArea.setObjectName("fi_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_28.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_28.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(19)
        self.gridLayout_4.setVerticalSpacing(12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.projectAcronym_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.projectAcronym_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.projectAcronym_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.projectAcronym_lb.setFont(font)
        self.projectAcronym_lb.setObjectName("projectAcronym_lb")
        self.gridLayout_4.addWidget(self.projectAcronym_lb, 0, 0, 1, 1)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.projectAcronym_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.projectAcronym_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.projectAcronym_ln.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.projectAcronym_ln.setFont(font)
        self.projectAcronym_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.projectAcronym_ln.setFrame(False)
        self.projectAcronym_ln.setObjectName("projectAcronym_ln")
        self.horizontalLayout_52.addWidget(self.projectAcronym_ln)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem2)
        self.infoButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton_1.setIcon(icon1)
        self.infoButton_1.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_1.setAutoRaise(False)
        self.infoButton_1.setObjectName("infoButton_1")
        self.horizontalLayout_52.addWidget(self.infoButton_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem3)
        self.gridLayout_4.addLayout(self.horizontalLayout_52, 0, 1, 1, 1)
        self.date_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.date_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.date_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.date_lb.setFont(font)
        self.date_lb.setObjectName("date_lb")
        self.gridLayout_4.addWidget(self.date_lb, 1, 0, 1, 1)
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.date_dt = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.date_dt.setMinimumSize(QtCore.QSize(130, 27))
        self.date_dt.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.date_dt.setFont(font)
        self.date_dt.setStyleSheet("QDateEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
"\n"
"QDateEdit::drop-down {subcontrol-origin: padding; subcontrol-position: top right; width: 27px; border-top-right-radius: 3px; border-bottom-right-radius: 3px;}\n"
"\n"
"QDateEdit::drop-down:hover {subcontrol-origin: padding; subcontrol-position: top right; width: 27px; border-left-width: 1px; border-left-color: darkgray; border-left-style: solid; border-top-right-radius: 3px; border-bottom-right-radius: 3px;}\n"
"\n"
"QDateEdit::down-arrow {image: url(icons/arrow_down.png); width: 18px; height: 18px;}\n"
"\n"
"QDateEdit::down-arrow:on {top: 1px; left: 1px;}")
        self.date_dt.setFrame(False)
        self.date_dt.setAlignment(QtCore.Qt.AlignCenter)
        self.date_dt.setAccelerated(True)
        self.date_dt.setTime(QtCore.QTime(23, 0, 0))
        self.date_dt.setCalendarPopup(True)
        self.date_dt.setTimeSpec(QtCore.Qt.UTC)
        self.date_dt.setObjectName("date_dt")
        self.horizontalLayout_70.addWidget(self.date_dt)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_70.addItem(spacerItem4)
        self.infoButton_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_2.setText("")
        self.infoButton_2.setIcon(icon1)
        self.infoButton_2.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_2.setAutoRaise(False)
        self.infoButton_2.setObjectName("infoButton_2")
        self.horizontalLayout_70.addWidget(self.infoButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_70.addItem(spacerItem5)
        self.gridLayout_4.addLayout(self.horizontalLayout_70, 1, 1, 1, 1)
        self.flightNumber_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.flightNumber_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.flightNumber_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.flightNumber_lb.setFont(font)
        self.flightNumber_lb.setObjectName("flightNumber_lb")
        self.gridLayout_4.addWidget(self.flightNumber_lb, 2, 0, 1, 1)
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.flightNumber_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.flightNumber_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.flightNumber_ln.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.flightNumber_ln.setFont(font)
        self.flightNumber_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.flightNumber_ln.setFrame(False)
        self.flightNumber_ln.setObjectName("flightNumber_ln")
        self.horizontalLayout_71.addWidget(self.flightNumber_ln)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_71.addItem(spacerItem6)
        self.infoButton_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_3.setText("")
        self.infoButton_3.setIcon(icon1)
        self.infoButton_3.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_3.setAutoRaise(False)
        self.infoButton_3.setObjectName("infoButton_3")
        self.horizontalLayout_71.addWidget(self.infoButton_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_71.addItem(spacerItem7)
        self.gridLayout_4.addLayout(self.horizontalLayout_71, 2, 1, 1, 1)
        self.missionSci_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.missionSci_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.missionSci_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.missionSci_lb.setFont(font)
        self.missionSci_lb.setObjectName("missionSci_lb")
        self.gridLayout_4.addWidget(self.missionSci_lb, 3, 0, 1, 1)
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.missionSci_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.missionSci_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.missionSci_ln.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.missionSci_ln.setFont(font)
        self.missionSci_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.missionSci_ln.setFrame(False)
        self.missionSci_ln.setObjectName("missionSci_ln")
        self.horizontalLayout_72.addWidget(self.missionSci_ln)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem8)
        self.infoButton_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_4.setText("")
        self.infoButton_4.setIcon(icon1)
        self.infoButton_4.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_4.setAutoRaise(False)
        self.infoButton_4.setObjectName("infoButton_4")
        self.horizontalLayout_72.addWidget(self.infoButton_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem9)
        self.gridLayout_4.addLayout(self.horizontalLayout_72, 3, 1, 1, 1)
        self.flightManager_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.flightManager_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.flightManager_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.flightManager_lb.setFont(font)
        self.flightManager_lb.setObjectName("flightManager_lb")
        self.gridLayout_4.addWidget(self.flightManager_lb, 4, 0, 1, 1)
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.flightManager_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.flightManager_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.flightManager_ln.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.flightManager_ln.setFont(font)
        self.flightManager_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.flightManager_ln.setFrame(False)
        self.flightManager_ln.setObjectName("flightManager_ln")
        self.horizontalLayout_73.addWidget(self.flightManager_ln)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_73.addItem(spacerItem10)
        self.infoButton_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_5.setText("")
        self.infoButton_5.setIcon(icon1)
        self.infoButton_5.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_5.setAutoRaise(False)
        self.infoButton_5.setObjectName("infoButton_5")
        self.horizontalLayout_73.addWidget(self.infoButton_5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_73.addItem(spacerItem11)
        self.gridLayout_4.addLayout(self.horizontalLayout_73, 4, 1, 1, 1)
        self.operator_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.operator_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.operator_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.operator_lb.setFont(font)
        self.operator_lb.setObjectName("operator_lb")
        self.gridLayout_4.addWidget(self.operator_lb, 5, 0, 1, 1)
        self.horizontalLayout_74 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        self.operator_cb = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.operator_cb.setMinimumSize(QtCore.QSize(200, 27))
        self.operator_cb.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.operator_cb.setFont(font)
        self.operator_cb.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/arrow_down.png); \n"
"    width: 18px;\n"
"    height: 18px\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: transparent;\n"
"    selection-color: blue;\n"
"    border: 0px, solid black;\n"
"}")
        self.operator_cb.setFrame(False)
        self.operator_cb.setObjectName("operator_cb")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.operator_cb.addItem("")
        self.horizontalLayout_74.addWidget(self.operator_cb)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem12)
        self.infoButton_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_6.setText("")
        self.infoButton_6.setIcon(icon1)
        self.infoButton_6.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_6.setAutoRaise(False)
        self.infoButton_6.setObjectName("infoButton_6")
        self.horizontalLayout_74.addWidget(self.infoButton_6)
        spacerItem13 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem13)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setEnabled(True)
        self.label_38.setMinimumSize(QtCore.QSize(15, 15))
        self.label_38.setMaximumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_38.setFont(font)
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("icons/fwdarrow_icon.svg"))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_74.addWidget(self.label_38)
        spacerItem14 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem14)
        self.newOperator_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.newOperator_ln.setEnabled(True)
        self.newOperator_ln.setMinimumSize(QtCore.QSize(300, 27))
        self.newOperator_ln.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.newOperator_ln.setFont(font)
        self.newOperator_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.newOperator_ln.setFrame(False)
        self.newOperator_ln.setObjectName("newOperator_ln")
        self.horizontalLayout_74.addWidget(self.newOperator_ln)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem15)
        self.gridLayout_4.addLayout(self.horizontalLayout_74, 5, 1, 1, 1)
        self.aircraft_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.aircraft_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.aircraft_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aircraft_lb.setFont(font)
        self.aircraft_lb.setObjectName("aircraft_lb")
        self.gridLayout_4.addWidget(self.aircraft_lb, 6, 0, 1, 1)
        self.horizontalLayout_75 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.aircraft_cb = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.aircraft_cb.setEnabled(False)
        self.aircraft_cb.setMinimumSize(QtCore.QSize(200, 27))
        self.aircraft_cb.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aircraft_cb.setFont(font)
        self.aircraft_cb.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/arrow_down.png); \n"
"    width: 18px;\n"
"    height: 18px\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: transparent;\n"
"    selection-color: blue;\n"
"    border: 0px, solid black;\n"
"}")
        self.aircraft_cb.setFrame(False)
        self.aircraft_cb.setObjectName("aircraft_cb")
        self.horizontalLayout_75.addWidget(self.aircraft_cb)
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem16)
        self.emtpyButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.emtpyButton.setEnabled(False)
        self.emtpyButton.setMaximumSize(QtCore.QSize(27, 27))
        self.emtpyButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.emtpyButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emtpyButton.setIcon(icon2)
        self.emtpyButton.setIconSize(QtCore.QSize(27, 27))
        self.emtpyButton.setAutoRaise(False)
        self.emtpyButton.setObjectName("emtpyButton")
        self.horizontalLayout_75.addWidget(self.emtpyButton)
        spacerItem17 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem17)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_39.setEnabled(True)
        self.label_39.setMinimumSize(QtCore.QSize(15, 15))
        self.label_39.setMaximumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_39.setFont(font)
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("icons/fwdarrow_icon.svg"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_75.addWidget(self.label_39)
        spacerItem18 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem18)
        self.newAircraft_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.newAircraft_ln.setEnabled(True)
        self.newAircraft_ln.setMinimumSize(QtCore.QSize(300, 27))
        self.newAircraft_ln.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.newAircraft_ln.setFont(font)
        self.newAircraft_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.newAircraft_ln.setFrame(False)
        self.newAircraft_ln.setObjectName("newAircraft_ln")
        self.horizontalLayout_75.addWidget(self.newAircraft_ln)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem19)
        self.gridLayout_4.addLayout(self.horizontalLayout_75, 6, 1, 1, 1)
        self.location_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.location_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.location_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.location_lb.setFont(font)
        self.location_lb.setObjectName("location_lb")
        self.gridLayout_4.addWidget(self.location_lb, 7, 0, 1, 1)
        self.horizontalLayout_76 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")
        self.location_cb = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.location_cb.setEnabled(True)
        self.location_cb.setMinimumSize(QtCore.QSize(200, 27))
        self.location_cb.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.location_cb.setFont(font)
        self.location_cb.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/arrow_down.png); \n"
"    width: 18px;\n"
"    height: 18px\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: transparent;\n"
"    selection-color: blue;\n"
"    border: 0px, solid black;\n"
"}")
        self.location_cb.setFrame(False)
        self.location_cb.setObjectName("location_cb")
        self.horizontalLayout_76.addWidget(self.location_cb)
        spacerItem20 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem20)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setMinimumSize(QtCore.QSize(15, 15))
        self.label_34.setMaximumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_34.setFont(font)
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("icons/fwdarrow_icon.svg"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_76.addWidget(self.label_34)
        spacerItem21 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem21)
        self.detailList = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.detailList.setEnabled(False)
        self.detailList.setMinimumSize(QtCore.QSize(200, 27))
        self.detailList.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.detailList.setFont(font)
        self.detailList.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/arrow_down.png); \n"
"    width: 18px;\n"
"    height: 18px\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: transparent;\n"
"    selection-color: blue;\n"
"    border: 0px, solid black;\n"
"}")
        self.detailList.setFrame(False)
        self.detailList.setObjectName("detailList")
        self.horizontalLayout_76.addWidget(self.detailList)
        spacerItem22 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem22)
        self.infoButton_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_7.setText("")
        self.infoButton_7.setIcon(icon1)
        self.infoButton_7.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_7.setAutoRaise(False)
        self.infoButton_7.setObjectName("infoButton_7")
        self.horizontalLayout_76.addWidget(self.infoButton_7)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem23)
        self.gridLayout_4.addLayout(self.horizontalLayout_76, 7, 1, 1, 1)
        self.gridLayout_28.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_28.addItem(spacerItem24, 1, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 149, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_28.addItem(spacerItem25, 2, 1, 1, 1)
        self.fi_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_26.addWidget(self.fi_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.tabWidgetPage2)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.gi_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage2)
        self.gi_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.gi_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gi_scrollArea.setWidgetResizable(True)
        self.gi_scrollArea.setObjectName("gi_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_29.addItem(spacerItem26, 0, 2, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem27, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(19)
        self.gridLayout_3.setVerticalSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.contactName_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.contactName_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.contactName_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contactName_lb.setFont(font)
        self.contactName_lb.setObjectName("contactName_lb")
        self.gridLayout_3.addWidget(self.contactName_lb, 0, 0, 1, 1)
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.contactName_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.contactName_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.contactName_ln.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contactName_ln.setFont(font)
        self.contactName_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.contactName_ln.setFrame(False)
        self.contactName_ln.setObjectName("contactName_ln")
        self.horizontalLayout_53.addWidget(self.contactName_ln)
        spacerItem28 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem28)
        self.infoButton_8 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_8.setText("")
        self.infoButton_8.setIcon(icon1)
        self.infoButton_8.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_8.setAutoRaise(False)
        self.infoButton_8.setObjectName("infoButton_8")
        self.horizontalLayout_53.addWidget(self.infoButton_8)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem29)
        self.gridLayout_3.addLayout(self.horizontalLayout_53, 0, 1, 1, 1)
        self.contact_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.contact_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.contact_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contact_lb.setFont(font)
        self.contact_lb.setObjectName("contact_lb")
        self.gridLayout_3.addWidget(self.contact_lb, 1, 0, 1, 1)
        self.horizontalLayout_78 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")
        self.contact_cb = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.contact_cb.setMinimumSize(QtCore.QSize(180, 27))
        self.contact_cb.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contact_cb.setFont(font)
        self.contact_cb.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/arrow_down.png); \n"
"    width: 18px;\n"
"    height: 18px\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px; \n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: transparent;\n"
"    selection-color: blue;\n"
"    border: 0px, solid black;\n"
"}")
        self.contact_cb.setFrame(False)
        self.contact_cb.setObjectName("contact_cb")
        self.contact_cb.addItem("")
        self.contact_cb.addItem("")
        self.contact_cb.addItem("")
        self.contact_cb.addItem("")
        self.contact_cb.addItem("")
        self.contact_cb.addItem("")
        self.horizontalLayout_78.addWidget(self.contact_cb)
        spacerItem30 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_78.addItem(spacerItem30)
        self.infoButton_9 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.infoButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_9.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_9.setText("")
        self.infoButton_9.setIcon(icon1)
        self.infoButton_9.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_9.setAutoRaise(False)
        self.infoButton_9.setObjectName("infoButton_9")
        self.horizontalLayout_78.addWidget(self.infoButton_9)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_78.addItem(spacerItem31)
        self.gridLayout_3.addLayout(self.horizontalLayout_78, 1, 1, 1, 1)
        self.contactEmail_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.contactEmail_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.contactEmail_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contactEmail_lb.setFont(font)
        self.contactEmail_lb.setObjectName("contactEmail_lb")
        self.gridLayout_3.addWidget(self.contactEmail_lb, 2, 0, 1, 1)
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.contactEmail_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactEmail_ln.sizePolicy().hasHeightForWidth())
        self.contactEmail_ln.setSizePolicy(sizePolicy)
        self.contactEmail_ln.setMinimumSize(QtCore.QSize(400, 27))
        self.contactEmail_ln.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contactEmail_ln.setFont(font)
        self.contactEmail_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.contactEmail_ln.setFrame(False)
        self.contactEmail_ln.setObjectName("contactEmail_ln")
        self.horizontalLayout_79.addWidget(self.contactEmail_ln)
        spacerItem32 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem32)
        self.infoButton_10 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.infoButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_10.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_10.setText("")
        self.infoButton_10.setIcon(icon1)
        self.infoButton_10.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_10.setAutoRaise(False)
        self.infoButton_10.setObjectName("infoButton_10")
        self.horizontalLayout_79.addWidget(self.infoButton_10)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem33)
        self.gridLayout_3.addLayout(self.horizontalLayout_79, 2, 1, 1, 1)
        self.gridLayout_29.addLayout(self.gridLayout_3, 1, 1, 1, 2)
        spacerItem34 = QtWidgets.QSpacerItem(454, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem34, 1, 3, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(20, 354, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_29.addItem(spacerItem35, 2, 1, 1, 1)
        self.gi_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_27.addWidget(self.gi_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.sa_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage3)
        self.sa_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.sa_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sa_scrollArea.setWidgetResizable(True)
        self.sa_scrollArea.setObjectName("sa_scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1049, 542))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem36 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem36, 0, 1, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem37, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.satelliteCalValCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.satelliteCalValCheck.setFont(font)
        self.satelliteCalValCheck.setObjectName("satelliteCalValCheck")
        self.horizontalLayout_3.addWidget(self.satelliteCalValCheck)
        spacerItem38 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem38)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.anthroPollutionCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.anthroPollutionCheck.setFont(font)
        self.anthroPollutionCheck.setObjectName("anthroPollutionCheck")
        self.horizontalLayout_4.addWidget(self.anthroPollutionCheck)
        spacerItem39 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem39)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mesoscaleImpactsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mesoscaleImpactsCheck.setFont(font)
        self.mesoscaleImpactsCheck.setObjectName("mesoscaleImpactsCheck")
        self.horizontalLayout_5.addWidget(self.mesoscaleImpactsCheck)
        spacerItem40 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem40)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem41 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem41)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        spacerItem42 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem42)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem43 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem43)
        self.cloudMicrophysicsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudMicrophysicsCheck.setFont(font)
        self.cloudMicrophysicsCheck.setObjectName("cloudMicrophysicsCheck")
        self.horizontalLayout_15.addWidget(self.cloudMicrophysicsCheck)
        spacerItem44 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem44)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        spacerItem45 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_80.addItem(spacerItem45)
        self.cloudDynamicsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudDynamicsCheck.setFont(font)
        self.cloudDynamicsCheck.setObjectName("cloudDynamicsCheck")
        self.horizontalLayout_80.addWidget(self.cloudDynamicsCheck)
        spacerItem46 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_80.addItem(spacerItem46)
        self.verticalLayout_3.addLayout(self.horizontalLayout_80)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        spacerItem47 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem47)
        self.cloudRadiativeCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudRadiativeCheck.setFont(font)
        self.cloudRadiativeCheck.setObjectName("cloudRadiativeCheck")
        self.horizontalLayout_83.addWidget(self.cloudRadiativeCheck)
        spacerItem48 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem48)
        self.verticalLayout_3.addLayout(self.horizontalLayout_83)
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        spacerItem49 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_84.addItem(spacerItem49)
        self.cloudConvectionCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudConvectionCheck.setFont(font)
        self.cloudConvectionCheck.setObjectName("cloudConvectionCheck")
        self.horizontalLayout_84.addWidget(self.cloudConvectionCheck)
        spacerItem50 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_84.addItem(spacerItem50)
        self.verticalLayout_3.addLayout(self.horizontalLayout_84)
        self.horizontalLayout_92.addLayout(self.verticalLayout_3)
        spacerItem51 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_92.addItem(spacerItem51)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gasChemCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemCheck.setFont(font)
        self.gasChemCheck.setObjectName("gasChemCheck")
        self.horizontalLayout.addWidget(self.gasChemCheck)
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem52)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem53 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem53)
        self.gasChemOxidantsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemOxidantsCheck.setFont(font)
        self.gasChemOxidantsCheck.setObjectName("gasChemOxidantsCheck")
        self.horizontalLayout_2.addWidget(self.gasChemOxidantsCheck)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem54)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem55 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem55)
        self.gasChemOrganicsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemOrganicsCheck.setFont(font)
        self.gasChemOrganicsCheck.setObjectName("gasChemOrganicsCheck")
        self.horizontalLayout_12.addWidget(self.gasChemOrganicsCheck)
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem56)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem57 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem57)
        self.gasChemOtherCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemOtherCheck.setFont(font)
        self.gasChemOtherCheck.setObjectName("gasChemOtherCheck")
        self.horizontalLayout_13.addWidget(self.gasChemOtherCheck)
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem58)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        spacerItem59 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem59)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.aerosolCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aerosolCheck.setFont(font)
        self.aerosolCheck.setObjectName("aerosolCheck")
        self.horizontalLayout_14.addWidget(self.aerosolCheck)
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem60)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        spacerItem61 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem61)
        self.aerosolMicrophysicalCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aerosolMicrophysicalCheck.setFont(font)
        self.aerosolMicrophysicalCheck.setObjectName("aerosolMicrophysicalCheck")
        self.horizontalLayout_85.addWidget(self.aerosolMicrophysicalCheck)
        spacerItem62 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem62)
        self.verticalLayout_2.addLayout(self.horizontalLayout_85)
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        spacerItem63 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_86.addItem(spacerItem63)
        self.aerosolRadiativeCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aerosolRadiativeCheck.setFont(font)
        self.aerosolRadiativeCheck.setObjectName("aerosolRadiativeCheck")
        self.horizontalLayout_86.addWidget(self.aerosolRadiativeCheck)
        spacerItem64 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_86.addItem(spacerItem64)
        self.verticalLayout_2.addLayout(self.horizontalLayout_86)
        spacerItem65 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem65)
        self.horizontalLayout_92.addLayout(self.verticalLayout_2)
        spacerItem66 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_92.addItem(spacerItem66)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radiationCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationCheck.setFont(font)
        self.radiationCheck.setObjectName("radiationCheck")
        self.horizontalLayout_7.addWidget(self.radiationCheck)
        spacerItem67 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem67)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem68 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem68)
        self.radiationAtmosSpectroscopyCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationAtmosSpectroscopyCheck.setFont(font)
        self.radiationAtmosSpectroscopyCheck.setObjectName("radiationAtmosSpectroscopyCheck")
        self.horizontalLayout_8.addWidget(self.radiationAtmosSpectroscopyCheck)
        spacerItem69 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem69)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        spacerItem70 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_87.addItem(spacerItem70)
        self.radiationSurfPropertiesCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationSurfPropertiesCheck.setFont(font)
        self.radiationSurfPropertiesCheck.setObjectName("radiationSurfPropertiesCheck")
        self.horizontalLayout_87.addWidget(self.radiationSurfPropertiesCheck)
        spacerItem71 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_87.addItem(spacerItem71)
        self.verticalLayout.addLayout(self.horizontalLayout_87)
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        spacerItem72 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem72)
        self.radiationOtherCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationOtherCheck.setFont(font)
        self.radiationOtherCheck.setObjectName("radiationOtherCheck")
        self.horizontalLayout_88.addWidget(self.radiationOtherCheck)
        spacerItem73 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem73)
        self.verticalLayout.addLayout(self.horizontalLayout_88)
        spacerItem74 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem74)
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_89.addWidget(self.label_13)
        spacerItem75 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_89.addItem(spacerItem75)
        self.verticalLayout.addLayout(self.horizontalLayout_89)
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        spacerItem76 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_90.addItem(spacerItem76)
        self.blCloudCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.blCloudCheck.setFont(font)
        self.blCloudCheck.setObjectName("blCloudCheck")
        self.horizontalLayout_90.addWidget(self.blCloudCheck)
        spacerItem77 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_90.addItem(spacerItem77)
        self.verticalLayout.addLayout(self.horizontalLayout_90)
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        spacerItem78 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_91.addItem(spacerItem78)
        self.blDynamicsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.blDynamicsCheck.setFont(font)
        self.blDynamicsCheck.setObjectName("blDynamicsCheck")
        self.horizontalLayout_91.addWidget(self.blDynamicsCheck)
        spacerItem79 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_91.addItem(spacerItem79)
        self.verticalLayout.addLayout(self.horizontalLayout_91)
        spacerItem80 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem80)
        self.horizontalLayout_92.addLayout(self.verticalLayout)
        spacerItem81 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_92.addItem(spacerItem81)
        self.infoButton_25 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.infoButton_25.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_25.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_25.setText("")
        self.infoButton_25.setIcon(icon1)
        self.infoButton_25.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_25.setAutoRaise(False)
        self.infoButton_25.setObjectName("infoButton_25")
        self.horizontalLayout_92.addWidget(self.infoButton_25)
        self.verticalLayout_4.addLayout(self.horizontalLayout_92)
        spacerItem82 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem82)
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        spacerItem83 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem83)
        self.sa_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.sa_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.sa_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sa_addButton.setFont(font)
        self.sa_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.sa_addButton.setObjectName("sa_addButton")
        self.horizontalLayout_61.addWidget(self.sa_addButton)
        spacerItem84 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem84)
        self.sa_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.sa_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.sa_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.sa_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.sa_infoButton.setText("")
        self.sa_infoButton.setIcon(icon1)
        self.sa_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.sa_infoButton.setAutoRaise(False)
        self.sa_infoButton.setObjectName("sa_infoButton")
        self.horizontalLayout_61.addWidget(self.sa_infoButton)
        spacerItem85 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem85)
        self.verticalLayout_4.addLayout(self.horizontalLayout_61)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_4.addLayout(self.gridLayout_5)
        spacerItem86 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem86)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setMinimumSize(QtCore.QSize(0, 27))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)
        spacerItem87 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem87)
        self.horizontalLayout_16.addLayout(self.verticalLayout_12)
        self.SAOtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.SAOtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.SAOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SAOtherTextBox.setFont(font)
        self.SAOtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.SAOtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SAOtherTextBox.setObjectName("SAOtherTextBox")
        self.horizontalLayout_16.addWidget(self.SAOtherTextBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 1, 1, 2, 2)
        spacerItem88 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem88, 2, 3, 1, 1)
        spacerItem89 = QtWidgets.QSpacerItem(28, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem89, 3, 2, 1, 1)
        self.sa_scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_30.addWidget(self.sa_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.tabWidgetPage4)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.gr_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage4)
        self.gr_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.gr_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gr_scrollArea.setWidgetResizable(True)
        self.gr_scrollArea.setObjectName("gr_scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        spacerItem90 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_17.addItem(spacerItem90, 0, 1, 1, 1)
        spacerItem91 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem91, 1, 0, 1, 1)
        self.verticalLayout_59 = QtWidgets.QVBoxLayout()
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_50.addWidget(self.label_32)
        spacerItem92 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem92)
        self.verticalLayout_59.addLayout(self.horizontalLayout_50)
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        spacerItem93 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem93)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_31.setMinimumSize(QtCore.QSize(150, 27))
        self.label_31.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_45.addWidget(self.label_31)
        spacerItem94 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_45.addItem(spacerItem94)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_29.setMinimumSize(QtCore.QSize(150, 27))
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_45.addWidget(self.label_29)
        self.horizontalLayout_51.addLayout(self.verticalLayout_45)
        spacerItem95 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem95)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.northBoundLatitudeLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.northBoundLatitudeLine.setMinimumSize(QtCore.QSize(70, 27))
        self.northBoundLatitudeLine.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.northBoundLatitudeLine.setFont(font)
        self.northBoundLatitudeLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.northBoundLatitudeLine.setFrame(False)
        self.northBoundLatitudeLine.setObjectName("northBoundLatitudeLine")
        self.verticalLayout_11.addWidget(self.northBoundLatitudeLine)
        spacerItem96 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem96)
        self.westBoundLongitudeLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.westBoundLongitudeLine.setMinimumSize(QtCore.QSize(70, 27))
        self.westBoundLongitudeLine.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.westBoundLongitudeLine.setFont(font)
        self.westBoundLongitudeLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.westBoundLongitudeLine.setFrame(False)
        self.westBoundLongitudeLine.setObjectName("westBoundLongitudeLine")
        self.verticalLayout_11.addWidget(self.westBoundLongitudeLine)
        self.horizontalLayout_51.addLayout(self.verticalLayout_11)
        spacerItem97 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem97)
        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.southBoundLatitudeLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.southBoundLatitudeLine.setMinimumSize(QtCore.QSize(70, 27))
        self.southBoundLatitudeLine.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.southBoundLatitudeLine.setFont(font)
        self.southBoundLatitudeLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.southBoundLatitudeLine.setFrame(False)
        self.southBoundLatitudeLine.setObjectName("southBoundLatitudeLine")
        self.horizontalLayout_49.addWidget(self.southBoundLatitudeLine)
        spacerItem98 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem98)
        self.infoButton_11 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.infoButton_11.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_11.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_11.setText("")
        self.infoButton_11.setIcon(icon1)
        self.infoButton_11.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_11.setAutoRaise(False)
        self.infoButton_11.setObjectName("infoButton_11")
        self.horizontalLayout_49.addWidget(self.infoButton_11)
        self.verticalLayout_41.addLayout(self.horizontalLayout_49)
        spacerItem99 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_41.addItem(spacerItem99)
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.eastBoundLongitudeLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.eastBoundLongitudeLine.setMinimumSize(QtCore.QSize(70, 27))
        self.eastBoundLongitudeLine.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.eastBoundLongitudeLine.setFont(font)
        self.eastBoundLongitudeLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.eastBoundLongitudeLine.setFrame(False)
        self.eastBoundLongitudeLine.setObjectName("eastBoundLongitudeLine")
        self.horizontalLayout_46.addWidget(self.eastBoundLongitudeLine)
        spacerItem100 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem100)
        self.infoButton_12 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.infoButton_12.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_12.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_12.setText("")
        self.infoButton_12.setIcon(icon1)
        self.infoButton_12.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_12.setAutoRaise(False)
        self.infoButton_12.setObjectName("infoButton_12")
        self.horizontalLayout_46.addWidget(self.infoButton_12)
        self.verticalLayout_41.addLayout(self.horizontalLayout_46)
        self.horizontalLayout_51.addLayout(self.verticalLayout_41)
        self.horizontalLayout_81.addLayout(self.horizontalLayout_51)
        spacerItem101 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem101)
        self.verticalLayout_46 = QtWidgets.QVBoxLayout()
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_30.setMinimumSize(QtCore.QSize(150, 27))
        self.label_30.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_47.addWidget(self.label_30)
        spacerItem102 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem102)
        self.minAltitudeLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.minAltitudeLine.setMinimumSize(QtCore.QSize(90, 27))
        self.minAltitudeLine.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.minAltitudeLine.setFont(font)
        self.minAltitudeLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.minAltitudeLine.setFrame(False)
        self.minAltitudeLine.setObjectName("minAltitudeLine")
        self.horizontalLayout_47.addWidget(self.minAltitudeLine)
        spacerItem103 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem103)
        self.maxAltitudeLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.maxAltitudeLine.setMinimumSize(QtCore.QSize(90, 27))
        self.maxAltitudeLine.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.maxAltitudeLine.setFont(font)
        self.maxAltitudeLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.maxAltitudeLine.setFrame(False)
        self.maxAltitudeLine.setObjectName("maxAltitudeLine")
        self.horizontalLayout_47.addWidget(self.maxAltitudeLine)
        spacerItem104 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem104)
        self.infoButton_13 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.infoButton_13.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_13.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_13.setText("")
        self.infoButton_13.setIcon(icon1)
        self.infoButton_13.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_13.setAutoRaise(False)
        self.infoButton_13.setObjectName("infoButton_13")
        self.horizontalLayout_47.addWidget(self.infoButton_13)
        self.verticalLayout_46.addLayout(self.horizontalLayout_47)
        spacerItem105 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_46.addItem(spacerItem105)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        spacerItem106 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem106)
        self.readBoundingBoxButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.readBoundingBoxButton.setMinimumSize(QtCore.QSize(330, 27))
        self.readBoundingBoxButton.setMaximumSize(QtCore.QSize(360, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.readBoundingBoxButton.setFont(font)
        self.readBoundingBoxButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.readBoundingBoxButton.setObjectName("readBoundingBoxButton")
        self.horizontalLayout_48.addWidget(self.readBoundingBoxButton)
        spacerItem107 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem107)
        self.verticalLayout_46.addLayout(self.horizontalLayout_48)
        self.horizontalLayout_81.addLayout(self.verticalLayout_46)
        self.verticalLayout_59.addLayout(self.horizontalLayout_81)
        spacerItem108 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_59.addItem(spacerItem108)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_54.addWidget(self.label_33)
        spacerItem109 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem109)
        self.verticalLayout_59.addLayout(self.horizontalLayout_54)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem110 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem110)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.polarCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.polarCheck.setFont(font)
        self.polarCheck.setObjectName("polarCheck")
        self.gridLayout_7.addWidget(self.polarCheck, 0, 0, 1, 1)
        self.subTropicalCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.subTropicalCheck.setFont(font)
        self.subTropicalCheck.setObjectName("subTropicalCheck")
        self.gridLayout_7.addWidget(self.subTropicalCheck, 0, 1, 1, 1)
        self.maritimeCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.maritimeCheck.setFont(font)
        self.maritimeCheck.setObjectName("maritimeCheck")
        self.gridLayout_7.addWidget(self.maritimeCheck, 0, 2, 1, 1)
        self.oceanicIslandsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oceanicIslandsCheck.setFont(font)
        self.oceanicIslandsCheck.setObjectName("oceanicIslandsCheck")
        self.gridLayout_7.addWidget(self.oceanicIslandsCheck, 0, 3, 1, 1)
        self.midLatitudesCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.midLatitudesCheck.setFont(font)
        self.midLatitudesCheck.setObjectName("midLatitudesCheck")
        self.gridLayout_7.addWidget(self.midLatitudesCheck, 1, 0, 1, 1)
        self.tropicalCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tropicalCheck.setFont(font)
        self.tropicalCheck.setObjectName("tropicalCheck")
        self.gridLayout_7.addWidget(self.tropicalCheck, 1, 1, 1, 1)
        self.continentalCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.continentalCheck.setFont(font)
        self.continentalCheck.setObjectName("continentalCheck")
        self.gridLayout_7.addWidget(self.continentalCheck, 1, 2, 1, 1)
        self.geogOtherCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.geogOtherCheck.setFont(font)
        self.geogOtherCheck.setObjectName("geogOtherCheck")
        self.gridLayout_7.addWidget(self.geogOtherCheck, 1, 3, 1, 1)
        self.horizontalLayout_17.addLayout(self.gridLayout_7)
        spacerItem111 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem111)
        self.infoButton_16 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.infoButton_16.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_16.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_16.setText("")
        self.infoButton_16.setIcon(icon1)
        self.infoButton_16.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_16.setAutoRaise(False)
        self.infoButton_16.setObjectName("infoButton_16")
        self.horizontalLayout_17.addWidget(self.infoButton_16)
        self.verticalLayout_59.addLayout(self.horizontalLayout_17)
        spacerItem112 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_59.addItem(spacerItem112)
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        spacerItem113 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem113)
        self.gr_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.gr_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.gr_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gr_addButton.setFont(font)
        self.gr_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.gr_addButton.setObjectName("gr_addButton")
        self.horizontalLayout_62.addWidget(self.gr_addButton)
        spacerItem114 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem114)
        self.gr_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.gr_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.gr_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.gr_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.gr_infoButton.setText("")
        self.gr_infoButton.setIcon(icon1)
        self.gr_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.gr_infoButton.setAutoRaise(False)
        self.gr_infoButton.setObjectName("gr_infoButton")
        self.horizontalLayout_62.addWidget(self.gr_infoButton)
        spacerItem115 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem115)
        self.verticalLayout_59.addLayout(self.horizontalLayout_62)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_59.addLayout(self.gridLayout_8)
        spacerItem116 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_59.addItem(spacerItem116)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_15.setMinimumSize(QtCore.QSize(90, 27))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        spacerItem117 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem117)
        self.horizontalLayout_18.addLayout(self.verticalLayout_9)
        self.GROtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.GROtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.GROtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.GROtherTextBox.setFont(font)
        self.GROtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.GROtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GROtherTextBox.setObjectName("GROtherTextBox")
        self.horizontalLayout_18.addWidget(self.GROtherTextBox)
        self.verticalLayout_59.addLayout(self.horizontalLayout_18)
        self.gridLayout_17.addLayout(self.verticalLayout_59, 1, 1, 2, 2)
        spacerItem118 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem118, 2, 3, 1, 1)
        spacerItem119 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem119, 3, 2, 1, 1)
        self.gr_scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_31.addWidget(self.gr_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage8 = QtWidgets.QWidget()
        self.tabWidgetPage8.setObjectName("tabWidgetPage8")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tabWidgetPage8)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lo_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage8)
        self.lo_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.lo_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lo_scrollArea.setWidgetResizable(True)
        self.lo_scrollArea.setObjectName("lo_scrollArea")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        spacerItem120 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_32.addItem(spacerItem120, 0, 1, 1, 1)
        spacerItem121 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_32.addItem(spacerItem121, 1, 0, 1, 1)
        self.verticalLayout_44 = QtWidgets.QVBoxLayout()
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.oceanCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oceanCheck.setFont(font)
        self.oceanCheck.setObjectName("oceanCheck")
        self.verticalLayout_22.addWidget(self.oceanCheck)
        self.semiAridCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.semiAridCheck.setFont(font)
        self.semiAridCheck.setObjectName("semiAridCheck")
        self.verticalLayout_22.addWidget(self.semiAridCheck)
        self.seaIceCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.seaIceCheck.setFont(font)
        self.seaIceCheck.setObjectName("seaIceCheck")
        self.verticalLayout_22.addWidget(self.seaIceCheck)
        self.horizontalLayout_27.addLayout(self.verticalLayout_22)
        spacerItem122 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem122)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.desertCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.desertCheck.setFont(font)
        self.desertCheck.setObjectName("desertCheck")
        self.verticalLayout_23.addWidget(self.desertCheck)
        self.snowCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.snowCheck.setFont(font)
        self.snowCheck.setObjectName("snowCheck")
        self.verticalLayout_23.addWidget(self.snowCheck)
        self.urbanCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.urbanCheck.setFont(font)
        self.urbanCheck.setObjectName("urbanCheck")
        self.verticalLayout_23.addWidget(self.urbanCheck)
        self.horizontalLayout_27.addLayout(self.verticalLayout_23)
        spacerItem123 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem123)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.lakeIceCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lakeIceCheck.setFont(font)
        self.lakeIceCheck.setObjectName("lakeIceCheck")
        self.verticalLayout_24.addWidget(self.lakeIceCheck)
        self.forestCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.forestCheck.setFont(font)
        self.forestCheck.setObjectName("forestCheck")
        self.verticalLayout_24.addWidget(self.forestCheck)
        self.vegetationCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.vegetationCheck.setFont(font)
        self.vegetationCheck.setObjectName("vegetationCheck")
        self.verticalLayout_24.addWidget(self.vegetationCheck)
        self.horizontalLayout_27.addLayout(self.verticalLayout_24)
        spacerItem124 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem124)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.mountainousCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mountainousCheck.setFont(font)
        self.mountainousCheck.setObjectName("mountainousCheck")
        self.verticalLayout_43.addWidget(self.mountainousCheck)
        self.hillyCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hillyCheck.setFont(font)
        self.hillyCheck.setObjectName("hillyCheck")
        self.verticalLayout_43.addWidget(self.hillyCheck)
        self.flatCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.flatCheck.setFont(font)
        self.flatCheck.setObjectName("flatCheck")
        self.verticalLayout_43.addWidget(self.flatCheck)
        self.horizontalLayout_27.addLayout(self.verticalLayout_43)
        spacerItem125 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem125)
        self.infoButton_17 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.infoButton_17.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_17.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_17.setText("")
        self.infoButton_17.setIcon(icon1)
        self.infoButton_17.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_17.setAutoRaise(False)
        self.infoButton_17.setObjectName("infoButton_17")
        self.horizontalLayout_27.addWidget(self.infoButton_17)
        self.verticalLayout_44.addLayout(self.horizontalLayout_27)
        spacerItem126 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_44.addItem(spacerItem126)
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        spacerItem127 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem127)
        self.so_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.so_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.so_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.so_addButton.setFont(font)
        self.so_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.so_addButton.setObjectName("so_addButton")
        self.horizontalLayout_66.addWidget(self.so_addButton)
        spacerItem128 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem128)
        self.so_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.so_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.so_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.so_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.so_infoButton.setText("")
        self.so_infoButton.setIcon(icon1)
        self.so_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.so_infoButton.setAutoRaise(False)
        self.so_infoButton.setObjectName("so_infoButton")
        self.horizontalLayout_66.addWidget(self.so_infoButton)
        spacerItem129 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem129)
        self.verticalLayout_44.addLayout(self.horizontalLayout_66)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.verticalLayout_44.addLayout(self.gridLayout_16)
        spacerItem130 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_44.addItem(spacerItem130)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout()
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_19.setMinimumSize(QtCore.QSize(90, 27))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_53.addWidget(self.label_19)
        spacerItem131 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_53.addItem(spacerItem131)
        self.horizontalLayout_28.addLayout(self.verticalLayout_53)
        self.SOOtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_5)
        self.SOOtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.SOOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SOOtherTextBox.setFont(font)
        self.SOOtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.SOOtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SOOtherTextBox.setObjectName("SOOtherTextBox")
        self.horizontalLayout_28.addWidget(self.SOOtherTextBox)
        self.verticalLayout_44.addLayout(self.horizontalLayout_28)
        self.gridLayout_32.addLayout(self.verticalLayout_44, 1, 1, 2, 2)
        spacerItem132 = QtWidgets.QSpacerItem(152, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_32.addItem(spacerItem132, 2, 3, 1, 1)
        spacerItem133 = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_32.addItem(spacerItem133, 3, 2, 1, 1)
        self.lo_scrollArea.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_13.addWidget(self.lo_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage8, "")
        self.tabWidgetPage5 = QtWidgets.QWidget()
        self.tabWidgetPage5.setObjectName("tabWidgetPage5")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tabWidgetPage5)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.af_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage5)
        self.af_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.af_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.af_scrollArea.setWidgetResizable(True)
        self.af_scrollArea.setObjectName("af_scrollArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_33.setObjectName("gridLayout_33")
        spacerItem134 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_33.addItem(spacerItem134, 0, 1, 1, 1)
        spacerItem135 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem135, 1, 0, 1, 1)
        self.verticalLayout_61 = QtWidgets.QVBoxLayout()
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.stationaryCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stationaryCheck.setFont(font)
        self.stationaryCheck.setObjectName("stationaryCheck")
        self.verticalLayout_10.addWidget(self.stationaryCheck)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem136 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem136)
        self.stationaryCyclonicCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stationaryCyclonicCheck.setFont(font)
        self.stationaryCyclonicCheck.setObjectName("stationaryCyclonicCheck")
        self.horizontalLayout_20.addWidget(self.stationaryCyclonicCheck)
        self.verticalLayout_10.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem137 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem137)
        self.stationaryAnticyclonicCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stationaryAnticyclonicCheck.setFont(font)
        self.stationaryAnticyclonicCheck.setObjectName("stationaryAnticyclonicCheck")
        self.horizontalLayout_19.addWidget(self.stationaryAnticyclonicCheck)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.warmFrontCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.warmFrontCheck.setFont(font)
        self.warmFrontCheck.setObjectName("warmFrontCheck")
        self.verticalLayout_10.addWidget(self.warmFrontCheck)
        self.warmConveyorBeltCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.warmConveyorBeltCheck.setFont(font)
        self.warmConveyorBeltCheck.setObjectName("warmConveyorBeltCheck")
        self.verticalLayout_10.addWidget(self.warmConveyorBeltCheck)
        self.horizontalLayout_21.addLayout(self.verticalLayout_10)
        spacerItem138 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem138)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.arcticColdAirOutbreakCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.arcticColdAirOutbreakCheck.setFont(font)
        self.arcticColdAirOutbreakCheck.setObjectName("arcticColdAirOutbreakCheck")
        self.verticalLayout_13.addWidget(self.arcticColdAirOutbreakCheck)
        self.coldFrontCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.coldFrontCheck.setFont(font)
        self.coldFrontCheck.setObjectName("coldFrontCheck")
        self.verticalLayout_13.addWidget(self.coldFrontCheck)
        self.occludedFrontCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.occludedFrontCheck.setFont(font)
        self.occludedFrontCheck.setObjectName("occludedFrontCheck")
        self.verticalLayout_13.addWidget(self.occludedFrontCheck)
        self.warmSectorCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.warmSectorCheck.setFont(font)
        self.warmSectorCheck.setObjectName("warmSectorCheck")
        self.verticalLayout_13.addWidget(self.warmSectorCheck)
        self.postColdFrontalAirMassCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.postColdFrontalAirMassCheck.setFont(font)
        self.postColdFrontalAirMassCheck.setObjectName("postColdFrontalAirMassCheck")
        self.verticalLayout_13.addWidget(self.postColdFrontalAirMassCheck)
        self.horizontalLayout_21.addLayout(self.verticalLayout_13)
        spacerItem139 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem139)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.orographicInfluenceCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.orographicInfluenceCheck.setFont(font)
        self.orographicInfluenceCheck.setObjectName("orographicInfluenceCheck")
        self.verticalLayout_14.addWidget(self.orographicInfluenceCheck)
        self.seaBreezeFrontCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.seaBreezeFrontCheck.setFont(font)
        self.seaBreezeFrontCheck.setObjectName("seaBreezeFrontCheck")
        self.verticalLayout_14.addWidget(self.seaBreezeFrontCheck)
        self.stratosphericFoldCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stratosphericFoldCheck.setFont(font)
        self.stratosphericFoldCheck.setObjectName("stratosphericFoldCheck")
        self.verticalLayout_14.addWidget(self.stratosphericFoldCheck)
        self.extendedConvergenceLineCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.extendedConvergenceLineCheck.setFont(font)
        self.extendedConvergenceLineCheck.setObjectName("extendedConvergenceLineCheck")
        self.verticalLayout_14.addWidget(self.extendedConvergenceLineCheck)
        self.horizontalLayout_21.addLayout(self.verticalLayout_14)
        spacerItem140 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem140)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.easterlyWaveCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.easterlyWaveCheck.setFont(font)
        self.easterlyWaveCheck.setObjectName("easterlyWaveCheck")
        self.verticalLayout_15.addWidget(self.easterlyWaveCheck)
        self.equatorialWaveCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.equatorialWaveCheck.setFont(font)
        self.equatorialWaveCheck.setObjectName("equatorialWaveCheck")
        self.verticalLayout_15.addWidget(self.equatorialWaveCheck)
        self.tropicalCycloneCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tropicalCycloneCheck.setFont(font)
        self.tropicalCycloneCheck.setObjectName("tropicalCycloneCheck")
        self.verticalLayout_15.addWidget(self.tropicalCycloneCheck)
        self.mesoscaleOrganizedConvectionCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        self.mesoscaleOrganizedConvectionCheck.setMinimumSize(QtCore.QSize(0, 0))
        self.mesoscaleOrganizedConvectionCheck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mesoscaleOrganizedConvectionCheck.setFont(font)
        self.mesoscaleOrganizedConvectionCheck.setAutoFillBackground(False)
        self.mesoscaleOrganizedConvectionCheck.setChecked(False)
        self.mesoscaleOrganizedConvectionCheck.setAutoRepeat(False)
        self.mesoscaleOrganizedConvectionCheck.setAutoExclusive(False)
        self.mesoscaleOrganizedConvectionCheck.setTristate(False)
        self.mesoscaleOrganizedConvectionCheck.setObjectName("mesoscaleOrganizedConvectionCheck")
        self.verticalLayout_15.addWidget(self.mesoscaleOrganizedConvectionCheck)
        self.horizontalLayout_21.addLayout(self.verticalLayout_15)
        spacerItem141 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem141)
        self.infoButton_18 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.infoButton_18.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_18.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_18.setText("")
        self.infoButton_18.setIcon(icon1)
        self.infoButton_18.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_18.setAutoRaise(False)
        self.infoButton_18.setObjectName("infoButton_18")
        self.horizontalLayout_21.addWidget(self.infoButton_18)
        self.verticalLayout_61.addLayout(self.horizontalLayout_21)
        spacerItem142 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_61.addItem(spacerItem142)
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        spacerItem143 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem143)
        self.af_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.af_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.af_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_addButton.setFont(font)
        self.af_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.af_addButton.setObjectName("af_addButton")
        self.horizontalLayout_63.addWidget(self.af_addButton)
        spacerItem144 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem144)
        self.af_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.af_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.af_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.af_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.af_infoButton.setText("")
        self.af_infoButton.setIcon(icon1)
        self.af_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.af_infoButton.setAutoRaise(False)
        self.af_infoButton.setObjectName("af_infoButton")
        self.horizontalLayout_63.addWidget(self.af_infoButton)
        spacerItem145 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem145)
        self.verticalLayout_61.addLayout(self.horizontalLayout_63)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_61.addLayout(self.gridLayout_9)
        spacerItem146 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_61.addItem(spacerItem146)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout()
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_16.setMinimumSize(QtCore.QSize(90, 27))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_47.addWidget(self.label_16)
        spacerItem147 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_47.addItem(spacerItem147)
        self.horizontalLayout_22.addLayout(self.verticalLayout_47)
        self.AFOtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_6)
        self.AFOtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.AFOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.AFOtherTextBox.setFont(font)
        self.AFOtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.AFOtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AFOtherTextBox.setObjectName("AFOtherTextBox")
        self.horizontalLayout_22.addWidget(self.AFOtherTextBox)
        self.verticalLayout_61.addLayout(self.horizontalLayout_22)
        self.gridLayout_33.addLayout(self.verticalLayout_61, 1, 1, 1, 2)
        spacerItem148 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem148, 1, 3, 1, 1)
        spacerItem149 = QtWidgets.QSpacerItem(20, 105, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem149, 2, 2, 1, 1)
        self.af_scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_18.addWidget(self.af_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage5, "")
        self.tabWidgetPage6 = QtWidgets.QWidget()
        self.tabWidgetPage6.setObjectName("tabWidgetPage6")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tabWidgetPage6)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.ct_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage6)
        self.ct_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ct_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ct_scrollArea.setWidgetResizable(True)
        self.ct_scrollArea.setObjectName("ct_scrollArea")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34.setObjectName("gridLayout_34")
        spacerItem150 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_34.addItem(spacerItem150, 0, 1, 1, 1)
        spacerItem151 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem151, 1, 0, 1, 1)
        self.verticalLayout_62 = QtWidgets.QVBoxLayout()
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.waterCloudsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.waterCloudsCheck.setFont(font)
        self.waterCloudsCheck.setObjectName("waterCloudsCheck")
        self.verticalLayout_16.addWidget(self.waterCloudsCheck)
        self.mixedPhaseCloudsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mixedPhaseCloudsCheck.setFont(font)
        self.mixedPhaseCloudsCheck.setObjectName("mixedPhaseCloudsCheck")
        self.verticalLayout_16.addWidget(self.mixedPhaseCloudsCheck)
        self.iceCloudsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.iceCloudsCheck.setFont(font)
        self.iceCloudsCheck.setObjectName("iceCloudsCheck")
        self.verticalLayout_16.addWidget(self.iceCloudsCheck)
        self.cirrusCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cirrusCheck.setFont(font)
        self.cirrusCheck.setObjectName("cirrusCheck")
        self.verticalLayout_16.addWidget(self.cirrusCheck)
        self.horizontalLayout_23.addLayout(self.verticalLayout_16)
        spacerItem152 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem152)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.contrailsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contrailsCheck.setFont(font)
        self.contrailsCheck.setObjectName("contrailsCheck")
        self.verticalLayout_17.addWidget(self.contrailsCheck)
        self.stratocumulusCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stratocumulusCheck.setFont(font)
        self.stratocumulusCheck.setObjectName("stratocumulusCheck")
        self.verticalLayout_17.addWidget(self.stratocumulusCheck)
        self.shallowCumulusCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.shallowCumulusCheck.setFont(font)
        self.shallowCumulusCheck.setObjectName("shallowCumulusCheck")
        self.verticalLayout_17.addWidget(self.shallowCumulusCheck)
        self.cumulusCongestusCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cumulusCongestusCheck.setFont(font)
        self.cumulusCongestusCheck.setObjectName("cumulusCongestusCheck")
        self.verticalLayout_17.addWidget(self.cumulusCongestusCheck)
        self.horizontalLayout_23.addLayout(self.verticalLayout_17)
        spacerItem153 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem153)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.cumulonimbusToweringCumulusCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cumulonimbusToweringCumulusCheck.setFont(font)
        self.cumulonimbusToweringCumulusCheck.setObjectName("cumulonimbusToweringCumulusCheck")
        self.verticalLayout_18.addWidget(self.cumulonimbusToweringCumulusCheck)
        self.altostratusAltocumulusCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.altostratusAltocumulusCheck.setFont(font)
        self.altostratusAltocumulusCheck.setObjectName("altostratusAltocumulusCheck")
        self.verticalLayout_18.addWidget(self.altostratusAltocumulusCheck)
        self.waveCloudsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.waveCloudsCheck.setFont(font)
        self.waveCloudsCheck.setObjectName("waveCloudsCheck")
        self.verticalLayout_18.addWidget(self.waveCloudsCheck)
        self.horizontalLayout_23.addLayout(self.verticalLayout_18)
        spacerItem154 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem154)
        self.verticalLayout_48 = QtWidgets.QVBoxLayout()
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.deepFrontalStratiformCloudsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.deepFrontalStratiformCloudsCheck.setFont(font)
        self.deepFrontalStratiformCloudsCheck.setObjectName("deepFrontalStratiformCloudsCheck")
        self.verticalLayout_48.addWidget(self.deepFrontalStratiformCloudsCheck)
        self.cloudFreeAboveAircraftCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudFreeAboveAircraftCheck.setFont(font)
        self.cloudFreeAboveAircraftCheck.setObjectName("cloudFreeAboveAircraftCheck")
        self.verticalLayout_48.addWidget(self.cloudFreeAboveAircraftCheck)
        self.cloudFreeBelowAircraftCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudFreeBelowAircraftCheck.setFont(font)
        self.cloudFreeBelowAircraftCheck.setObjectName("cloudFreeBelowAircraftCheck")
        self.verticalLayout_48.addWidget(self.cloudFreeBelowAircraftCheck)
        self.horizontalLayout_23.addLayout(self.verticalLayout_48)
        self.infoButton_19 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_7)
        self.infoButton_19.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_19.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_19.setText("")
        self.infoButton_19.setIcon(icon1)
        self.infoButton_19.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_19.setAutoRaise(False)
        self.infoButton_19.setObjectName("infoButton_19")
        self.horizontalLayout_23.addWidget(self.infoButton_19)
        self.verticalLayout_62.addLayout(self.horizontalLayout_23)
        spacerItem155 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_62.addItem(spacerItem155)
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        spacerItem156 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem156)
        self.ct_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_7)
        self.ct_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.ct_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ct_addButton.setFont(font)
        self.ct_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.ct_addButton.setObjectName("ct_addButton")
        self.horizontalLayout_64.addWidget(self.ct_addButton)
        spacerItem157 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem157)
        self.ct_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_7)
        self.ct_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.ct_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.ct_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ct_infoButton.setText("")
        self.ct_infoButton.setIcon(icon1)
        self.ct_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.ct_infoButton.setAutoRaise(False)
        self.ct_infoButton.setObjectName("ct_infoButton")
        self.horizontalLayout_64.addWidget(self.ct_infoButton)
        spacerItem158 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem158)
        self.verticalLayout_62.addLayout(self.horizontalLayout_64)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_62.addLayout(self.gridLayout_10)
        spacerItem159 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_62.addItem(spacerItem159)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout()
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_17.setMinimumSize(QtCore.QSize(90, 27))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_49.addWidget(self.label_17)
        spacerItem160 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_49.addItem(spacerItem160)
        self.horizontalLayout_24.addLayout(self.verticalLayout_49)
        self.CTOtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_7)
        self.CTOtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.CTOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.CTOtherTextBox.setFont(font)
        self.CTOtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.CTOtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CTOtherTextBox.setObjectName("CTOtherTextBox")
        self.horizontalLayout_24.addWidget(self.CTOtherTextBox)
        self.verticalLayout_62.addLayout(self.horizontalLayout_24)
        self.gridLayout_34.addLayout(self.verticalLayout_62, 1, 1, 2, 2)
        spacerItem161 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem161, 2, 3, 1, 1)
        spacerItem162 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_34.addItem(spacerItem162, 3, 2, 1, 1)
        self.ct_scrollArea.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_19.addWidget(self.ct_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage6, "")
        self.tabWidgetPage7 = QtWidgets.QWidget()
        self.tabWidgetPage7.setObjectName("tabWidgetPage7")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tabWidgetPage7)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.cp_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage7)
        self.cp_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.cp_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cp_scrollArea.setWidgetResizable(True)
        self.cp_scrollArea.setObjectName("cp_scrollArea")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_35.setObjectName("gridLayout_35")
        spacerItem163 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_35.addItem(spacerItem163, 0, 2, 1, 1)
        spacerItem164 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem164, 1, 0, 1, 1)
        self.verticalLayout_63 = QtWidgets.QVBoxLayout()
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout()
        self.verticalLayout_50.setSpacing(7)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.rainCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.rainCheck.setFont(font)
        self.rainCheck.setObjectName("rainCheck")
        self.verticalLayout_50.addWidget(self.rainCheck)
        self.drizzleCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.drizzleCheck.setFont(font)
        self.drizzleCheck.setObjectName("drizzleCheck")
        self.verticalLayout_50.addWidget(self.drizzleCheck)
        self.dropletsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dropletsCheck.setFont(font)
        self.dropletsCheck.setObjectName("dropletsCheck")
        self.verticalLayout_50.addWidget(self.dropletsCheck)
        self.horizontalLayout_25.addLayout(self.verticalLayout_50)
        spacerItem165 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem165)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setSpacing(7)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.pristineIceCrystalsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pristineIceCrystalsCheck.setFont(font)
        self.pristineIceCrystalsCheck.setObjectName("pristineIceCrystalsCheck")
        self.verticalLayout_21.addWidget(self.pristineIceCrystalsCheck)
        self.snowOrAggregatesCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.snowOrAggregatesCheck.setFont(font)
        self.snowOrAggregatesCheck.setObjectName("snowOrAggregatesCheck")
        self.verticalLayout_21.addWidget(self.snowOrAggregatesCheck)
        self.graupelOrHailCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.graupelOrHailCheck.setFont(font)
        self.graupelOrHailCheck.setObjectName("graupelOrHailCheck")
        self.verticalLayout_21.addWidget(self.graupelOrHailCheck)
        self.horizontalLayout_25.addLayout(self.verticalLayout_21)
        spacerItem166 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem166)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.seaSaltAerosolCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.seaSaltAerosolCheck.setFont(font)
        self.seaSaltAerosolCheck.setObjectName("seaSaltAerosolCheck")
        self.verticalLayout_20.addWidget(self.seaSaltAerosolCheck)
        self.continentalAerosolCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.continentalAerosolCheck.setFont(font)
        self.continentalAerosolCheck.setObjectName("continentalAerosolCheck")
        self.verticalLayout_20.addWidget(self.continentalAerosolCheck)
        self.urbanPlumeCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.urbanPlumeCheck.setFont(font)
        self.urbanPlumeCheck.setObjectName("urbanPlumeCheck")
        self.verticalLayout_20.addWidget(self.urbanPlumeCheck)
        self.horizontalLayout_25.addLayout(self.verticalLayout_20)
        spacerItem167 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem167)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(7)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.biomassBurningCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.biomassBurningCheck.setFont(font)
        self.biomassBurningCheck.setObjectName("biomassBurningCheck")
        self.verticalLayout_19.addWidget(self.biomassBurningCheck)
        self.desertOrMineralDustCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.desertOrMineralDustCheck.setFont(font)
        self.desertOrMineralDustCheck.setObjectName("desertOrMineralDustCheck")
        self.verticalLayout_19.addWidget(self.desertOrMineralDustCheck)
        self.volcanicAshCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.volcanicAshCheck.setFont(font)
        self.volcanicAshCheck.setObjectName("volcanicAshCheck")
        self.verticalLayout_19.addWidget(self.volcanicAshCheck)
        self.horizontalLayout_25.addLayout(self.verticalLayout_19)
        spacerItem168 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem168)
        self.infoButton_20 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_8)
        self.infoButton_20.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_20.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_20.setText("")
        self.infoButton_20.setIcon(icon1)
        self.infoButton_20.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_20.setAutoRaise(False)
        self.infoButton_20.setObjectName("infoButton_20")
        self.horizontalLayout_25.addWidget(self.infoButton_20)
        self.verticalLayout_63.addLayout(self.horizontalLayout_25)
        spacerItem169 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_63.addItem(spacerItem169)
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        spacerItem170 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem170)
        self.ps_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_8)
        self.ps_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.ps_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ps_addButton.setFont(font)
        self.ps_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.ps_addButton.setObjectName("ps_addButton")
        self.horizontalLayout_65.addWidget(self.ps_addButton)
        spacerItem171 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem171)
        self.ps_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_8)
        self.ps_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.ps_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.ps_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ps_infoButton.setText("")
        self.ps_infoButton.setIcon(icon1)
        self.ps_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.ps_infoButton.setAutoRaise(False)
        self.ps_infoButton.setObjectName("ps_infoButton")
        self.horizontalLayout_65.addWidget(self.ps_infoButton)
        spacerItem172 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem172)
        self.verticalLayout_63.addLayout(self.horizontalLayout_65)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_63.addLayout(self.gridLayout_11)
        spacerItem173 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_63.addItem(spacerItem173)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout()
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_18.setMinimumSize(QtCore.QSize(90, 27))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_51.addWidget(self.label_18)
        spacerItem174 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_51.addItem(spacerItem174)
        self.horizontalLayout_26.addLayout(self.verticalLayout_51)
        self.PSOtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_8)
        self.PSOtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.PSOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.PSOtherTextBox.setFont(font)
        self.PSOtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.PSOtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PSOtherTextBox.setObjectName("PSOtherTextBox")
        self.horizontalLayout_26.addWidget(self.PSOtherTextBox)
        self.verticalLayout_63.addLayout(self.horizontalLayout_26)
        self.gridLayout_35.addLayout(self.verticalLayout_63, 1, 1, 2, 2)
        spacerItem175 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem175, 2, 3, 1, 1)
        spacerItem176 = QtWidgets.QSpacerItem(20, 175, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_35.addItem(spacerItem176, 3, 1, 1, 1)
        self.cp_scrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_20.addWidget(self.cp_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage7, "")
        self.tabWidgetPage9 = QtWidgets.QWidget()
        self.tabWidgetPage9.setObjectName("tabWidgetPage9")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tabWidgetPage9)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.ar_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage9)
        self.ar_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ar_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ar_scrollArea.setWidgetResizable(True)
        self.ar_scrollArea.setObjectName("ar_scrollArea")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_36.setObjectName("gridLayout_36")
        spacerItem177 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_36.addItem(spacerItem177, 0, 1, 1, 1)
        spacerItem178 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem178, 1, 0, 1, 1)
        self.verticalLayout_68 = QtWidgets.QVBoxLayout()
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.boundaryLayerCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.boundaryLayerCheck.setFont(font)
        self.boundaryLayerCheck.setObjectName("boundaryLayerCheck")
        self.horizontalLayout_32.addWidget(self.boundaryLayerCheck)
        spacerItem179 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem179)
        self.verticalLayout_25.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem180 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem180)
        self.blSubCloudCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.blSubCloudCheck.setFont(font)
        self.blSubCloudCheck.setObjectName("blSubCloudCheck")
        self.horizontalLayout_30.addWidget(self.blSubCloudCheck)
        spacerItem181 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem181)
        self.blNearSurfaceCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.blNearSurfaceCheck.setFont(font)
        self.blNearSurfaceCheck.setObjectName("blNearSurfaceCheck")
        self.horizontalLayout_30.addWidget(self.blNearSurfaceCheck)
        self.verticalLayout_25.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem182 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem182)
        self.blInCloudCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.blInCloudCheck.setFont(font)
        self.blInCloudCheck.setObjectName("blInCloudCheck")
        self.horizontalLayout_29.addWidget(self.blInCloudCheck)
        spacerItem183 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem183)
        self.verticalLayout_25.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_31.addLayout(self.verticalLayout_25)
        spacerItem184 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem184)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.upperTroposphereCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.upperTroposphereCheck.setFont(font)
        self.upperTroposphereCheck.setObjectName("upperTroposphereCheck")
        self.verticalLayout_26.addWidget(self.upperTroposphereCheck)
        self.midTroposphereCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.midTroposphereCheck.setFont(font)
        self.midTroposphereCheck.setObjectName("midTroposphereCheck")
        self.verticalLayout_26.addWidget(self.midTroposphereCheck)
        spacerItem185 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem185)
        self.horizontalLayout_31.addLayout(self.verticalLayout_26)
        spacerItem186 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem186)
        self.verticalLayout_65 = QtWidgets.QVBoxLayout()
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.lowerTroposphereCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lowerTroposphereCheck.setFont(font)
        self.lowerTroposphereCheck.setObjectName("lowerTroposphereCheck")
        self.verticalLayout_65.addWidget(self.lowerTroposphereCheck)
        self.lowerStratosphereCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lowerStratosphereCheck.setFont(font)
        self.lowerStratosphereCheck.setObjectName("lowerStratosphereCheck")
        self.verticalLayout_65.addWidget(self.lowerStratosphereCheck)
        spacerItem187 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_65.addItem(spacerItem187)
        self.horizontalLayout_31.addLayout(self.verticalLayout_65)
        spacerItem188 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem188)
        self.infoButton_21 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_9)
        self.infoButton_21.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_21.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_21.setText("")
        self.infoButton_21.setIcon(icon1)
        self.infoButton_21.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_21.setAutoRaise(False)
        self.infoButton_21.setObjectName("infoButton_21")
        self.horizontalLayout_31.addWidget(self.infoButton_21)
        self.verticalLayout_68.addLayout(self.horizontalLayout_31)
        spacerItem189 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_68.addItem(spacerItem189)
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        spacerItem190 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem190)
        self.ar_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_9)
        self.ar_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.ar_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ar_addButton.setFont(font)
        self.ar_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.ar_addButton.setObjectName("ar_addButton")
        self.horizontalLayout_67.addWidget(self.ar_addButton)
        spacerItem191 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem191)
        self.ar_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_9)
        self.ar_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.ar_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.ar_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ar_infoButton.setText("")
        self.ar_infoButton.setIcon(icon1)
        self.ar_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.ar_infoButton.setAutoRaise(False)
        self.ar_infoButton.setObjectName("ar_infoButton")
        self.horizontalLayout_67.addWidget(self.ar_infoButton)
        spacerItem192 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem192)
        self.verticalLayout_68.addLayout(self.horizontalLayout_67)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_68.addLayout(self.gridLayout_14)
        spacerItem193 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_68.addItem(spacerItem193)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_20.setMinimumSize(QtCore.QSize(90, 27))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_27.addWidget(self.label_20)
        spacerItem194 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem194)
        self.horizontalLayout_33.addLayout(self.verticalLayout_27)
        self.AROtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_9)
        self.AROtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.AROtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.AROtherTextBox.setFont(font)
        self.AROtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.AROtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AROtherTextBox.setObjectName("AROtherTextBox")
        self.horizontalLayout_33.addWidget(self.AROtherTextBox)
        self.verticalLayout_68.addLayout(self.horizontalLayout_33)
        self.gridLayout_36.addLayout(self.verticalLayout_68, 1, 1, 1, 2)
        spacerItem195 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem195, 1, 3, 1, 1)
        spacerItem196 = QtWidgets.QSpacerItem(20, 169, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_36.addItem(spacerItem196, 2, 2, 1, 1)
        self.ar_scrollArea.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_21.addWidget(self.ar_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage9, "")
        self.tabWidgetPage10 = QtWidgets.QWidget()
        self.tabWidgetPage10.setObjectName("tabWidgetPage10")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tabWidgetPage10)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.fm_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage10)
        self.fm_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.fm_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fm_scrollArea.setWidgetResizable(True)
        self.fm_scrollArea.setObjectName("fm_scrollArea")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_37.setObjectName("gridLayout_37")
        spacerItem197 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_37.addItem(spacerItem197, 0, 1, 1, 1)
        spacerItem198 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem198, 1, 0, 1, 1)
        self.verticalLayout_70 = QtWidgets.QVBoxLayout()
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.straightLevelRunsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.straightLevelRunsCheck.setFont(font)
        self.straightLevelRunsCheck.setObjectName("straightLevelRunsCheck")
        self.verticalLayout_28.addWidget(self.straightLevelRunsCheck)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        spacerItem199 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem199)
        self.stackedStraightLevelRunsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stackedStraightLevelRunsCheck.setFont(font)
        self.stackedStraightLevelRunsCheck.setObjectName("stackedStraightLevelRunsCheck")
        self.horizontalLayout_34.addWidget(self.stackedStraightLevelRunsCheck)
        spacerItem200 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem200)
        self.verticalLayout_28.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        spacerItem201 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem201)
        self.separatedStraightLevelRuns = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.separatedStraightLevelRuns.setFont(font)
        self.separatedStraightLevelRuns.setObjectName("separatedStraightLevelRuns")
        self.horizontalLayout_35.addWidget(self.separatedStraightLevelRuns)
        spacerItem202 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem202)
        self.verticalLayout_28.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36.addLayout(self.verticalLayout_28)
        spacerItem203 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem203)
        self.verticalLayout_69 = QtWidgets.QVBoxLayout()
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.racetracksCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.racetracksCheck.setFont(font)
        self.racetracksCheck.setObjectName("racetracksCheck")
        self.verticalLayout_69.addWidget(self.racetracksCheck)
        self.orbitsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.orbitsCheck.setFont(font)
        self.orbitsCheck.setObjectName("orbitsCheck")
        self.verticalLayout_69.addWidget(self.orbitsCheck)
        spacerItem204 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_69.addItem(spacerItem204)
        self.horizontalLayout_36.addLayout(self.verticalLayout_69)
        spacerItem205 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem205)
        self.verticalLayout_66 = QtWidgets.QVBoxLayout()
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.lagrangianDescentsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lagrangianDescentsCheck.setFont(font)
        self.lagrangianDescentsCheck.setObjectName("lagrangianDescentsCheck")
        self.verticalLayout_66.addWidget(self.lagrangianDescentsCheck)
        self.deepProfileAscentDescentsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.deepProfileAscentDescentsCheck.setFont(font)
        self.deepProfileAscentDescentsCheck.setObjectName("deepProfileAscentDescentsCheck")
        self.verticalLayout_66.addWidget(self.deepProfileAscentDescentsCheck)
        spacerItem206 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_66.addItem(spacerItem206)
        self.horizontalLayout_36.addLayout(self.verticalLayout_66)
        spacerItem207 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem207)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.dropsondeDeployedCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dropsondeDeployedCheck.setFont(font)
        self.dropsondeDeployedCheck.setObjectName("dropsondeDeployedCheck")
        self.verticalLayout_29.addWidget(self.dropsondeDeployedCheck)
        self.selfCalibrationCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.selfCalibrationCheck.setFont(font)
        self.selfCalibrationCheck.setObjectName("selfCalibrationCheck")
        self.verticalLayout_29.addWidget(self.selfCalibrationCheck)
        spacerItem208 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem208)
        self.horizontalLayout_36.addLayout(self.verticalLayout_29)
        spacerItem209 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem209)
        self.infoButton_22 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_10)
        self.infoButton_22.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_22.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_22.setText("")
        self.infoButton_22.setIcon(icon1)
        self.infoButton_22.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_22.setAutoRaise(False)
        self.infoButton_22.setObjectName("infoButton_22")
        self.horizontalLayout_36.addWidget(self.infoButton_22)
        self.verticalLayout_70.addLayout(self.horizontalLayout_36)
        spacerItem210 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_70.addItem(spacerItem210)
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        spacerItem211 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem211)
        self.fm_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_10)
        self.fm_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.fm_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fm_addButton.setFont(font)
        self.fm_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.fm_addButton.setObjectName("fm_addButton")
        self.horizontalLayout_68.addWidget(self.fm_addButton)
        spacerItem212 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem212)
        self.fm_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_10)
        self.fm_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.fm_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.fm_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.fm_infoButton.setText("")
        self.fm_infoButton.setIcon(icon1)
        self.fm_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.fm_infoButton.setAutoRaise(False)
        self.fm_infoButton.setObjectName("fm_infoButton")
        self.horizontalLayout_68.addWidget(self.fm_infoButton)
        spacerItem213 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem213)
        self.verticalLayout_70.addLayout(self.horizontalLayout_68)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.verticalLayout_70.addLayout(self.gridLayout_15)
        spacerItem214 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_70.addItem(spacerItem214)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_21.setMinimumSize(QtCore.QSize(90, 27))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_30.addWidget(self.label_21)
        spacerItem215 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_30.addItem(spacerItem215)
        self.horizontalLayout_37.addLayout(self.verticalLayout_30)
        self.FTOtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_10)
        self.FTOtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.FTOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.FTOtherTextBox.setFont(font)
        self.FTOtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.FTOtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FTOtherTextBox.setObjectName("FTOtherTextBox")
        self.horizontalLayout_37.addWidget(self.FTOtherTextBox)
        self.verticalLayout_70.addLayout(self.horizontalLayout_37)
        self.gridLayout_37.addLayout(self.verticalLayout_70, 1, 1, 2, 1)
        spacerItem216 = QtWidgets.QSpacerItem(152, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem216, 2, 2, 1, 1)
        spacerItem217 = QtWidgets.QSpacerItem(20, 174, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_37.addItem(spacerItem217, 3, 1, 1, 1)
        self.fm_scrollArea.setWidget(self.scrollAreaWidgetContents_10)
        self.gridLayout_23.addWidget(self.fm_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage10, "")
        self.tabWidgetPage11 = QtWidgets.QWidget()
        self.tabWidgetPage11.setObjectName("tabWidgetPage11")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tabWidgetPage11)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.sc_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage11)
        self.sc_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.sc_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sc_scrollArea.setWidgetResizable(True)
        self.sc_scrollArea.setObjectName("sc_scrollArea")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_38.setObjectName("gridLayout_38")
        spacerItem218 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_38.addItem(spacerItem218, 0, 1, 1, 1)
        spacerItem219 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem219, 1, 0, 1, 1)
        self.verticalLayout_67 = QtWidgets.QVBoxLayout()
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_31.addWidget(self.label_22)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        spacerItem220 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem220)
        self.polarAtrainCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.polarAtrainCheck.setFont(font)
        self.polarAtrainCheck.setObjectName("polarAtrainCheck")
        self.horizontalLayout_40.addWidget(self.polarAtrainCheck)
        self.verticalLayout_31.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        spacerItem221 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem221)
        self.polarMetopCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.polarMetopCheck.setFont(font)
        self.polarMetopCheck.setObjectName("polarMetopCheck")
        self.horizontalLayout_38.addWidget(self.polarMetopCheck)
        self.verticalLayout_31.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        spacerItem222 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem222)
        self.polarNpoessCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.polarNpoessCheck.setFont(font)
        self.polarNpoessCheck.setObjectName("polarNpoessCheck")
        self.horizontalLayout_39.addWidget(self.polarNpoessCheck)
        self.verticalLayout_31.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        spacerItem223 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem223)
        self.polarOtherCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.polarOtherCheck.setFont(font)
        self.polarOtherCheck.setObjectName("polarOtherCheck")
        self.horizontalLayout_41.addWidget(self.polarOtherCheck)
        self.verticalLayout_31.addLayout(self.horizontalLayout_41)
        self.horizontalLayout_44.addLayout(self.verticalLayout_31)
        spacerItem224 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem224)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_32.addWidget(self.label_23)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        spacerItem225 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem225)
        self.geosynchMsgCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.geosynchMsgCheck.setFont(font)
        self.geosynchMsgCheck.setObjectName("geosynchMsgCheck")
        self.horizontalLayout_42.addWidget(self.geosynchMsgCheck)
        self.verticalLayout_32.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        spacerItem226 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem226)
        self.geosynchOtherCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.geosynchOtherCheck.setFont(font)
        self.geosynchOtherCheck.setObjectName("geosynchOtherCheck")
        self.horizontalLayout_43.addWidget(self.geosynchOtherCheck)
        self.verticalLayout_32.addLayout(self.horizontalLayout_43)
        spacerItem227 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_32.addItem(spacerItem227)
        self.horizontalLayout_44.addLayout(self.verticalLayout_32)
        spacerItem228 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem228)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.airsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.airsCheck.setFont(font)
        self.airsCheck.setObjectName("airsCheck")
        self.verticalLayout_33.addWidget(self.airsCheck)
        self.amsuMhsCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.amsuMhsCheck.setFont(font)
        self.amsuMhsCheck.setObjectName("amsuMhsCheck")
        self.verticalLayout_33.addWidget(self.amsuMhsCheck)
        self.caliopCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.caliopCheck.setFont(font)
        self.caliopCheck.setObjectName("caliopCheck")
        self.verticalLayout_33.addWidget(self.caliopCheck)
        self.cloudsatCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudsatCheck.setFont(font)
        self.cloudsatCheck.setObjectName("cloudsatCheck")
        self.verticalLayout_33.addWidget(self.cloudsatCheck)
        spacerItem229 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_33.addItem(spacerItem229)
        self.horizontalLayout_44.addLayout(self.verticalLayout_33)
        spacerItem230 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem230)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.crisCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.crisCheck.setFont(font)
        self.crisCheck.setObjectName("crisCheck")
        self.verticalLayout_34.addWidget(self.crisCheck)
        self.iasiCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.iasiCheck.setFont(font)
        self.iasiCheck.setObjectName("iasiCheck")
        self.verticalLayout_34.addWidget(self.iasiCheck)
        self.modisCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.modisCheck.setFont(font)
        self.modisCheck.setObjectName("modisCheck")
        self.verticalLayout_34.addWidget(self.modisCheck)
        spacerItem231 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_34.addItem(spacerItem231)
        self.horizontalLayout_44.addLayout(self.verticalLayout_34)
        spacerItem232 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem232)
        self.infoButton_23 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_11)
        self.infoButton_23.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_23.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_23.setText("")
        self.infoButton_23.setIcon(icon1)
        self.infoButton_23.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_23.setAutoRaise(False)
        self.infoButton_23.setObjectName("infoButton_23")
        self.horizontalLayout_44.addWidget(self.infoButton_23)
        self.verticalLayout_67.addLayout(self.horizontalLayout_44)
        spacerItem233 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_67.addItem(spacerItem233)
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        spacerItem234 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem234)
        self.sc_addButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_11)
        self.sc_addButton.setMinimumSize(QtCore.QSize(180, 27))
        self.sc_addButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sc_addButton.setFont(font)
        self.sc_addButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.sc_addButton.setObjectName("sc_addButton")
        self.horizontalLayout_69.addWidget(self.sc_addButton)
        spacerItem235 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem235)
        self.sc_infoButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_11)
        self.sc_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.sc_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.sc_infoButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.sc_infoButton.setText("")
        self.sc_infoButton.setIcon(icon1)
        self.sc_infoButton.setIconSize(QtCore.QSize(23, 23))
        self.sc_infoButton.setAutoRaise(False)
        self.sc_infoButton.setObjectName("sc_infoButton")
        self.horizontalLayout_69.addWidget(self.sc_infoButton)
        spacerItem236 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem236)
        self.verticalLayout_67.addLayout(self.horizontalLayout_69)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.verticalLayout_67.addLayout(self.gridLayout_25)
        spacerItem237 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_67.addItem(spacerItem237)
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_24.setMinimumSize(QtCore.QSize(90, 27))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_35.addWidget(self.label_24)
        spacerItem238 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_35.addItem(spacerItem238)
        self.horizontalLayout_45.addLayout(self.verticalLayout_35)
        self.SCOtherTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_11)
        self.SCOtherTextBox.setMinimumSize(QtCore.QSize(750, 100))
        self.SCOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SCOtherTextBox.setFont(font)
        self.SCOtherTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.SCOtherTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SCOtherTextBox.setObjectName("SCOtherTextBox")
        self.horizontalLayout_45.addWidget(self.SCOtherTextBox)
        self.verticalLayout_67.addLayout(self.horizontalLayout_45)
        self.gridLayout_38.addLayout(self.verticalLayout_67, 1, 1, 2, 1)
        spacerItem239 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem239, 2, 2, 1, 1)
        spacerItem240 = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_38.addItem(spacerItem240, 3, 1, 1, 1)
        self.sc_scrollArea.setWidget(self.scrollAreaWidgetContents_11)
        self.gridLayout_24.addWidget(self.sc_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage11, "")
        self.tabWidgetPage12 = QtWidgets.QWidget()
        self.tabWidgetPage12.setObjectName("tabWidgetPage12")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.tabWidgetPage12)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.so_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage12)
        self.so_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.so_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.so_scrollArea.setWidgetResizable(True)
        self.so_scrollArea.setObjectName("so_scrollArea")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_12)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem241 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem241, 0, 1, 1, 1)
        spacerItem242 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem242, 1, 0, 1, 1)
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout()
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout()
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_55.addWidget(self.label_26)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.groundListWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_12)
        self.groundListWidget.setMinimumSize(QtCore.QSize(300, 110))
        self.groundListWidget.setMaximumSize(QtCore.QSize(300, 110))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groundListWidget.setFont(font)
        self.groundListWidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: rgb(200,200,200);\n"
"    color: black;\n"
"}")
        self.groundListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.groundListWidget.setObjectName("groundListWidget")
        self.horizontalLayout_55.addWidget(self.groundListWidget)
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.groundAddButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groundAddButton.sizePolicy().hasHeightForWidth())
        self.groundAddButton.setSizePolicy(sizePolicy)
        self.groundAddButton.setMinimumSize(QtCore.QSize(27, 27))
        self.groundAddButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groundAddButton.setFont(font)
        self.groundAddButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.groundAddButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/plus_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.groundAddButton.setIcon(icon3)
        self.groundAddButton.setIconSize(QtCore.QSize(23, 23))
        self.groundAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.groundAddButton.setAutoRaise(False)
        self.groundAddButton.setObjectName("groundAddButton")
        self.verticalLayout_38.addWidget(self.groundAddButton)
        self.groundRemoveButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        self.groundRemoveButton.setMinimumSize(QtCore.QSize(27, 27))
        self.groundRemoveButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groundRemoveButton.setFont(font)
        self.groundRemoveButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.groundRemoveButton.setIcon(icon4)
        self.groundRemoveButton.setIconSize(QtCore.QSize(23, 23))
        self.groundRemoveButton.setAutoRaise(False)
        self.groundRemoveButton.setObjectName("groundRemoveButton")
        self.verticalLayout_38.addWidget(self.groundRemoveButton)
        spacerItem243 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_38.addItem(spacerItem243)
        self.horizontalLayout_55.addLayout(self.verticalLayout_38)
        self.verticalLayout_55.addLayout(self.horizontalLayout_55)
        self.horizontalLayout_59.addLayout(self.verticalLayout_55)
        spacerItem244 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem244)
        self.verticalLayout_54 = QtWidgets.QVBoxLayout()
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_54.addWidget(self.label_27)
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.armListWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_12)
        self.armListWidget.setMinimumSize(QtCore.QSize(300, 110))
        self.armListWidget.setMaximumSize(QtCore.QSize(300, 110))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.armListWidget.setFont(font)
        self.armListWidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: rgb(200,200,200);\n"
"    color: black;\n"
"}")
        self.armListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.armListWidget.setObjectName("armListWidget")
        self.horizontalLayout_56.addWidget(self.armListWidget)
        self.verticalLayout_37 = QtWidgets.QVBoxLayout()
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.armAddButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.armAddButton.sizePolicy().hasHeightForWidth())
        self.armAddButton.setSizePolicy(sizePolicy)
        self.armAddButton.setMinimumSize(QtCore.QSize(27, 27))
        self.armAddButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.armAddButton.setFont(font)
        self.armAddButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.armAddButton.setText("")
        self.armAddButton.setIcon(icon3)
        self.armAddButton.setIconSize(QtCore.QSize(23, 23))
        self.armAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.armAddButton.setAutoRaise(False)
        self.armAddButton.setObjectName("armAddButton")
        self.verticalLayout_37.addWidget(self.armAddButton)
        self.armRemoveButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        self.armRemoveButton.setMinimumSize(QtCore.QSize(27, 27))
        self.armRemoveButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.armRemoveButton.setFont(font)
        self.armRemoveButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.armRemoveButton.setText("")
        self.armRemoveButton.setIcon(icon4)
        self.armRemoveButton.setIconSize(QtCore.QSize(23, 23))
        self.armRemoveButton.setAutoRaise(False)
        self.armRemoveButton.setObjectName("armRemoveButton")
        self.verticalLayout_37.addWidget(self.armRemoveButton)
        spacerItem245 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_37.addItem(spacerItem245)
        self.horizontalLayout_56.addLayout(self.verticalLayout_37)
        self.verticalLayout_54.addLayout(self.horizontalLayout_56)
        self.horizontalLayout_59.addLayout(self.verticalLayout_54)
        self.verticalLayout_58.addLayout(self.horizontalLayout_59)
        spacerItem246 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_58.addItem(spacerItem246)
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout()
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_56.addWidget(self.label_25)
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.vesselListWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_12)
        self.vesselListWidget.setMinimumSize(QtCore.QSize(300, 110))
        self.vesselListWidget.setMaximumSize(QtCore.QSize(300, 110))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.vesselListWidget.setFont(font)
        self.vesselListWidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: rgb(200,200,200);\n"
"    color: black;\n"
"}")
        self.vesselListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vesselListWidget.setObjectName("vesselListWidget")
        self.horizontalLayout_57.addWidget(self.vesselListWidget)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.vesselAddButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vesselAddButton.sizePolicy().hasHeightForWidth())
        self.vesselAddButton.setSizePolicy(sizePolicy)
        self.vesselAddButton.setMinimumSize(QtCore.QSize(27, 27))
        self.vesselAddButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.vesselAddButton.setFont(font)
        self.vesselAddButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.vesselAddButton.setText("")
        self.vesselAddButton.setIcon(icon3)
        self.vesselAddButton.setIconSize(QtCore.QSize(23, 23))
        self.vesselAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.vesselAddButton.setAutoRaise(False)
        self.vesselAddButton.setObjectName("vesselAddButton")
        self.verticalLayout_39.addWidget(self.vesselAddButton)
        self.vesselRemoveButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        self.vesselRemoveButton.setMinimumSize(QtCore.QSize(27, 27))
        self.vesselRemoveButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.vesselRemoveButton.setFont(font)
        self.vesselRemoveButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.vesselRemoveButton.setText("")
        self.vesselRemoveButton.setIcon(icon4)
        self.vesselRemoveButton.setIconSize(QtCore.QSize(23, 23))
        self.vesselRemoveButton.setAutoRaise(False)
        self.vesselRemoveButton.setObjectName("vesselRemoveButton")
        self.verticalLayout_39.addWidget(self.vesselRemoveButton)
        spacerItem247 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_39.addItem(spacerItem247)
        self.horizontalLayout_57.addLayout(self.verticalLayout_39)
        self.verticalLayout_56.addLayout(self.horizontalLayout_57)
        self.horizontalLayout_60.addLayout(self.verticalLayout_56)
        spacerItem248 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem248)
        self.verticalLayout_57 = QtWidgets.QVBoxLayout()
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_57.addWidget(self.label_28)
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.armMobileListWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_12)
        self.armMobileListWidget.setMinimumSize(QtCore.QSize(300, 110))
        self.armMobileListWidget.setMaximumSize(QtCore.QSize(300, 110))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.armMobileListWidget.setFont(font)
        self.armMobileListWidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background:  rgb(240, 240, 240);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: rgb(200,200,200);\n"
"    color: black;\n"
"}")
        self.armMobileListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.armMobileListWidget.setObjectName("armMobileListWidget")
        self.horizontalLayout_58.addWidget(self.armMobileListWidget)
        self.verticalLayout_40 = QtWidgets.QVBoxLayout()
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.armMobileAddButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.armMobileAddButton.sizePolicy().hasHeightForWidth())
        self.armMobileAddButton.setSizePolicy(sizePolicy)
        self.armMobileAddButton.setMinimumSize(QtCore.QSize(27, 27))
        self.armMobileAddButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.armMobileAddButton.setFont(font)
        self.armMobileAddButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.armMobileAddButton.setText("")
        self.armMobileAddButton.setIcon(icon3)
        self.armMobileAddButton.setIconSize(QtCore.QSize(23, 23))
        self.armMobileAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.armMobileAddButton.setAutoRaise(False)
        self.armMobileAddButton.setObjectName("armMobileAddButton")
        self.verticalLayout_40.addWidget(self.armMobileAddButton)
        self.armMobileRemoveButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        self.armMobileRemoveButton.setMinimumSize(QtCore.QSize(27, 27))
        self.armMobileRemoveButton.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.armMobileRemoveButton.setFont(font)
        self.armMobileRemoveButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.armMobileRemoveButton.setText("")
        self.armMobileRemoveButton.setIcon(icon4)
        self.armMobileRemoveButton.setIconSize(QtCore.QSize(23, 23))
        self.armMobileRemoveButton.setAutoRaise(False)
        self.armMobileRemoveButton.setObjectName("armMobileRemoveButton")
        self.verticalLayout_40.addWidget(self.armMobileRemoveButton)
        spacerItem249 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_40.addItem(spacerItem249)
        self.horizontalLayout_58.addLayout(self.verticalLayout_40)
        self.verticalLayout_57.addLayout(self.horizontalLayout_58)
        self.horizontalLayout_60.addLayout(self.verticalLayout_57)
        self.verticalLayout_58.addLayout(self.horizontalLayout_60)
        self.horizontalLayout_77.addLayout(self.verticalLayout_58)
        spacerItem250 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_77.addItem(spacerItem250)
        self.infoButton_14 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_12)
        self.infoButton_14.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_14.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.infoButton_14.setText("")
        self.infoButton_14.setIcon(icon1)
        self.infoButton_14.setIconSize(QtCore.QSize(23, 23))
        self.infoButton_14.setAutoRaise(False)
        self.infoButton_14.setObjectName("infoButton_14")
        self.horizontalLayout_77.addWidget(self.infoButton_14)
        self.gridLayout.addLayout(self.horizontalLayout_77, 1, 1, 2, 1)
        spacerItem251 = QtWidgets.QSpacerItem(146, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem251, 2, 2, 1, 1)
        spacerItem252 = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem252, 3, 1, 1, 1)
        self.so_scrollArea.setWidget(self.scrollAreaWidgetContents_12)
        self.gridLayout_39.addWidget(self.so_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage12, "")
        self.tabWidgetPage13 = QtWidgets.QWidget()
        self.tabWidgetPage13.setObjectName("tabWidgetPage13")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tabWidgetPage13)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.an_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage13)
        self.an_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.an_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.an_scrollArea.setWidgetResizable(True)
        self.an_scrollArea.setObjectName("an_scrollArea")
        self.scrollAreaWidgetContents_13 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_13.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_13.setObjectName("scrollAreaWidgetContents_13")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_13)
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_40.setObjectName("gridLayout_40")
        spacerItem253 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_40.addItem(spacerItem253, 0, 1, 1, 1)
        spacerItem254 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_40.addItem(spacerItem254, 1, 0, 1, 1)
        self.OtherCommentsTextBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_13)
        self.OtherCommentsTextBox.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.OtherCommentsTextBox.setFont(font)
        self.OtherCommentsTextBox.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.OtherCommentsTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OtherCommentsTextBox.setObjectName("OtherCommentsTextBox")
        self.gridLayout_40.addWidget(self.OtherCommentsTextBox, 1, 1, 2, 2)
        spacerItem255 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_40.addItem(spacerItem255, 2, 3, 1, 1)
        spacerItem256 = QtWidgets.QSpacerItem(20, 275, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_40.addItem(spacerItem256, 3, 2, 1, 1)
        self.an_scrollArea.setWidget(self.scrollAreaWidgetContents_13)
        self.gridLayout_12.addWidget(self.an_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage13, "")
        self.tabWidgetPage14 = QtWidgets.QWidget()
        self.tabWidgetPage14.setObjectName("tabWidgetPage14")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tabWidgetPage14)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.ii_scrollArea = QtWidgets.QScrollArea(self.tabWidgetPage14)
        self.ii_scrollArea.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ii_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ii_scrollArea.setWidgetResizable(True)
        self.ii_scrollArea.setObjectName("ii_scrollArea")
        self.scrollAreaWidgetContents_14 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(QtCore.QRect(0, 0, 1069, 529))
        self.scrollAreaWidgetContents_14.setObjectName("scrollAreaWidgetContents_14")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_14)
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_41.setObjectName("gridLayout_41")
        spacerItem257 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_41.addItem(spacerItem257, 0, 1, 1, 1)
        spacerItem258 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_41.addItem(spacerItem258, 1, 0, 1, 1)
        self.verticalLayout_64 = QtWidgets.QVBoxLayout()
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_35.setMinimumSize(QtCore.QSize(850, 0))
        self.label_35.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_35.setFont(font)
        self.label_35.setScaledContents(False)
        self.label_35.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_64.addWidget(self.label_35)
        spacerItem259 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_64.addItem(spacerItem259)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        spacerItem260 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem260)
        self.imageAddButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_14)
        self.imageAddButton.setMinimumSize(QtCore.QSize(150, 27))
        self.imageAddButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.imageAddButton.setFont(font)
        self.imageAddButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.imageAddButton.setObjectName("imageAddButton")
        self.horizontalLayout_82.addWidget(self.imageAddButton)
        spacerItem261 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem261)
        self.urlAddButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents_14)
        self.urlAddButton.setMinimumSize(QtCore.QSize(190, 27))
        self.urlAddButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.urlAddButton.setFont(font)
        self.urlAddButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.urlAddButton.setObjectName("urlAddButton")
        self.horizontalLayout_82.addWidget(self.urlAddButton)
        spacerItem262 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem262)
        self.verticalLayout_64.addLayout(self.horizontalLayout_82)
        spacerItem263 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_64.addItem(spacerItem263)
        self.verticalLayout_52 = QtWidgets.QVBoxLayout()
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.verticalLayout_64.addLayout(self.verticalLayout_52)
        self.gridLayout_41.addLayout(self.verticalLayout_64, 1, 1, 2, 2)
        spacerItem264 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_41.addItem(spacerItem264, 2, 3, 1, 1)
        spacerItem265 = QtWidgets.QSpacerItem(20, 214, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_41.addItem(spacerItem265, 3, 2, 1, 1)
        self.ii_scrollArea.setWidget(self.scrollAreaWidgetContents_14)
        self.gridLayout_22.addWidget(self.ii_scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage14, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/new_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/save_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSave_As.setFont(font)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionASMM_CreatorAbout = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/about_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionASMM_CreatorAbout.setIcon(icon10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionASMM_CreatorAbout.setFont(font)
        self.actionASMM_CreatorAbout.setObjectName("actionASMM_CreatorAbout")
        self.actionEUFAR_N7SP = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/eufar_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEUFAR_N7SP.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionEUFAR_N7SP.setFont(font)
        self.actionEUFAR_N7SP.setObjectName("actionEUFAR_N7SP")
        self.actionChangelog = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/changelog_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangelog.setIcon(icon12)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionChangelog.setFont(font)
        self.actionChangelog.setObjectName("actionChangelog")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/print_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon13)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionPrint.setFont(font)
        self.actionPrint.setObjectName("actionPrint")
        self.actionASMM_XML_Standard = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/xml_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionASMM_XML_Standard.setIcon(icon14)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionASMM_XML_Standard.setFont(font)
        self.actionASMM_XML_Standard.setObjectName("actionASMM_XML_Standard")
        self.actionHoriztonal_layout = QtWidgets.QAction(MainWindow)
        self.actionHoriztonal_layout.setObjectName("actionHoriztonal_layout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionASMM_CreatorAbout)
        self.menuAbout.addAction(self.actionASMM_XML_Standard)
        self.menuAbout.addAction(self.actionEUFAR_N7SP)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionChangelog)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.projectAcronym_lb.setText(_translate("MainWindow", "Project acronym:"))
        self.date_lb.setText(_translate("MainWindow", "Date (yyyy-mm-dd):"))
        self.date_dt.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.flightNumber_lb.setText(_translate("MainWindow", "Flight identifier:"))
        self.missionSci_lb.setText(_translate("MainWindow", "Mission scientist:"))
        self.flightManager_lb.setText(_translate("MainWindow", "Flight manager:"))
        self.operator_lb.setText(_translate("MainWindow", "Operator:"))
        self.operator_cb.setItemText(0, _translate("MainWindow", "Make a choice..."))
        self.operator_cb.setItemText(1, _translate("MainWindow", "Other..."))
        self.operator_cb.setItemText(2, _translate("MainWindow", "Alfred Wegener Institute"))
        self.operator_cb.setItemText(3, _translate("MainWindow", "CNR - Istituto per i Sistemi Agricoli e Forestali del Mediterraneo"))
        self.operator_cb.setItemText(4, _translate("MainWindow", "CNR - Istituto di Metodologie per l\'Analisi Ambientale"))
        self.operator_cb.setItemText(5, _translate("MainWindow", "Deutsches Zentrum fur Luft- und Raumfahrt"))
        self.operator_cb.setItemText(6, _translate("MainWindow", "ENVISCOPE"))
        self.operator_cb.setItemText(7, _translate("MainWindow", "NERC - Facility for Airborne Atmospheric Measurements"))
        self.operator_cb.setItemText(8, _translate("MainWindow", "FUB - Institut fur Weltraumwissenschaften"))
        self.operator_cb.setItemText(9, _translate("MainWindow", "Instituto Nacional de Tecnica Aeroespacial"))
        self.operator_cb.setItemText(10, _translate("MainWindow", "KIT - Institute of Meteorology and Climate Research"))
        self.operator_cb.setItemText(11, _translate("MainWindow", "NERC - Airborne Research and Survey Facility"))
        self.operator_cb.setItemText(12, _translate("MainWindow", "NERC - British Antarctic Survey"))
        self.operator_cb.setItemText(13, _translate("MainWindow", "SAFIRE"))
        self.operator_cb.setItemText(14, _translate("MainWindow", "UEDIN - Airborne GeoSciences"))
        self.aircraft_lb.setText(_translate("MainWindow", "Platform/Aircraft:"))
        self.location_lb.setText(_translate("MainWindow", "Location:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Flight Information"))
        self.contactName_lb.setText(_translate("MainWindow", "Name:"))
        self.contact_lb.setText(_translate("MainWindow", "Role:"))
        self.contact_cb.setItemText(0, _translate("MainWindow", "Make a choice..."))
        self.contact_cb.setItemText(1, _translate("MainWindow", "Flight Manager"))
        self.contact_cb.setItemText(2, _translate("MainWindow", "Mission Scientist"))
        self.contact_cb.setItemText(3, _translate("MainWindow", "Other"))
        self.contact_cb.setItemText(4, _translate("MainWindow", "Pilot"))
        self.contact_cb.setItemText(5, _translate("MainWindow", "Scientist"))
        self.contactEmail_lb.setText(_translate("MainWindow", "E-mail:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Contact Information"))
        self.satelliteCalValCheck.setText(_translate("MainWindow", "Satellite Cal/Val"))
        self.anthroPollutionCheck.setText(_translate("MainWindow", "Anthropogenic pollution"))
        self.mesoscaleImpactsCheck.setText(_translate("MainWindow", "Mesoscale atmospheric impacts"))
        self.label_12.setText(_translate("MainWindow", "Cloud:"))
        self.cloudMicrophysicsCheck.setText(_translate("MainWindow", "Microphysics"))
        self.cloudDynamicsCheck.setText(_translate("MainWindow", "Dynamics"))
        self.cloudRadiativeCheck.setText(_translate("MainWindow", "Radiative properties"))
        self.cloudConvectionCheck.setText(_translate("MainWindow", "Convection dynamics"))
        self.gasChemCheck.setText(_translate("MainWindow", "Gas Chemistry"))
        self.gasChemOxidantsCheck.setText(_translate("MainWindow", "Oxidants"))
        self.gasChemOrganicsCheck.setText(_translate("MainWindow", "Organics"))
        self.gasChemOtherCheck.setText(_translate("MainWindow", "Other"))
        self.aerosolCheck.setText(_translate("MainWindow", "Aerosol"))
        self.aerosolMicrophysicalCheck.setText(_translate("MainWindow", "Cloud microphysical impacts"))
        self.aerosolRadiativeCheck.setText(_translate("MainWindow", "Radiative properties/impacts"))
        self.radiationCheck.setText(_translate("MainWindow", "Radiation"))
        self.radiationAtmosSpectroscopyCheck.setText(_translate("MainWindow", "Atmospheric spectroscopy"))
        self.radiationSurfPropertiesCheck.setText(_translate("MainWindow", "Surf. properties/retrievals"))
        self.radiationOtherCheck.setText(_translate("MainWindow", "Other"))
        self.label_13.setText(_translate("MainWindow", "Boundary-layer:"))
        self.blCloudCheck.setText(_translate("MainWindow", "Cloud"))
        self.blDynamicsCheck.setText(_translate("MainWindow", "Dynamics"))
        self.sa_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_14.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Scientific Aims"))
        self.label_32.setText(_translate("MainWindow", "Geographic bounding box:"))
        self.label_31.setText(_translate("MainWindow", "North/South latitudes:"))
        self.label_29.setText(_translate("MainWindow", "West/East longitudes:"))
        self.label_30.setText(_translate("MainWindow", "Min/Max altitudes (m):"))
        self.readBoundingBoxButton.setText(_translate("MainWindow", "Read bounding box information from NetCDF"))
        self.label_33.setText(_translate("MainWindow", "Geographic situation:"))
        self.polarCheck.setText(_translate("MainWindow", "Polar"))
        self.subTropicalCheck.setText(_translate("MainWindow", "Sub-tropical"))
        self.maritimeCheck.setText(_translate("MainWindow", "Maritime"))
        self.oceanicIslandsCheck.setText(_translate("MainWindow", "Oceanic Islands"))
        self.midLatitudesCheck.setText(_translate("MainWindow", "Mid-Latitudes"))
        self.tropicalCheck.setText(_translate("MainWindow", "Tropical"))
        self.continentalCheck.setText(_translate("MainWindow", "Continental"))
        self.geogOtherCheck.setText(_translate("MainWindow", "Other"))
        self.gr_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_15.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("MainWindow", "Geographical Region"))
        self.oceanCheck.setText(_translate("MainWindow", "Ocean"))
        self.semiAridCheck.setText(_translate("MainWindow", "Semi-arid"))
        self.seaIceCheck.setText(_translate("MainWindow", "Sea-ice"))
        self.desertCheck.setText(_translate("MainWindow", "Desert"))
        self.snowCheck.setText(_translate("MainWindow", "Snow"))
        self.urbanCheck.setText(_translate("MainWindow", "Urban"))
        self.lakeIceCheck.setText(_translate("MainWindow", "Lake-ice"))
        self.forestCheck.setText(_translate("MainWindow", "Forest"))
        self.vegetationCheck.setText(_translate("MainWindow", "Vegetation"))
        self.mountainousCheck.setText(_translate("MainWindow", "Mountainous"))
        self.hillyCheck.setText(_translate("MainWindow", "Hilly"))
        self.flatCheck.setText(_translate("MainWindow", "Flat"))
        self.so_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_19.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage8), _translate("MainWindow", "Land or Oceans Surfaces Overflown"))
        self.stationaryCheck.setText(_translate("MainWindow", "Stationary"))
        self.stationaryCyclonicCheck.setText(_translate("MainWindow", "Cyclonic"))
        self.stationaryAnticyclonicCheck.setText(_translate("MainWindow", "Anticyclonic"))
        self.warmFrontCheck.setText(_translate("MainWindow", "Warm front"))
        self.warmConveyorBeltCheck.setText(_translate("MainWindow", "Warm conveyor belt"))
        self.arcticColdAirOutbreakCheck.setText(_translate("MainWindow", "Arctic cold-air outbreak"))
        self.coldFrontCheck.setText(_translate("MainWindow", "Cold front"))
        self.occludedFrontCheck.setText(_translate("MainWindow", "Occluded front"))
        self.warmSectorCheck.setText(_translate("MainWindow", "Warm sector"))
        self.postColdFrontalAirMassCheck.setText(_translate("MainWindow", "Post-cold-frontal air-mass"))
        self.orographicInfluenceCheck.setText(_translate("MainWindow", "Orographic influence"))
        self.seaBreezeFrontCheck.setText(_translate("MainWindow", "Sea-breeze front"))
        self.stratosphericFoldCheck.setText(_translate("MainWindow", "Stratospheric fold/intrusion"))
        self.extendedConvergenceLineCheck.setText(_translate("MainWindow", "Extended convergence line"))
        self.easterlyWaveCheck.setText(_translate("MainWindow", "Easterly Wave"))
        self.equatorialWaveCheck.setText(_translate("MainWindow", "Equatorial wave"))
        self.tropicalCycloneCheck.setText(_translate("MainWindow", "Tropical cyclone"))
        self.mesoscaleOrganizedConvectionCheck.setText(_translate("MainWindow", "Mesoscale organized convection"))
        self.af_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_16.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage5), _translate("MainWindow", "Atmospheric Synoptic Features"))
        self.waterCloudsCheck.setText(_translate("MainWindow", "Water clouds"))
        self.mixedPhaseCloudsCheck.setText(_translate("MainWindow", "Mixed-phase clouds"))
        self.iceCloudsCheck.setText(_translate("MainWindow", "Ice clouds"))
        self.cirrusCheck.setText(_translate("MainWindow", "Cirrus"))
        self.contrailsCheck.setText(_translate("MainWindow", "Contrails"))
        self.stratocumulusCheck.setText(_translate("MainWindow", "Stratocumulus"))
        self.shallowCumulusCheck.setText(_translate("MainWindow", "Shallow cumulus"))
        self.cumulusCongestusCheck.setText(_translate("MainWindow", "Cumulus congestus"))
        self.cumulonimbusToweringCumulusCheck.setText(_translate("MainWindow", "Cumulonimbus/towering cumulus"))
        self.altostratusAltocumulusCheck.setText(_translate("MainWindow", "Altostratus/altocumulus"))
        self.waveCloudsCheck.setText(_translate("MainWindow", "Wave clouds"))
        self.deepFrontalStratiformCloudsCheck.setText(_translate("MainWindow", "Deep frontal statiform clouds"))
        self.cloudFreeAboveAircraftCheck.setText(_translate("MainWindow", "Cloud-free above aircraft"))
        self.cloudFreeBelowAircraftCheck.setText(_translate("MainWindow", "Cloud-free below aircraft"))
        self.ct_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_17.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage6), _translate("MainWindow", "Cloud Types and Forms Sampled During Flight"))
        self.rainCheck.setText(_translate("MainWindow", "Rain"))
        self.drizzleCheck.setText(_translate("MainWindow", "Drizzle"))
        self.dropletsCheck.setText(_translate("MainWindow", "Droplets (liquid)"))
        self.pristineIceCrystalsCheck.setText(_translate("MainWindow", "Pristine ice crystals"))
        self.snowOrAggregatesCheck.setText(_translate("MainWindow", "Snow/aggregates"))
        self.graupelOrHailCheck.setText(_translate("MainWindow", "Graupel/hail"))
        self.seaSaltAerosolCheck.setText(_translate("MainWindow", "Sea-salt aerosol"))
        self.continentalAerosolCheck.setText(_translate("MainWindow", "Continental aerosol"))
        self.urbanPlumeCheck.setText(_translate("MainWindow", "Urban plume"))
        self.biomassBurningCheck.setText(_translate("MainWindow", "Biomass burning"))
        self.desertOrMineralDustCheck.setText(_translate("MainWindow", "Desert/mineral dust"))
        self.volcanicAshCheck.setText(_translate("MainWindow", "Volcanic ash"))
        self.ps_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_18.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage7), _translate("MainWindow", "Cloud, Precipitation and Aerosol Particles Sampled"))
        self.boundaryLayerCheck.setText(_translate("MainWindow", "Boundary-layer:"))
        self.blSubCloudCheck.setText(_translate("MainWindow", "sub-cloud"))
        self.blNearSurfaceCheck.setText(_translate("MainWindow", "near-surface"))
        self.blInCloudCheck.setText(_translate("MainWindow", "in-cloud"))
        self.upperTroposphereCheck.setText(_translate("MainWindow", "Upper troposphere"))
        self.midTroposphereCheck.setText(_translate("MainWindow", "Mid troposphere"))
        self.lowerTroposphereCheck.setText(_translate("MainWindow", "Lower troposphere"))
        self.lowerStratosphereCheck.setText(_translate("MainWindow", "Lower stratosphere"))
        self.ar_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_20.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage9), _translate("MainWindow", "Altitude Range of Measurement"))
        self.straightLevelRunsCheck.setText(_translate("MainWindow", "Straight/Level runs"))
        self.stackedStraightLevelRunsCheck.setText(_translate("MainWindow", "stacked"))
        self.separatedStraightLevelRuns.setText(_translate("MainWindow", "separated"))
        self.racetracksCheck.setText(_translate("MainWindow", "Racetracks"))
        self.orbitsCheck.setText(_translate("MainWindow", "Orbits"))
        self.lagrangianDescentsCheck.setText(_translate("MainWindow", "Lagrangian descents"))
        self.deepProfileAscentDescentsCheck.setText(_translate("MainWindow", "Deep profile ascents/descents"))
        self.dropsondeDeployedCheck.setText(_translate("MainWindow", "Dropsonde deployed"))
        self.selfCalibrationCheck.setText(_translate("MainWindow", "Self-calibration"))
        self.fm_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_21.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage10), _translate("MainWindow", "Types of Flight Manoeuvre"))
        self.label_22.setText(_translate("MainWindow", "Polar:"))
        self.polarAtrainCheck.setText(_translate("MainWindow", "A-train"))
        self.polarMetopCheck.setText(_translate("MainWindow", "METOP"))
        self.polarNpoessCheck.setText(_translate("MainWindow", "NPOESS"))
        self.polarOtherCheck.setText(_translate("MainWindow", "Other"))
        self.label_23.setText(_translate("MainWindow", "Geosynch:"))
        self.geosynchMsgCheck.setText(_translate("MainWindow", "MSG"))
        self.geosynchOtherCheck.setText(_translate("MainWindow", "Other"))
        self.airsCheck.setText(_translate("MainWindow", "AIRS"))
        self.amsuMhsCheck.setText(_translate("MainWindow", "AMSU/MHS"))
        self.caliopCheck.setText(_translate("MainWindow", "CALIOP"))
        self.cloudsatCheck.setText(_translate("MainWindow", "Cloudsat"))
        self.crisCheck.setText(_translate("MainWindow", "CriS"))
        self.iasiCheck.setText(_translate("MainWindow", "IASI"))
        self.modisCheck.setText(_translate("MainWindow", "MODIS"))
        self.sc_addButton.setText(_translate("MainWindow", "Add a new CheckBox"))
        self.label_24.setText(_translate("MainWindow", "Comments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage11), _translate("MainWindow", "Satellite Coordination"))
        self.label_26.setText(_translate("MainWindow", "Ground Sites:"))
        self.groundRemoveButton.setText(_translate("MainWindow", "Remove"))
        self.label_27.setText(_translate("MainWindow", "ARM Sites:"))
        self.label_25.setText(_translate("MainWindow", "Research Vessels: "))
        self.label_28.setText(_translate("MainWindow", "ARM Mobile sites:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage12), _translate("MainWindow", "Supporting Surface-based Observations"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage13), _translate("MainWindow", "Additional Notes on the Flight"))
        self.label_35.setText(_translate("MainWindow", "Use the following buttons to add images (JPG, PNG, BMP) to the PDF file. The number of images is limited to 10. All images will be included in the PDF report but not in the XML file."))
        self.imageAddButton.setText(_translate("MainWindow", "Add a new image"))
        self.urlAddButton.setText(_translate("MainWindow", "Add a new image (URL)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage14), _translate("MainWindow", "Images Included in the PDF Report"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New..."))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionExit.setText(_translate("MainWindow", "Exit..."))
        self.actionASMM_CreatorAbout.setText(_translate("MainWindow", "ASMM Creator..."))
        self.actionEUFAR_N7SP.setText(_translate("MainWindow", "EUFAR N7SP..."))
        self.actionChangelog.setText(_translate("MainWindow", "Changelog"))
        self.actionPrint.setText(_translate("MainWindow", "Print..."))
        self.actionASMM_XML_Standard.setText(_translate("MainWindow", "ASMM XML Standard..."))
        self.actionHoriztonal_layout.setText(_translate("MainWindow", "Horiztonal layout..."))
        self.actionHelp.setText(_translate("MainWindow", "Help..."))


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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1093, 583))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
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
        self.layoutWidget = QtWidgets.QWidget(self.tabWidgetPage1)
        self.layoutWidget.setGeometry(QtCore.QRect(35, 35, 831, 318))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(12)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(150, 27))
        self.label_4.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_71.addWidget(self.label_4)
        self.campaignLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.campaignLine.setMinimumSize(QtCore.QSize(300, 27))
        self.campaignLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.campaignLine.setFont(font)
        self.campaignLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.campaignLine.setFrame(False)
        self.campaignLine.setObjectName("campaignLine")
        self.horizontalLayout_71.addWidget(self.campaignLine)
        self.infoButton_1 = QtWidgets.QToolButton(self.layoutWidget)
        self.infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_1.setStyleSheet("QToolButton {\n"
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
        self.infoButton_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton_1.setIcon(icon1)
        self.infoButton_1.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_1.setAutoRaise(False)
        self.infoButton_1.setObjectName("infoButton_1")
        self.horizontalLayout_71.addWidget(self.infoButton_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_71.addItem(spacerItem)
        self.verticalLayout_36.addLayout(self.horizontalLayout_71)
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(150, 27))
        self.label_3.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_70.addWidget(self.label_3)
        self.dateLine = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateLine.setMinimumSize(QtCore.QSize(130, 27))
        self.dateLine.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dateLine.setFont(font)
        self.dateLine.setStyleSheet("QDateEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}\n"
"\n"
"QDateEdit::drop-down {subcontrol-origin: padding; subcontrol-position: top right; width: 27px; border-top-right-radius: 3px; border-bottom-right-radius: 3px;}\n"
"\n"
"QDateEdit::drop-down:hover {subcontrol-origin: padding; subcontrol-position: top right; width: 27px; border-left-width: 1px; border-left-color: darkgray; border-left-style: solid; border-top-right-radius: 3px; border-bottom-right-radius: 3px;}\n"
"\n"
"QDateEdit::down-arrow {image: url(icons/arrow_down.png); width: 18px; height: 18px;}\n"
"\n"
"QDateEdit::down-arrow:on {top: 1px; left: 1px;}")
        self.dateLine.setFrame(False)
        self.dateLine.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLine.setAccelerated(True)
        self.dateLine.setTime(QtCore.QTime(23, 0, 0))
        self.dateLine.setCalendarPopup(True)
        self.dateLine.setTimeSpec(QtCore.Qt.UTC)
        self.dateLine.setObjectName("dateLine")
        self.horizontalLayout_70.addWidget(self.dateLine)
        self.infoButton_2 = QtWidgets.QToolButton(self.layoutWidget)
        self.infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_2.setStyleSheet("QToolButton {\n"
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
        self.infoButton_2.setText("")
        self.infoButton_2.setIcon(icon1)
        self.infoButton_2.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_2.setAutoRaise(False)
        self.infoButton_2.setObjectName("infoButton_2")
        self.horizontalLayout_70.addWidget(self.infoButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_70.addItem(spacerItem1)
        self.verticalLayout_36.addLayout(self.horizontalLayout_70)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 27))
        self.label_2.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_52.addWidget(self.label_2)
        self.flightNumberLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.flightNumberLine.setMinimumSize(QtCore.QSize(300, 27))
        self.flightNumberLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.flightNumberLine.setFont(font)
        self.flightNumberLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.flightNumberLine.setFrame(False)
        self.flightNumberLine.setObjectName("flightNumberLine")
        self.horizontalLayout_52.addWidget(self.flightNumberLine)
        self.infoButton_3 = QtWidgets.QToolButton(self.layoutWidget)
        self.infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_3.setStyleSheet("QToolButton {\n"
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
        self.infoButton_3.setText("")
        self.infoButton_3.setIcon(icon1)
        self.infoButton_3.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_3.setAutoRaise(False)
        self.infoButton_3.setObjectName("infoButton_3")
        self.horizontalLayout_52.addWidget(self.infoButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem2)
        self.verticalLayout_36.addLayout(self.horizontalLayout_52)
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(150, 27))
        self.label_5.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_72.addWidget(self.label_5)
        self.missionSciLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.missionSciLine.setMinimumSize(QtCore.QSize(300, 27))
        self.missionSciLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.missionSciLine.setFont(font)
        self.missionSciLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.missionSciLine.setFrame(False)
        self.missionSciLine.setObjectName("missionSciLine")
        self.horizontalLayout_72.addWidget(self.missionSciLine)
        self.infoButton_4 = QtWidgets.QToolButton(self.layoutWidget)
        self.infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_4.setStyleSheet("QToolButton {\n"
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
        self.infoButton_4.setText("")
        self.infoButton_4.setIcon(icon1)
        self.infoButton_4.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_4.setAutoRaise(False)
        self.infoButton_4.setObjectName("infoButton_4")
        self.horizontalLayout_72.addWidget(self.infoButton_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem3)
        self.verticalLayout_36.addLayout(self.horizontalLayout_72)
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 27))
        self.label_6.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_73.addWidget(self.label_6)
        self.flightManagerLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.flightManagerLine.setMinimumSize(QtCore.QSize(300, 27))
        self.flightManagerLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.flightManagerLine.setFont(font)
        self.flightManagerLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.flightManagerLine.setFrame(False)
        self.flightManagerLine.setObjectName("flightManagerLine")
        self.horizontalLayout_73.addWidget(self.flightManagerLine)
        self.infoButton_5 = QtWidgets.QToolButton(self.layoutWidget)
        self.infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_5.setStyleSheet("QToolButton {\n"
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
        self.infoButton_5.setText("")
        self.infoButton_5.setIcon(icon1)
        self.infoButton_5.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_5.setAutoRaise(False)
        self.infoButton_5.setObjectName("infoButton_5")
        self.horizontalLayout_73.addWidget(self.infoButton_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_73.addItem(spacerItem4)
        self.verticalLayout_36.addLayout(self.horizontalLayout_73)
        self.horizontalLayout_74 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(150, 27))
        self.label_8.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_74.addWidget(self.label_8)
        self.operatorList = QtWidgets.QComboBox(self.layoutWidget)
        self.operatorList.setMinimumSize(QtCore.QSize(200, 27))
        self.operatorList.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.operatorList.setFont(font)
        self.operatorList.setStyleSheet("QComboBox {\n"
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
        self.operatorList.setFrame(False)
        self.operatorList.setObjectName("operatorList")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.operatorList.addItem("")
        self.horizontalLayout_74.addWidget(self.operatorList)
        self.infoButton_6 = QtWidgets.QToolButton(self.layoutWidget)
        self.infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_6.setStyleSheet("QToolButton {\n"
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
        self.infoButton_6.setText("")
        self.infoButton_6.setIcon(icon1)
        self.infoButton_6.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_6.setAutoRaise(False)
        self.infoButton_6.setObjectName("infoButton_6")
        self.horizontalLayout_74.addWidget(self.infoButton_6)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem5)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget)
        self.label_38.setEnabled(True)
        self.label_38.setMinimumSize(QtCore.QSize(25, 12))
        self.label_38.setMaximumSize(QtCore.QSize(25, 12))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_38.setFont(font)
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("icons/fwd_arrow.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_74.addWidget(self.label_38)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem6)
        self.tmpOperatorLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.tmpOperatorLine.setEnabled(True)
        self.tmpOperatorLine.setMinimumSize(QtCore.QSize(300, 27))
        self.tmpOperatorLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tmpOperatorLine.setFont(font)
        self.tmpOperatorLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.tmpOperatorLine.setFrame(False)
        self.tmpOperatorLine.setObjectName("tmpOperatorLine")
        self.horizontalLayout_74.addWidget(self.tmpOperatorLine)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(spacerItem7)
        self.verticalLayout_36.addLayout(self.horizontalLayout_74)
        self.horizontalLayout_75 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(150, 27))
        self.label_7.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_75.addWidget(self.label_7)
        self.aircraftList = QtWidgets.QComboBox(self.layoutWidget)
        self.aircraftList.setEnabled(False)
        self.aircraftList.setMinimumSize(QtCore.QSize(200, 27))
        self.aircraftList.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aircraftList.setFont(font)
        self.aircraftList.setStyleSheet("QComboBox {\n"
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
        self.aircraftList.setFrame(False)
        self.aircraftList.setObjectName("aircraftList")
        self.horizontalLayout_75.addWidget(self.aircraftList)
        self.emtpyButton = QtWidgets.QToolButton(self.layoutWidget)
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
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem8)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget)
        self.label_39.setEnabled(True)
        self.label_39.setMinimumSize(QtCore.QSize(25, 12))
        self.label_39.setMaximumSize(QtCore.QSize(25, 12))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_39.setFont(font)
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("icons/fwd_arrow.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_75.addWidget(self.label_39)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem9)
        self.tmpAircraftLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.tmpAircraftLine.setEnabled(True)
        self.tmpAircraftLine.setMinimumSize(QtCore.QSize(300, 27))
        self.tmpAircraftLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tmpAircraftLine.setFont(font)
        self.tmpAircraftLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.tmpAircraftLine.setFrame(False)
        self.tmpAircraftLine.setObjectName("tmpAircraftLine")
        self.horizontalLayout_75.addWidget(self.tmpAircraftLine)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem10)
        self.verticalLayout_36.addLayout(self.horizontalLayout_75)
        self.horizontalLayout_76 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(150, 27))
        self.label_9.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_76.addWidget(self.label_9)
        self.locationList = QtWidgets.QComboBox(self.layoutWidget)
        self.locationList.setEnabled(True)
        self.locationList.setMinimumSize(QtCore.QSize(200, 27))
        self.locationList.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.locationList.setFont(font)
        self.locationList.setStyleSheet("QComboBox {\n"
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
        self.locationList.setFrame(False)
        self.locationList.setObjectName("locationList")
        self.horizontalLayout_76.addWidget(self.locationList)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem11)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget)
        self.label_34.setMinimumSize(QtCore.QSize(25, 12))
        self.label_34.setMaximumSize(QtCore.QSize(25, 12))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_34.setFont(font)
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("icons/fwd_arrow.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_76.addWidget(self.label_34)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem12)
        self.detailList = QtWidgets.QComboBox(self.layoutWidget)
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
        self.infoButton_7 = QtWidgets.QToolButton(self.layoutWidget)
        self.infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_7.setStyleSheet("QToolButton {\n"
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
        self.infoButton_7.setText("")
        self.infoButton_7.setIcon(icon1)
        self.infoButton_7.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_7.setAutoRaise(False)
        self.infoButton_7.setObjectName("infoButton_7")
        self.horizontalLayout_76.addWidget(self.infoButton_7)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem13)
        self.verticalLayout_36.addLayout(self.horizontalLayout_76)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabWidgetPage2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem14, 0, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem15, 1, 0, 1, 1)
        self.verticalLayout_42 = QtWidgets.QVBoxLayout()
        self.verticalLayout_42.setSpacing(12)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label.setMinimumSize(QtCore.QSize(110, 27))
        self.label.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_53.addWidget(self.label)
        self.contactNameLine = QtWidgets.QLineEdit(self.tabWidgetPage2)
        self.contactNameLine.setMinimumSize(QtCore.QSize(300, 27))
        self.contactNameLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contactNameLine.setFont(font)
        self.contactNameLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.contactNameLine.setFrame(False)
        self.contactNameLine.setObjectName("contactNameLine")
        self.horizontalLayout_53.addWidget(self.contactNameLine)
        self.infoButton_8 = QtWidgets.QToolButton(self.tabWidgetPage2)
        self.infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_8.setStyleSheet("QToolButton {\n"
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
        self.infoButton_8.setText("")
        self.infoButton_8.setIcon(icon1)
        self.infoButton_8.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_8.setAutoRaise(False)
        self.infoButton_8.setObjectName("infoButton_8")
        self.horizontalLayout_53.addWidget(self.infoButton_8)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem16)
        self.verticalLayout_42.addLayout(self.horizontalLayout_53)
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.label_10 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_10.setMinimumSize(QtCore.QSize(110, 27))
        self.label_10.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_79.addWidget(self.label_10)
        self.contactRoleBox = QtWidgets.QComboBox(self.tabWidgetPage2)
        self.contactRoleBox.setMinimumSize(QtCore.QSize(180, 27))
        self.contactRoleBox.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contactRoleBox.setFont(font)
        self.contactRoleBox.setStyleSheet("QComboBox {\n"
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
"QComboBox:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
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
        self.contactRoleBox.setFrame(False)
        self.contactRoleBox.setObjectName("contactRoleBox")
        self.contactRoleBox.addItem("")
        self.contactRoleBox.addItem("")
        self.contactRoleBox.addItem("")
        self.contactRoleBox.addItem("")
        self.contactRoleBox.addItem("")
        self.contactRoleBox.addItem("")
        self.horizontalLayout_79.addWidget(self.contactRoleBox)
        self.infoButton_9 = QtWidgets.QToolButton(self.tabWidgetPage2)
        self.infoButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_9.setStyleSheet("QToolButton {\n"
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
        self.infoButton_9.setText("")
        self.infoButton_9.setIcon(icon1)
        self.infoButton_9.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_9.setAutoRaise(False)
        self.infoButton_9.setObjectName("infoButton_9")
        self.horizontalLayout_79.addWidget(self.infoButton_9)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem17)
        self.verticalLayout_42.addLayout(self.horizontalLayout_79)
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.label_11 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_11.setMinimumSize(QtCore.QSize(110, 27))
        self.label_11.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_80.addWidget(self.label_11)
        self.contactEmailLine = QtWidgets.QLineEdit(self.tabWidgetPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactEmailLine.sizePolicy().hasHeightForWidth())
        self.contactEmailLine.setSizePolicy(sizePolicy)
        self.contactEmailLine.setMinimumSize(QtCore.QSize(300, 27))
        self.contactEmailLine.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.contactEmailLine.setFont(font)
        self.contactEmailLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.contactEmailLine.setFrame(False)
        self.contactEmailLine.setObjectName("contactEmailLine")
        self.horizontalLayout_80.addWidget(self.contactEmailLine)
        self.infoButton_10 = QtWidgets.QToolButton(self.tabWidgetPage2)
        self.infoButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_10.setStyleSheet("QToolButton {\n"
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
        self.infoButton_10.setText("")
        self.infoButton_10.setIcon(icon1)
        self.infoButton_10.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_10.setAutoRaise(False)
        self.infoButton_10.setObjectName("infoButton_10")
        self.horizontalLayout_80.addWidget(self.infoButton_10)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_80.addItem(spacerItem18)
        self.verticalLayout_42.addLayout(self.horizontalLayout_80)
        self.gridLayout_3.addLayout(self.verticalLayout_42, 1, 1, 1, 2)
        spacerItem19 = QtWidgets.QSpacerItem(382, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 1, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 134, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem20, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem21, 0, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem22, 1, 0, 1, 1)
        self.verticalLayout_60 = QtWidgets.QVBoxLayout()
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.satelliteCalValCheck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.satelliteCalValCheck.setFont(font)
        self.satelliteCalValCheck.setObjectName("satelliteCalValCheck")
        self.verticalLayout_6.addWidget(self.satelliteCalValCheck)
        self.anthroPollutionCheck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.anthroPollutionCheck.setFont(font)
        self.anthroPollutionCheck.setObjectName("anthroPollutionCheck")
        self.verticalLayout_6.addWidget(self.anthroPollutionCheck)
        self.mesoscaleImpactsCheck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mesoscaleImpactsCheck.setFont(font)
        self.mesoscaleImpactsCheck.setObjectName("mesoscaleImpactsCheck")
        self.verticalLayout_6.addWidget(self.mesoscaleImpactsCheck)
        self.frame_3 = QtWidgets.QFrame(self.tabWidgetPage3)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
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
        self.verticalLayout_3.addWidget(self.label_12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem23 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem23)
        self.cloudMicrophysicsCheck = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudMicrophysicsCheck.setFont(font)
        self.cloudMicrophysicsCheck.setObjectName("cloudMicrophysicsCheck")
        self.horizontalLayout_3.addWidget(self.cloudMicrophysicsCheck)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem24 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem24)
        self.cloudDynamicsCheck = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudDynamicsCheck.setFont(font)
        self.cloudDynamicsCheck.setObjectName("cloudDynamicsCheck")
        self.horizontalLayout_4.addWidget(self.cloudDynamicsCheck)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem25 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem25)
        self.cloudRadiativeCheck = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudRadiativeCheck.setFont(font)
        self.cloudRadiativeCheck.setObjectName("cloudRadiativeCheck")
        self.horizontalLayout_5.addWidget(self.cloudRadiativeCheck)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem26 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem26)
        self.cloudConvectionCheck = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudConvectionCheck.setFont(font)
        self.cloudConvectionCheck.setObjectName("cloudConvectionCheck")
        self.horizontalLayout_6.addWidget(self.cloudConvectionCheck)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.horizontalLayout_15.addLayout(self.verticalLayout_6)
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem27)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.tabWidgetPage3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gasChemCheck = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemCheck.setFont(font)
        self.gasChemCheck.setObjectName("gasChemCheck")
        self.verticalLayout_2.addWidget(self.gasChemCheck)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem28 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem28)
        self.gasChemOxidantsCheck = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemOxidantsCheck.setFont(font)
        self.gasChemOxidantsCheck.setObjectName("gasChemOxidantsCheck")
        self.horizontalLayout_12.addWidget(self.gasChemOxidantsCheck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem29 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem29)
        self.gasChemOrganicsCheck = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemOrganicsCheck.setFont(font)
        self.gasChemOrganicsCheck.setObjectName("gasChemOrganicsCheck")
        self.horizontalLayout_13.addWidget(self.gasChemOrganicsCheck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem30 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem30)
        self.gasChemOtherCheck = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gasChemOtherCheck.setFont(font)
        self.gasChemOtherCheck.setObjectName("gasChemOtherCheck")
        self.horizontalLayout_14.addWidget(self.gasChemOtherCheck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.tabWidgetPage3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.aerosolCheck = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aerosolCheck.setFont(font)
        self.aerosolCheck.setObjectName("aerosolCheck")
        self.verticalLayout_5.addWidget(self.aerosolCheck)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem31 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem31)
        self.aerosolMicrophysicalCheck = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aerosolMicrophysicalCheck.setFont(font)
        self.aerosolMicrophysicalCheck.setObjectName("aerosolMicrophysicalCheck")
        self.horizontalLayout.addWidget(self.aerosolMicrophysicalCheck)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem32 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem32)
        self.aerosolRadiativeCheck = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aerosolRadiativeCheck.setFont(font)
        self.aerosolRadiativeCheck.setObjectName("aerosolRadiativeCheck")
        self.horizontalLayout_2.addWidget(self.aerosolRadiativeCheck)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        spacerItem33 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem33)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.tabWidgetPage3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radiationCheck = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationCheck.setFont(font)
        self.radiationCheck.setObjectName("radiationCheck")
        self.verticalLayout.addWidget(self.radiationCheck)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem34 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem34)
        self.radiationAtmosSpectroscopyCheck = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationAtmosSpectroscopyCheck.setFont(font)
        self.radiationAtmosSpectroscopyCheck.setObjectName("radiationAtmosSpectroscopyCheck")
        self.horizontalLayout_9.addWidget(self.radiationAtmosSpectroscopyCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem35 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem35)
        self.radiationSurfPropertiesCheck = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationSurfPropertiesCheck.setFont(font)
        self.radiationSurfPropertiesCheck.setObjectName("radiationSurfPropertiesCheck")
        self.horizontalLayout_10.addWidget(self.radiationSurfPropertiesCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem36 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem36)
        self.radiationOtherCheck = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radiationOtherCheck.setFont(font)
        self.radiationOtherCheck.setObjectName("radiationOtherCheck")
        self.horizontalLayout_11.addWidget(self.radiationOtherCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.tabWidgetPage3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
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
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem37 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem37)
        self.blCloudCheck = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.blCloudCheck.setFont(font)
        self.blCloudCheck.setObjectName("blCloudCheck")
        self.horizontalLayout_7.addWidget(self.blCloudCheck)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem38 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem38)
        self.blDynamicsCheck = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.blDynamicsCheck.setFont(font)
        self.blDynamicsCheck.setObjectName("blDynamicsCheck")
        self.horizontalLayout_8.addWidget(self.blDynamicsCheck)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8.addWidget(self.frame_4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        spacerItem39 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem39)
        self.infoButton_25 = QtWidgets.QToolButton(self.tabWidgetPage3)
        self.infoButton_25.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_25.setStyleSheet("QToolButton {\n"
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
        self.infoButton_25.setText("")
        self.infoButton_25.setIcon(icon1)
        self.infoButton_25.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_25.setAutoRaise(False)
        self.infoButton_25.setObjectName("infoButton_25")
        self.horizontalLayout_15.addWidget(self.infoButton_25)
        self.verticalLayout_60.addLayout(self.horizontalLayout_15)
        spacerItem40 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_60.addItem(spacerItem40)
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem41)
        self.sa_addButton = QtWidgets.QToolButton(self.tabWidgetPage3)
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
        spacerItem42 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem42)
        self.sa_infoButton = QtWidgets.QToolButton(self.tabWidgetPage3)
        self.sa_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.sa_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.sa_infoButton.setStyleSheet("QToolButton {\n"
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
        self.sa_infoButton.setText("")
        self.sa_infoButton.setIcon(icon1)
        self.sa_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.sa_infoButton.setAutoRaise(False)
        self.sa_infoButton.setObjectName("sa_infoButton")
        self.horizontalLayout_61.addWidget(self.sa_infoButton)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem43)
        self.verticalLayout_60.addLayout(self.horizontalLayout_61)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_60.addLayout(self.gridLayout_5)
        spacerItem44 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_60.addItem(spacerItem44)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_14.setMinimumSize(QtCore.QSize(90, 27))
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
        spacerItem45 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem45)
        self.horizontalLayout_16.addLayout(self.verticalLayout_12)
        self.SAOtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage3)
        self.SAOtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.SAOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.verticalLayout_60.addLayout(self.horizontalLayout_16)
        self.gridLayout_6.addLayout(self.verticalLayout_60, 1, 1, 1, 1)
        spacerItem46 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem46, 1, 2, 1, 1)
        spacerItem47 = QtWidgets.QSpacerItem(20, 174, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem47, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tabWidgetPage4)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        spacerItem48 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_17.addItem(spacerItem48, 0, 2, 1, 1)
        spacerItem49 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem49, 1, 0, 1, 1)
        self.verticalLayout_59 = QtWidgets.QVBoxLayout()
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_32 = QtWidgets.QLabel(self.tabWidgetPage4)
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
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem50)
        self.verticalLayout_59.addLayout(self.horizontalLayout_50)
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem51)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.label_31 = QtWidgets.QLabel(self.tabWidgetPage4)
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
        spacerItem52 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_45.addItem(spacerItem52)
        self.label_29 = QtWidgets.QLabel(self.tabWidgetPage4)
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
        spacerItem53 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem53)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.northBoundLatitudeLine = QtWidgets.QLineEdit(self.tabWidgetPage4)
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
        spacerItem54 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem54)
        self.westBoundLongitudeLine = QtWidgets.QLineEdit(self.tabWidgetPage4)
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
        spacerItem55 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem55)
        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.southBoundLatitudeLine = QtWidgets.QLineEdit(self.tabWidgetPage4)
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
        spacerItem56 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem56)
        self.infoButton_11 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.infoButton_11.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_11.setStyleSheet("QToolButton {\n"
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
        self.infoButton_11.setText("")
        self.infoButton_11.setIcon(icon1)
        self.infoButton_11.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_11.setAutoRaise(False)
        self.infoButton_11.setObjectName("infoButton_11")
        self.horizontalLayout_49.addWidget(self.infoButton_11)
        self.verticalLayout_41.addLayout(self.horizontalLayout_49)
        spacerItem57 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_41.addItem(spacerItem57)
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.eastBoundLongitudeLine = QtWidgets.QLineEdit(self.tabWidgetPage4)
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
        spacerItem58 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem58)
        self.infoButton_12 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.infoButton_12.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_12.setStyleSheet("QToolButton {\n"
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
        self.infoButton_12.setText("")
        self.infoButton_12.setIcon(icon1)
        self.infoButton_12.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_12.setAutoRaise(False)
        self.infoButton_12.setObjectName("infoButton_12")
        self.horizontalLayout_46.addWidget(self.infoButton_12)
        self.verticalLayout_41.addLayout(self.horizontalLayout_46)
        self.horizontalLayout_51.addLayout(self.verticalLayout_41)
        self.horizontalLayout_81.addLayout(self.horizontalLayout_51)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem59)
        self.verticalLayout_46 = QtWidgets.QVBoxLayout()
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.label_30 = QtWidgets.QLabel(self.tabWidgetPage4)
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
        spacerItem60 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem60)
        self.minAltitudeLine = QtWidgets.QLineEdit(self.tabWidgetPage4)
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
        spacerItem61 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem61)
        self.maxAltitudeLine = QtWidgets.QLineEdit(self.tabWidgetPage4)
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
        spacerItem62 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem62)
        self.infoButton_13 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.infoButton_13.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_13.setStyleSheet("QToolButton {\n"
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
        self.infoButton_13.setText("")
        self.infoButton_13.setIcon(icon1)
        self.infoButton_13.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_13.setAutoRaise(False)
        self.infoButton_13.setObjectName("infoButton_13")
        self.horizontalLayout_47.addWidget(self.infoButton_13)
        self.verticalLayout_46.addLayout(self.horizontalLayout_47)
        spacerItem63 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_46.addItem(spacerItem63)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        spacerItem64 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem64)
        self.readBoundingBoxButton = QtWidgets.QToolButton(self.tabWidgetPage4)
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
        spacerItem65 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem65)
        self.verticalLayout_46.addLayout(self.horizontalLayout_48)
        self.horizontalLayout_81.addLayout(self.verticalLayout_46)
        self.verticalLayout_59.addLayout(self.horizontalLayout_81)
        spacerItem66 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_59.addItem(spacerItem66)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_33 = QtWidgets.QLabel(self.tabWidgetPage4)
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
        spacerItem67 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem67)
        self.verticalLayout_59.addLayout(self.horizontalLayout_54)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem68 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem68)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.polarCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        self.subTropicalCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        self.maritimeCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        self.oceanicIslandsCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        self.midLatitudesCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        self.tropicalCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        self.continentalCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        self.geogOtherCheck = QtWidgets.QCheckBox(self.tabWidgetPage4)
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
        spacerItem69 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem69)
        self.infoButton_16 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.infoButton_16.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_16.setStyleSheet("QToolButton {\n"
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
        self.infoButton_16.setText("")
        self.infoButton_16.setIcon(icon1)
        self.infoButton_16.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_16.setAutoRaise(False)
        self.infoButton_16.setObjectName("infoButton_16")
        self.horizontalLayout_17.addWidget(self.infoButton_16)
        self.verticalLayout_59.addLayout(self.horizontalLayout_17)
        spacerItem70 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_59.addItem(spacerItem70)
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        spacerItem71 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem71)
        self.gr_addButton = QtWidgets.QToolButton(self.tabWidgetPage4)
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
        spacerItem72 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem72)
        self.gr_infoButton = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.gr_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.gr_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.gr_infoButton.setStyleSheet("QToolButton {\n"
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
        self.gr_infoButton.setText("")
        self.gr_infoButton.setIcon(icon1)
        self.gr_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.gr_infoButton.setAutoRaise(False)
        self.gr_infoButton.setObjectName("gr_infoButton")
        self.horizontalLayout_62.addWidget(self.gr_infoButton)
        spacerItem73 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem73)
        self.verticalLayout_59.addLayout(self.horizontalLayout_62)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_59.addLayout(self.gridLayout_8)
        spacerItem74 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_59.addItem(spacerItem74)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.tabWidgetPage4)
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
        spacerItem75 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem75)
        self.horizontalLayout_18.addLayout(self.verticalLayout_9)
        self.GROtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage4)
        self.GROtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.GROtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.gridLayout_17.addLayout(self.verticalLayout_59, 1, 1, 1, 2)
        spacerItem76 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem76, 1, 3, 1, 1)
        spacerItem77 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem77, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage8 = QtWidgets.QWidget()
        self.tabWidgetPage8.setObjectName("tabWidgetPage8")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tabWidgetPage8)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem78 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_16.addItem(spacerItem78, 0, 1, 1, 1)
        spacerItem79 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem79, 1, 0, 1, 1)
        self.verticalLayout_44 = QtWidgets.QVBoxLayout()
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.oceanCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.semiAridCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.seaIceCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        spacerItem80 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem80)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.desertCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.snowCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.urbanCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        spacerItem81 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem81)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.lakeIceCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.forestCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.vegetationCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        spacerItem82 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem82)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.mountainousCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.hillyCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        self.flatCheck = QtWidgets.QCheckBox(self.tabWidgetPage8)
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
        spacerItem83 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem83)
        self.infoButton_17 = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.infoButton_17.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_17.setStyleSheet("QToolButton {\n"
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
        self.infoButton_17.setText("")
        self.infoButton_17.setIcon(icon1)
        self.infoButton_17.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_17.setAutoRaise(False)
        self.infoButton_17.setObjectName("infoButton_17")
        self.horizontalLayout_27.addWidget(self.infoButton_17)
        self.verticalLayout_44.addLayout(self.horizontalLayout_27)
        spacerItem84 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_44.addItem(spacerItem84)
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        spacerItem85 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem85)
        self.so_addButton = QtWidgets.QToolButton(self.tabWidgetPage8)
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
        spacerItem86 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem86)
        self.so_infoButton = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.so_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.so_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.so_infoButton.setStyleSheet("QToolButton {\n"
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
        self.so_infoButton.setText("")
        self.so_infoButton.setIcon(icon1)
        self.so_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.so_infoButton.setAutoRaise(False)
        self.so_infoButton.setObjectName("so_infoButton")
        self.horizontalLayout_66.addWidget(self.so_infoButton)
        spacerItem87 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem87)
        self.verticalLayout_44.addLayout(self.horizontalLayout_66)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_44.addLayout(self.gridLayout_13)
        spacerItem88 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_44.addItem(spacerItem88)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout()
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.label_19 = QtWidgets.QLabel(self.tabWidgetPage8)
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
        spacerItem89 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_53.addItem(spacerItem89)
        self.horizontalLayout_28.addLayout(self.verticalLayout_53)
        self.SOOtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage8)
        self.SOOtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.SOOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.gridLayout_16.addLayout(self.verticalLayout_44, 1, 1, 1, 1)
        spacerItem90 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem90, 1, 2, 1, 1)
        spacerItem91 = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem91, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage8, "")
        self.tabWidgetPage5 = QtWidgets.QWidget()
        self.tabWidgetPage5.setObjectName("tabWidgetPage5")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tabWidgetPage5)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem92 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_18.addItem(spacerItem92, 0, 1, 1, 1)
        spacerItem93 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem93, 1, 0, 1, 1)
        self.verticalLayout_61 = QtWidgets.QVBoxLayout()
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.stationaryCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        spacerItem94 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem94)
        self.stationaryCyclonicCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        spacerItem95 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem95)
        self.stationaryAnticyclonicCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.warmFrontCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.warmConveyorBeltCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        spacerItem96 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem96)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.arcticColdAirOutbreakCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.coldFrontCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.occludedFrontCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.warmSectorCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.postColdFrontalAirMassCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        spacerItem97 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem97)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.orographicInfluenceCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.seaBreezeFrontCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.stratosphericFoldCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.extendedConvergenceLineCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        spacerItem98 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem98)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.easterlyWaveCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.equatorialWaveCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.tropicalCycloneCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        self.mesoscaleOrganizedConvectionCheck = QtWidgets.QCheckBox(self.tabWidgetPage5)
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
        spacerItem99 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem99)
        self.infoButton_18 = QtWidgets.QToolButton(self.tabWidgetPage5)
        self.infoButton_18.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_18.setStyleSheet("QToolButton {\n"
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
        self.infoButton_18.setText("")
        self.infoButton_18.setIcon(icon1)
        self.infoButton_18.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_18.setAutoRaise(False)
        self.infoButton_18.setObjectName("infoButton_18")
        self.horizontalLayout_21.addWidget(self.infoButton_18)
        self.verticalLayout_61.addLayout(self.horizontalLayout_21)
        spacerItem100 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_61.addItem(spacerItem100)
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        spacerItem101 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem101)
        self.af_addButton = QtWidgets.QToolButton(self.tabWidgetPage5)
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
        spacerItem102 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem102)
        self.af_infoButton = QtWidgets.QToolButton(self.tabWidgetPage5)
        self.af_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.af_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.af_infoButton.setStyleSheet("QToolButton {\n"
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
        self.af_infoButton.setText("")
        self.af_infoButton.setIcon(icon1)
        self.af_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.af_infoButton.setAutoRaise(False)
        self.af_infoButton.setObjectName("af_infoButton")
        self.horizontalLayout_63.addWidget(self.af_infoButton)
        spacerItem103 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem103)
        self.verticalLayout_61.addLayout(self.horizontalLayout_63)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_61.addLayout(self.gridLayout_9)
        spacerItem104 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_61.addItem(spacerItem104)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout()
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.label_16 = QtWidgets.QLabel(self.tabWidgetPage5)
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
        spacerItem105 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_47.addItem(spacerItem105)
        self.horizontalLayout_22.addLayout(self.verticalLayout_47)
        self.AFOtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage5)
        self.AFOtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.AFOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.gridLayout_18.addLayout(self.verticalLayout_61, 1, 1, 1, 2)
        spacerItem106 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem106, 1, 3, 1, 1)
        spacerItem107 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem107, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage5, "")
        self.tabWidgetPage6 = QtWidgets.QWidget()
        self.tabWidgetPage6.setObjectName("tabWidgetPage6")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tabWidgetPage6)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        spacerItem108 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_19.addItem(spacerItem108, 0, 1, 1, 1)
        spacerItem109 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem109, 1, 0, 1, 1)
        self.verticalLayout_62 = QtWidgets.QVBoxLayout()
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.waterCloudsCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.mixedPhaseCloudsCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.iceCloudsCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.cirrusCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        spacerItem110 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem110)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.contrailsCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.stratocumulusCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.shallowCumulusCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.cumulusCongestusCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        spacerItem111 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem111)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.cumulonimbusToweringCumulusCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.altostratusAltocumulusCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.waveCloudsCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        spacerItem112 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem112)
        self.verticalLayout_48 = QtWidgets.QVBoxLayout()
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.deepFrontalStratiformCloudsCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.cloudFreeAboveAircraftCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.cloudFreeBelowAircraftCheck = QtWidgets.QCheckBox(self.tabWidgetPage6)
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
        self.infoButton_19 = QtWidgets.QToolButton(self.tabWidgetPage6)
        self.infoButton_19.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_19.setStyleSheet("QToolButton {\n"
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
        self.infoButton_19.setText("")
        self.infoButton_19.setIcon(icon1)
        self.infoButton_19.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_19.setAutoRaise(False)
        self.infoButton_19.setObjectName("infoButton_19")
        self.horizontalLayout_23.addWidget(self.infoButton_19)
        self.verticalLayout_62.addLayout(self.horizontalLayout_23)
        spacerItem113 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_62.addItem(spacerItem113)
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        spacerItem114 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem114)
        self.ct_addButton = QtWidgets.QToolButton(self.tabWidgetPage6)
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
        spacerItem115 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem115)
        self.ct_infoButton = QtWidgets.QToolButton(self.tabWidgetPage6)
        self.ct_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.ct_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.ct_infoButton.setStyleSheet("QToolButton {\n"
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
        self.ct_infoButton.setText("")
        self.ct_infoButton.setIcon(icon1)
        self.ct_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.ct_infoButton.setAutoRaise(False)
        self.ct_infoButton.setObjectName("ct_infoButton")
        self.horizontalLayout_64.addWidget(self.ct_infoButton)
        spacerItem116 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem116)
        self.verticalLayout_62.addLayout(self.horizontalLayout_64)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_62.addLayout(self.gridLayout_10)
        spacerItem117 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_62.addItem(spacerItem117)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout()
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.label_17 = QtWidgets.QLabel(self.tabWidgetPage6)
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
        spacerItem118 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_49.addItem(spacerItem118)
        self.horizontalLayout_24.addLayout(self.verticalLayout_49)
        self.CTOtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage6)
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
        self.gridLayout_19.addLayout(self.verticalLayout_62, 1, 1, 1, 1)
        spacerItem119 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem119, 1, 2, 1, 1)
        spacerItem120 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem120, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage6, "")
        self.tabWidgetPage7 = QtWidgets.QWidget()
        self.tabWidgetPage7.setObjectName("tabWidgetPage7")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tabWidgetPage7)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem121 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_20.addItem(spacerItem121, 0, 1, 1, 1)
        spacerItem122 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem122, 1, 0, 1, 1)
        self.verticalLayout_63 = QtWidgets.QVBoxLayout()
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout()
        self.verticalLayout_50.setSpacing(7)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.rainCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.drizzleCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.dropletsCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        spacerItem123 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem123)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setSpacing(7)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.pristineIceCrystalsCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.snowOrAggregatesCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.graupelOrHailCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        spacerItem124 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem124)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.seaSaltAerosolCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.continentalAerosolCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.urbanPlumeCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        spacerItem125 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem125)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(7)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.biomassBurningCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.desertOrMineralDustCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        self.volcanicAshCheck = QtWidgets.QCheckBox(self.tabWidgetPage7)
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
        spacerItem126 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem126)
        self.infoButton_20 = QtWidgets.QToolButton(self.tabWidgetPage7)
        self.infoButton_20.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_20.setStyleSheet("QToolButton {\n"
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
        self.infoButton_20.setText("")
        self.infoButton_20.setIcon(icon1)
        self.infoButton_20.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_20.setAutoRaise(False)
        self.infoButton_20.setObjectName("infoButton_20")
        self.horizontalLayout_25.addWidget(self.infoButton_20)
        self.verticalLayout_63.addLayout(self.horizontalLayout_25)
        spacerItem127 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_63.addItem(spacerItem127)
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        spacerItem128 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem128)
        self.ps_addButton = QtWidgets.QToolButton(self.tabWidgetPage7)
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
        spacerItem129 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem129)
        self.ps_infoButton = QtWidgets.QToolButton(self.tabWidgetPage7)
        self.ps_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.ps_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.ps_infoButton.setStyleSheet("QToolButton {\n"
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
        self.ps_infoButton.setText("")
        self.ps_infoButton.setIcon(icon1)
        self.ps_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.ps_infoButton.setAutoRaise(False)
        self.ps_infoButton.setObjectName("ps_infoButton")
        self.horizontalLayout_65.addWidget(self.ps_infoButton)
        spacerItem130 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem130)
        self.verticalLayout_63.addLayout(self.horizontalLayout_65)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_63.addLayout(self.gridLayout_11)
        spacerItem131 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_63.addItem(spacerItem131)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout()
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_18 = QtWidgets.QLabel(self.tabWidgetPage7)
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
        spacerItem132 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_51.addItem(spacerItem132)
        self.horizontalLayout_26.addLayout(self.verticalLayout_51)
        self.PSOtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage7)
        self.PSOtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.PSOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.gridLayout_20.addLayout(self.verticalLayout_63, 1, 1, 1, 1)
        spacerItem133 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem133, 1, 2, 1, 1)
        spacerItem134 = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem134, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage7, "")
        self.tabWidgetPage9 = QtWidgets.QWidget()
        self.tabWidgetPage9.setObjectName("tabWidgetPage9")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tabWidgetPage9)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem135 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_21.addItem(spacerItem135, 0, 1, 1, 1)
        spacerItem136 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem136, 1, 0, 1, 1)
        self.verticalLayout_68 = QtWidgets.QVBoxLayout()
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.boundaryLayerCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        spacerItem137 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem137)
        self.verticalLayout_25.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem138 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem138)
        self.blSubCloudCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        spacerItem139 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem139)
        self.blNearSurfaceCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        spacerItem140 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem140)
        self.blInCloudCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        spacerItem141 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem141)
        self.verticalLayout_25.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_31.addLayout(self.verticalLayout_25)
        spacerItem142 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem142)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.upperTroposphereCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        self.midTroposphereCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        spacerItem143 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem143)
        self.horizontalLayout_31.addLayout(self.verticalLayout_26)
        spacerItem144 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem144)
        self.verticalLayout_65 = QtWidgets.QVBoxLayout()
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.lowerTroposphereCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        self.lowerStratosphereCheck = QtWidgets.QCheckBox(self.tabWidgetPage9)
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
        spacerItem145 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_65.addItem(spacerItem145)
        self.horizontalLayout_31.addLayout(self.verticalLayout_65)
        spacerItem146 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem146)
        self.infoButton_21 = QtWidgets.QToolButton(self.tabWidgetPage9)
        self.infoButton_21.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_21.setStyleSheet("QToolButton {\n"
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
        self.infoButton_21.setText("")
        self.infoButton_21.setIcon(icon1)
        self.infoButton_21.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_21.setAutoRaise(False)
        self.infoButton_21.setObjectName("infoButton_21")
        self.horizontalLayout_31.addWidget(self.infoButton_21)
        self.verticalLayout_68.addLayout(self.horizontalLayout_31)
        spacerItem147 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_68.addItem(spacerItem147)
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        spacerItem148 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem148)
        self.ar_addButton = QtWidgets.QToolButton(self.tabWidgetPage9)
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
        spacerItem149 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem149)
        self.ar_infoButton = QtWidgets.QToolButton(self.tabWidgetPage9)
        self.ar_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.ar_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.ar_infoButton.setStyleSheet("QToolButton {\n"
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
        self.ar_infoButton.setText("")
        self.ar_infoButton.setIcon(icon1)
        self.ar_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.ar_infoButton.setAutoRaise(False)
        self.ar_infoButton.setObjectName("ar_infoButton")
        self.horizontalLayout_67.addWidget(self.ar_infoButton)
        spacerItem150 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem150)
        self.verticalLayout_68.addLayout(self.horizontalLayout_67)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_68.addLayout(self.gridLayout_14)
        spacerItem151 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_68.addItem(spacerItem151)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_20 = QtWidgets.QLabel(self.tabWidgetPage9)
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
        spacerItem152 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem152)
        self.horizontalLayout_33.addLayout(self.verticalLayout_27)
        self.AROtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage9)
        self.AROtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.AROtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.gridLayout_21.addLayout(self.verticalLayout_68, 1, 1, 1, 1)
        spacerItem153 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem153, 1, 2, 1, 1)
        spacerItem154 = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem154, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage9, "")
        self.tabWidgetPage10 = QtWidgets.QWidget()
        self.tabWidgetPage10.setObjectName("tabWidgetPage10")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tabWidgetPage10)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        spacerItem155 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_23.addItem(spacerItem155, 0, 1, 1, 1)
        spacerItem156 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem156, 1, 0, 1, 1)
        self.verticalLayout_70 = QtWidgets.QVBoxLayout()
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.straightLevelRunsCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        spacerItem157 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem157)
        self.stackedStraightLevelRunsCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        spacerItem158 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem158)
        self.verticalLayout_28.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        spacerItem159 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem159)
        self.separatedStraightLevelRuns = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        spacerItem160 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem160)
        self.verticalLayout_28.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36.addLayout(self.verticalLayout_28)
        spacerItem161 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem161)
        self.verticalLayout_69 = QtWidgets.QVBoxLayout()
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.racetracksCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        self.orbitsCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        spacerItem162 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_69.addItem(spacerItem162)
        self.horizontalLayout_36.addLayout(self.verticalLayout_69)
        spacerItem163 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem163)
        self.verticalLayout_66 = QtWidgets.QVBoxLayout()
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.lagrangianDescentsCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        self.deepProfileAscentDescentsCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        spacerItem164 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_66.addItem(spacerItem164)
        self.horizontalLayout_36.addLayout(self.verticalLayout_66)
        spacerItem165 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem165)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.dropsondeDeployedCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        self.selfCalibrationCheck = QtWidgets.QCheckBox(self.tabWidgetPage10)
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
        spacerItem166 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem166)
        self.horizontalLayout_36.addLayout(self.verticalLayout_29)
        spacerItem167 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem167)
        self.infoButton_22 = QtWidgets.QToolButton(self.tabWidgetPage10)
        self.infoButton_22.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_22.setStyleSheet("QToolButton {\n"
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
        self.infoButton_22.setText("")
        self.infoButton_22.setIcon(icon1)
        self.infoButton_22.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_22.setAutoRaise(False)
        self.infoButton_22.setObjectName("infoButton_22")
        self.horizontalLayout_36.addWidget(self.infoButton_22)
        self.verticalLayout_70.addLayout(self.horizontalLayout_36)
        spacerItem168 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_70.addItem(spacerItem168)
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        spacerItem169 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem169)
        self.fm_addButton = QtWidgets.QToolButton(self.tabWidgetPage10)
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
        spacerItem170 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem170)
        self.fm_infoButton = QtWidgets.QToolButton(self.tabWidgetPage10)
        self.fm_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.fm_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.fm_infoButton.setStyleSheet("QToolButton {\n"
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
        self.fm_infoButton.setText("")
        self.fm_infoButton.setIcon(icon1)
        self.fm_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.fm_infoButton.setAutoRaise(False)
        self.fm_infoButton.setObjectName("fm_infoButton")
        self.horizontalLayout_68.addWidget(self.fm_infoButton)
        spacerItem171 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem171)
        self.verticalLayout_70.addLayout(self.horizontalLayout_68)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.verticalLayout_70.addLayout(self.gridLayout_15)
        spacerItem172 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_70.addItem(spacerItem172)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_21 = QtWidgets.QLabel(self.tabWidgetPage10)
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
        spacerItem173 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_30.addItem(spacerItem173)
        self.horizontalLayout_37.addLayout(self.verticalLayout_30)
        self.FTOtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage10)
        self.FTOtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.FTOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.gridLayout_23.addLayout(self.verticalLayout_70, 1, 1, 1, 1)
        spacerItem174 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem174, 1, 2, 1, 1)
        spacerItem175 = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem175, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage10, "")
        self.tabWidgetPage11 = QtWidgets.QWidget()
        self.tabWidgetPage11.setObjectName("tabWidgetPage11")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tabWidgetPage11)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        spacerItem176 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_24.addItem(spacerItem176, 0, 1, 1, 1)
        spacerItem177 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem177, 1, 0, 1, 1)
        self.verticalLayout_67 = QtWidgets.QVBoxLayout()
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_22 = QtWidgets.QLabel(self.tabWidgetPage11)
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
        spacerItem178 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem178)
        self.polarAtrainCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
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
        spacerItem179 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem179)
        self.polarMetopCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
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
        spacerItem180 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem180)
        self.polarNpoessCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
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
        spacerItem181 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem181)
        self.polarOtherCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
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
        spacerItem182 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem182)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_23 = QtWidgets.QLabel(self.tabWidgetPage11)
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
        spacerItem183 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem183)
        self.geosynchMsgCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
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
        spacerItem184 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem184)
        self.geosynchOtherCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
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
        spacerItem185 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_32.addItem(spacerItem185)
        self.horizontalLayout_44.addLayout(self.verticalLayout_32)
        spacerItem186 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem186)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.airsCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.airsCheck.setFont(font)
        self.airsCheck.setObjectName("airsCheck")
        self.verticalLayout_33.addWidget(self.airsCheck)
        self.amsuMhsCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.amsuMhsCheck.setFont(font)
        self.amsuMhsCheck.setObjectName("amsuMhsCheck")
        self.verticalLayout_33.addWidget(self.amsuMhsCheck)
        self.caliopCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.caliopCheck.setFont(font)
        self.caliopCheck.setObjectName("caliopCheck")
        self.verticalLayout_33.addWidget(self.caliopCheck)
        self.cloudsatCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cloudsatCheck.setFont(font)
        self.cloudsatCheck.setObjectName("cloudsatCheck")
        self.verticalLayout_33.addWidget(self.cloudsatCheck)
        spacerItem187 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_33.addItem(spacerItem187)
        self.horizontalLayout_44.addLayout(self.verticalLayout_33)
        spacerItem188 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem188)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.crisCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.crisCheck.setFont(font)
        self.crisCheck.setObjectName("crisCheck")
        self.verticalLayout_34.addWidget(self.crisCheck)
        self.iasiCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.iasiCheck.setFont(font)
        self.iasiCheck.setObjectName("iasiCheck")
        self.verticalLayout_34.addWidget(self.iasiCheck)
        self.modisCheck = QtWidgets.QCheckBox(self.tabWidgetPage11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.modisCheck.setFont(font)
        self.modisCheck.setObjectName("modisCheck")
        self.verticalLayout_34.addWidget(self.modisCheck)
        spacerItem189 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_34.addItem(spacerItem189)
        self.horizontalLayout_44.addLayout(self.verticalLayout_34)
        spacerItem190 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem190)
        self.infoButton_23 = QtWidgets.QToolButton(self.tabWidgetPage11)
        self.infoButton_23.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_23.setStyleSheet("QToolButton {\n"
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
        self.infoButton_23.setText("")
        self.infoButton_23.setIcon(icon1)
        self.infoButton_23.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_23.setAutoRaise(False)
        self.infoButton_23.setObjectName("infoButton_23")
        self.horizontalLayout_44.addWidget(self.infoButton_23)
        self.verticalLayout_67.addLayout(self.horizontalLayout_44)
        spacerItem191 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_67.addItem(spacerItem191)
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        spacerItem192 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem192)
        self.sc_addButton = QtWidgets.QToolButton(self.tabWidgetPage11)
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
        spacerItem193 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem193)
        self.sc_infoButton = QtWidgets.QToolButton(self.tabWidgetPage11)
        self.sc_infoButton.setMinimumSize(QtCore.QSize(27, 27))
        self.sc_infoButton.setMaximumSize(QtCore.QSize(27, 27))
        self.sc_infoButton.setStyleSheet("QToolButton {\n"
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
        self.sc_infoButton.setText("")
        self.sc_infoButton.setIcon(icon1)
        self.sc_infoButton.setIconSize(QtCore.QSize(27, 27))
        self.sc_infoButton.setAutoRaise(False)
        self.sc_infoButton.setObjectName("sc_infoButton")
        self.horizontalLayout_69.addWidget(self.sc_infoButton)
        spacerItem194 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(spacerItem194)
        self.verticalLayout_67.addLayout(self.horizontalLayout_69)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.verticalLayout_67.addLayout(self.gridLayout_25)
        spacerItem195 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_67.addItem(spacerItem195)
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_24 = QtWidgets.QLabel(self.tabWidgetPage11)
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
        spacerItem196 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_35.addItem(spacerItem196)
        self.horizontalLayout_45.addLayout(self.verticalLayout_35)
        self.SCOtherTextBox = QtWidgets.QTextEdit(self.tabWidgetPage11)
        self.SCOtherTextBox.setMinimumSize(QtCore.QSize(750, 75))
        self.SCOtherTextBox.setMaximumSize(QtCore.QSize(16777215, 75))
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
        self.gridLayout_24.addLayout(self.verticalLayout_67, 1, 1, 1, 1)
        spacerItem197 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem197, 1, 2, 1, 1)
        spacerItem198 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_24.addItem(spacerItem198, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage11, "")
        self.tabWidgetPage12 = QtWidgets.QWidget()
        self.tabWidgetPage12.setObjectName("tabWidgetPage12")
        self.gridLayout = QtWidgets.QGridLayout(self.tabWidgetPage12)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem199 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem199, 0, 1, 1, 1)
        spacerItem200 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem200, 1, 0, 1, 1)
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout()
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout()
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.label_26 = QtWidgets.QLabel(self.tabWidgetPage12)
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
        self.groundListWidget = QtWidgets.QListWidget(self.tabWidgetPage12)
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
        self.groundAddButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        self.groundAddButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/plus_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.groundAddButton.setIcon(icon3)
        self.groundAddButton.setIconSize(QtCore.QSize(27, 27))
        self.groundAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.groundAddButton.setAutoRaise(False)
        self.groundAddButton.setObjectName("groundAddButton")
        self.verticalLayout_38.addWidget(self.groundAddButton)
        self.groundRemoveButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.groundRemoveButton.setIcon(icon4)
        self.groundRemoveButton.setIconSize(QtCore.QSize(27, 27))
        self.groundRemoveButton.setAutoRaise(False)
        self.groundRemoveButton.setObjectName("groundRemoveButton")
        self.verticalLayout_38.addWidget(self.groundRemoveButton)
        spacerItem201 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_38.addItem(spacerItem201)
        self.horizontalLayout_55.addLayout(self.verticalLayout_38)
        self.verticalLayout_55.addLayout(self.horizontalLayout_55)
        self.horizontalLayout_59.addLayout(self.verticalLayout_55)
        spacerItem202 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem202)
        self.verticalLayout_54 = QtWidgets.QVBoxLayout()
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.label_27 = QtWidgets.QLabel(self.tabWidgetPage12)
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
        self.armListWidget = QtWidgets.QListWidget(self.tabWidgetPage12)
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
        self.armAddButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        self.armAddButton.setText("")
        self.armAddButton.setIcon(icon3)
        self.armAddButton.setIconSize(QtCore.QSize(27, 27))
        self.armAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.armAddButton.setAutoRaise(False)
        self.armAddButton.setObjectName("armAddButton")
        self.verticalLayout_37.addWidget(self.armAddButton)
        self.armRemoveButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        self.armRemoveButton.setText("")
        self.armRemoveButton.setIcon(icon4)
        self.armRemoveButton.setIconSize(QtCore.QSize(27, 27))
        self.armRemoveButton.setAutoRaise(False)
        self.armRemoveButton.setObjectName("armRemoveButton")
        self.verticalLayout_37.addWidget(self.armRemoveButton)
        spacerItem203 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_37.addItem(spacerItem203)
        self.horizontalLayout_56.addLayout(self.verticalLayout_37)
        self.verticalLayout_54.addLayout(self.horizontalLayout_56)
        self.horizontalLayout_59.addLayout(self.verticalLayout_54)
        self.verticalLayout_58.addLayout(self.horizontalLayout_59)
        spacerItem204 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_58.addItem(spacerItem204)
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout()
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_25 = QtWidgets.QLabel(self.tabWidgetPage12)
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
        self.vesselListWidget = QtWidgets.QListWidget(self.tabWidgetPage12)
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
        self.vesselAddButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        self.vesselAddButton.setText("")
        self.vesselAddButton.setIcon(icon3)
        self.vesselAddButton.setIconSize(QtCore.QSize(27, 27))
        self.vesselAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.vesselAddButton.setAutoRaise(False)
        self.vesselAddButton.setObjectName("vesselAddButton")
        self.verticalLayout_39.addWidget(self.vesselAddButton)
        self.vesselRemoveButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        self.vesselRemoveButton.setText("")
        self.vesselRemoveButton.setIcon(icon4)
        self.vesselRemoveButton.setIconSize(QtCore.QSize(27, 27))
        self.vesselRemoveButton.setAutoRaise(False)
        self.vesselRemoveButton.setObjectName("vesselRemoveButton")
        self.verticalLayout_39.addWidget(self.vesselRemoveButton)
        spacerItem205 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_39.addItem(spacerItem205)
        self.horizontalLayout_57.addLayout(self.verticalLayout_39)
        self.verticalLayout_56.addLayout(self.horizontalLayout_57)
        self.horizontalLayout_60.addLayout(self.verticalLayout_56)
        spacerItem206 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem206)
        self.verticalLayout_57 = QtWidgets.QVBoxLayout()
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_28 = QtWidgets.QLabel(self.tabWidgetPage12)
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
        self.armMobileListWidget = QtWidgets.QListWidget(self.tabWidgetPage12)
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
        self.armMobileAddButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        self.armMobileAddButton.setText("")
        self.armMobileAddButton.setIcon(icon3)
        self.armMobileAddButton.setIconSize(QtCore.QSize(27, 27))
        self.armMobileAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.armMobileAddButton.setAutoRaise(False)
        self.armMobileAddButton.setObjectName("armMobileAddButton")
        self.verticalLayout_40.addWidget(self.armMobileAddButton)
        self.armMobileRemoveButton = QtWidgets.QToolButton(self.tabWidgetPage12)
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
        self.armMobileRemoveButton.setText("")
        self.armMobileRemoveButton.setIcon(icon4)
        self.armMobileRemoveButton.setIconSize(QtCore.QSize(27, 27))
        self.armMobileRemoveButton.setAutoRaise(False)
        self.armMobileRemoveButton.setObjectName("armMobileRemoveButton")
        self.verticalLayout_40.addWidget(self.armMobileRemoveButton)
        spacerItem207 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_40.addItem(spacerItem207)
        self.horizontalLayout_58.addLayout(self.verticalLayout_40)
        self.verticalLayout_57.addLayout(self.horizontalLayout_58)
        self.horizontalLayout_60.addLayout(self.verticalLayout_57)
        self.verticalLayout_58.addLayout(self.horizontalLayout_60)
        self.horizontalLayout_77.addLayout(self.verticalLayout_58)
        spacerItem208 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_77.addItem(spacerItem208)
        self.infoButton_14 = QtWidgets.QToolButton(self.tabWidgetPage12)
        self.infoButton_14.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_14.setStyleSheet("QToolButton {\n"
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
        self.infoButton_14.setText("")
        self.infoButton_14.setIcon(icon1)
        self.infoButton_14.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_14.setAutoRaise(False)
        self.infoButton_14.setObjectName("infoButton_14")
        self.horizontalLayout_77.addWidget(self.infoButton_14)
        self.gridLayout.addLayout(self.horizontalLayout_77, 1, 1, 1, 1)
        spacerItem209 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem209, 1, 2, 1, 1)
        spacerItem210 = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem210, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage12, "")
        self.tabWidgetPage13 = QtWidgets.QWidget()
        self.tabWidgetPage13.setObjectName("tabWidgetPage13")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tabWidgetPage13)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem211 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_12.addItem(spacerItem211, 0, 1, 1, 1)
        spacerItem212 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem212, 1, 0, 1, 1)
        self.OtherCommentsTextBox = QtWidgets.QTextEdit(self.tabWidgetPage13)
        self.OtherCommentsTextBox.setMaximumSize(QtCore.QSize(16777215, 200))
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
        self.gridLayout_12.addWidget(self.OtherCommentsTextBox, 1, 1, 1, 2)
        spacerItem213 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem213, 1, 3, 1, 1)
        spacerItem214 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem214, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage13, "")
        self.tabWidgetPage14 = QtWidgets.QWidget()
        self.tabWidgetPage14.setObjectName("tabWidgetPage14")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tabWidgetPage14)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.verticalLayout_64 = QtWidgets.QVBoxLayout()
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.label_35 = QtWidgets.QLabel(self.tabWidgetPage14)
        self.label_35.setMinimumSize(QtCore.QSize(850, 35))
        self.label_35.setMaximumSize(QtCore.QSize(850, 16777215))
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
        spacerItem215 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_64.addItem(spacerItem215)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        spacerItem216 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem216)
        self.imageAddButton = QtWidgets.QToolButton(self.tabWidgetPage14)
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
        spacerItem217 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem217)
        self.urlAddButton = QtWidgets.QToolButton(self.tabWidgetPage14)
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
        spacerItem218 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem218)
        self.verticalLayout_64.addLayout(self.horizontalLayout_82)
        spacerItem219 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_64.addItem(spacerItem219)
        self.verticalLayout_52 = QtWidgets.QVBoxLayout()
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.verticalLayout_64.addLayout(self.verticalLayout_52)
        self.gridLayout_22.addLayout(self.verticalLayout_64, 1, 1, 1, 1)
        spacerItem220 = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem220, 1, 2, 1, 1)
        spacerItem221 = QtWidgets.QSpacerItem(20, 214, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem221, 2, 1, 1, 1)
        spacerItem222 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem222, 1, 0, 1, 1)
        spacerItem223 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_22.addItem(spacerItem223, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage14, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
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
        self.label_4.setText(_translate("MainWindow", "Project acronym:"))
        self.label_3.setText(_translate("MainWindow", "Date (yyyy-mm-dd):"))
        self.dateLine.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_2.setText(_translate("MainWindow", "Flight identifier:"))
        self.label_5.setText(_translate("MainWindow", "Mission scientist:"))
        self.label_6.setText(_translate("MainWindow", "Flight manager:"))
        self.label_8.setText(_translate("MainWindow", "Operator:"))
        self.operatorList.setItemText(0, _translate("MainWindow", "Make a choice..."))
        self.operatorList.setItemText(1, _translate("MainWindow", "Other..."))
        self.operatorList.setItemText(2, _translate("MainWindow", "Alfred Wegener Institute"))
        self.operatorList.setItemText(3, _translate("MainWindow", "CNR - Istituto per i Sistemi Agricoli e Forestali del Mediterraneo"))
        self.operatorList.setItemText(4, _translate("MainWindow", "CNR - Istituto di Metodologie per l\'Analisi Ambientale"))
        self.operatorList.setItemText(5, _translate("MainWindow", "Deutsches Zentrum fur Luft- und Raumfahrt"))
        self.operatorList.setItemText(6, _translate("MainWindow", "ENVISCOPE"))
        self.operatorList.setItemText(7, _translate("MainWindow", "NERC - Facility for Airborne Atmospheric Measurements"))
        self.operatorList.setItemText(8, _translate("MainWindow", "FUB - Institut fur Weltraumwissenschaften"))
        self.operatorList.setItemText(9, _translate("MainWindow", "Instituto Nacional de Tecnica Aeroespacial"))
        self.operatorList.setItemText(10, _translate("MainWindow", "KIT - Institute of Meteorology and Climate Research"))
        self.operatorList.setItemText(11, _translate("MainWindow", "NERC - Airborne Research and Survey Facility"))
        self.operatorList.setItemText(12, _translate("MainWindow", "NERC - British Antarctic Survey"))
        self.operatorList.setItemText(13, _translate("MainWindow", "SAFIRE"))
        self.operatorList.setItemText(14, _translate("MainWindow", "UEDIN - Airborne GeoSciences"))
        self.label_7.setText(_translate("MainWindow", "Platform/Aircraft:"))
        self.label_9.setText(_translate("MainWindow", "Location:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Flight Information"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_10.setText(_translate("MainWindow", "Role:"))
        self.contactRoleBox.setItemText(0, _translate("MainWindow", "Make a choice..."))
        self.contactRoleBox.setItemText(1, _translate("MainWindow", "Flight Manager"))
        self.contactRoleBox.setItemText(2, _translate("MainWindow", "Mission Scientist"))
        self.contactRoleBox.setItemText(3, _translate("MainWindow", "Other"))
        self.contactRoleBox.setItemText(4, _translate("MainWindow", "Pilot"))
        self.contactRoleBox.setItemText(5, _translate("MainWindow", "Scientist"))
        self.label_11.setText(_translate("MainWindow", "E-mail:"))
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


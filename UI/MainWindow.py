# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListView, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 569)
        MainWindow.setMinimumSize(QSize(600, 200))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 0))
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"background-image: url(\"UI/images/todobg.jpg\");\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Snap ITC"])
        font.setPointSize(48)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(204, 167, 255);\n"
"background-color: rgba(0, 0, 0, 90);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(500, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_add = QPushButton(self.frame_3)
        self.bt_add.setObjectName(u"bt_add")
        self.bt_add.setMinimumSize(QSize(55, 40))
        self.bt_add.setMaximumSize(QSize(55, 40))
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(28)
        font1.setBold(False)
        self.bt_add.setFont(font1)
        self.bt_add.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(204, 167, 255);\n"
"border-radius: 15px;\n"
"border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"background-color: rgb(204, 167, 180);\n"
"border-radius: 10px;\n"
"border: 2px solid black; }\n"
"")
        icon = QIcon()
        icon.addFile(u"UI/images/plusicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_add.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.bt_add)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_widgets = QFrame(self.centralwidget)
        self.frame_widgets.setObjectName(u"frame_widgets")
        self.frame_widgets.setMinimumSize(QSize(500, 350))
        self.frame_widgets.setFrameShape(QFrame.NoFrame)
        self.frame_widgets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_widgets)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.frame_widgets)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"background-color: rgba(254, 249, 255, 80);")
        self.listView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setSelectionMode(QAbstractItemView.NoSelection)
        self.listView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listView.setTextElideMode(Qt.ElideNone)
        self.listView.setSpacing(25)
        self.listView.setUniformItemSizes(True)
        self.listView.setBatchSize(50)
        self.listView.setSelectionRectVisible(False)
        self.listView.setItemAlignment(Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.listView)


        self.verticalLayout.addWidget(self.frame_widgets)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"toDo.", None))
        self.bt_add.setText("")
    # retranslateUi


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
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QSize(600, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 0))
        self.centralwidget.setStyleSheet(u"")
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
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Sitka Text"])
        font.setPointSize(48)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(218, 218, 189, 255), stop:1 rgba(198, 198, 172, 255));")
        self.label.setAlignment(Qt.AlignCenter)

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
        self.bt_add.setMinimumSize(QSize(45, 45))
        self.bt_add.setMaximumSize(QSize(45, 45))
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(28)
        font1.setBold(False)
        self.bt_add.setFont(font1)
        self.bt_add.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 10px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(218, 218, 189, 255), stop:1 rgba(198, 198, 172, 255));\n"
"}\n"
"")

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
        self.bt_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi


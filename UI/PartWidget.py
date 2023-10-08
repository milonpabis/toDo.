# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'part.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 60)
        Form.setMinimumSize(QSize(0, 60))
        Form.setMaximumSize(QSize(16777215, 60))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.301, x2:1, y2:0.772727, stop:0.122222 rgba(234, 235, 204, 255), stop:0.127778 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(60, 0))
        self.frame.setMaximumSize(QSize(60, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, -1, -1, -1)
        self.check_done = QCheckBox(self.frame)
        self.check_done.setObjectName(u"check_done")
        self.check_done.setMinimumSize(QSize(12, 12))
        self.check_done.setMaximumSize(QSize(12, 12))
        self.check_done.setIconSize(QSize(16, 16))
        self.check_done.setTristate(False)

        self.verticalLayout.addWidget(self.check_done)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(260, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.stacked_text = QStackedWidget(self.frame_2)
        self.stacked_text.setObjectName(u"stacked_text")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_3 = QHBoxLayout(self.page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_text = QLabel(self.page)
        self.l_text.setObjectName(u"l_text")
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(10)
        font.setBold(True)
        self.l_text.setFont(font)

        self.horizontalLayout_3.addWidget(self.l_text)

        self.stacked_text.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.le_editext = QLineEdit(self.page_2)
        self.le_editext.setObjectName(u"le_editext")
        self.le_editext.setMinimumSize(QSize(200, 35))
        self.le_editext.setMaximumSize(QSize(16777215, 35))
        self.le_editext.setFont(font)

        self.horizontalLayout_4.addWidget(self.le_editext)

        self.stacked_text.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stacked_text)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(180, 60))
        self.frame_3.setMaximumSize(QSize(180, 60))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.stacked_buttons = QStackedWidget(self.frame_3)
        self.stacked_buttons.setObjectName(u"stacked_buttons")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_5 = QHBoxLayout(self.page_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_edit = QPushButton(self.page_3)
        self.bt_edit.setObjectName(u"bt_edit")
        self.bt_edit.setMinimumSize(QSize(50, 35))
        self.bt_edit.setMaximumSize(QSize(50, 35))
        self.bt_edit.setSizeIncrement(QSize(50, 35))
        self.bt_edit.setFont(font)
        self.bt_edit.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 8px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(218, 218, 189, 255), stop:1 rgba(198, 198, 172, 255));\n"
"}")

        self.horizontalLayout_5.addWidget(self.bt_edit)

        self.bt_delete = QPushButton(self.page_3)
        self.bt_delete.setObjectName(u"bt_delete")
        self.bt_delete.setMinimumSize(QSize(50, 35))
        self.bt_delete.setMaximumSize(QSize(50, 35))
        self.bt_delete.setSizeIncrement(QSize(50, 35))
        self.bt_delete.setFont(font)
        self.bt_delete.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 8px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(218, 218, 189, 255), stop:1 rgba(198, 198, 172, 255));\n"
"}")

        self.horizontalLayout_5.addWidget(self.bt_delete)

        self.stacked_buttons.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_6 = QHBoxLayout(self.page_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_cancel = QPushButton(self.page_4)
        self.bt_cancel.setObjectName(u"bt_cancel")
        self.bt_cancel.setMinimumSize(QSize(50, 35))
        self.bt_cancel.setMaximumSize(QSize(50, 35))
        self.bt_cancel.setFont(font)
        self.bt_cancel.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 8px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(218, 218, 189, 255), stop:1 rgba(198, 198, 172, 255));\n"
"}")

        self.horizontalLayout_6.addWidget(self.bt_cancel)

        self.bt_save = QPushButton(self.page_4)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setMinimumSize(QSize(50, 35))
        self.bt_save.setMaximumSize(QSize(50, 35))
        self.bt_save.setFont(font)
        self.bt_save.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 8px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(218, 218, 189, 255), stop:1 rgba(198, 198, 172, 255));\n"
"}")

        self.horizontalLayout_6.addWidget(self.bt_save)

        self.stacked_buttons.addWidget(self.page_4)

        self.horizontalLayout_2.addWidget(self.stacked_buttons)


        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        self.stacked_text.setCurrentIndex(1)
        self.stacked_buttons.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.check_done.setText("")
        self.l_text.setText("")
        self.stacked_buttons.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 8px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(234, 235, 204, 255), stop:1 rgba(218, 218, 189, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.721591, stop:0.1 rgba(218, 218, 189, 255), stop:1 rgba(198, 198, 172, 255));\n"
"}", None))
        self.bt_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.bt_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.bt_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.bt_save.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi


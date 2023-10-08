from UI.MainWindow import Ui_MainWindow
from UI.PartWidget import Ui_Form
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QListView, QFrame
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("toDo.")


        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.bt_add.pressed.connect(self.add_item)




    def add_item(self):
        self.bt_add.setDisabled(True)
        widget = PartWidget()
        widget.bt_delete.pressed.connect(lambda: self.delete_item(widget))
        widget.bt_save.pressed.connect(lambda: self.bt_add.setDisabled(False))
        widget.bt_cancel.pressed.connect(lambda: self.bt_add.setDisabled(False))
        widget.item = QStandardItem()
        widget.item.setSelectable(False)
        self.model.appendRow(widget.item)
        self.listView.setIndexWidget(widget.item.index(), widget)

    def delete_item(self, it):
        self.model.removeRow(it.item.row())





class PartWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.item = None
        self.bt_edit.pressed.connect(self.edit)
        self.bt_save.pressed.connect(self.save)
        self.bt_cancel.pressed.connect(self.cancel)


    def edit(self):
        self.le_editext.setText(self.l_text.text())
        self.change_widget(1)

    def cancel(self):
        self.le_editext.setText('')
        self.change_widget(0)

    def save(self):
        text = self.le_editext.text()
        self.l_text.setText(text)
        self.change_widget(0)

    def change_widget(self, idx):
        self.stacked_text.setCurrentIndex(idx)
        self.stacked_buttons.setCurrentIndex(idx)









from UI.MainWindow import Ui_MainWindow
from UI.PartWidget import Ui_Form
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QListView, QFrame
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt
from db_connect import DataBaseControl



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("toDo.")
        self.db = DataBaseControl()

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.bt_add.pressed.connect(self.add_item)

        data = self.db.return_data()
        for checked, text in data:
            self.add_item(checked, text)




    def add_item(self, *args):
        if args:
            widget = PartWidget(args[0], args[1])
        else:
            self.bt_add.setDisabled(True)
            widget = PartWidget()
        widget.bt_delete.pressed.connect(lambda: self.delete_item(widget))
        widget.bt_save.pressed.connect(lambda: self.bt_add.setDisabled(False))
        widget.bt_cancel.pressed.connect(lambda: self.bt_add.setDisabled(False))
        widget.bt_save.pressed.connect(lambda: self.save_db(widget))
        widget.check_done.stateChanged.connect(lambda: self.save_checks(widget))
        self.model.appendRow(widget.item)
        self.listView.setIndexWidget(widget.item.index(), widget)

    def delete_item(self, it):
        self.model.removeRow(it.item.row())
        self.db.delete_data(it.l_text.text())

    def save_db(self, widget):
        new = widget.new
        text = widget.le_editext.text()
        p_text = widget.l_text.text()
        if new:
            widget.new = False
            self.db.insert_data(text)
        else:
            self.db.update_data(text, p_text)
        widget.l_text.setText(text)

    def save_checks(self, widget):
        state = widget.check_done.isChecked()
        text = widget.l_text.text()
        self.db.save_check(state, text)








class PartWidget(QWidget, Ui_Form):

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.item = QStandardItem()
        self.item.setSelectable(False)
        self.new = True
        self.bt_edit.pressed.connect(self.edit)
        self.bt_save.pressed.connect(self.save)
        self.bt_cancel.pressed.connect(self.cancel)
        if args:
            self.new = False
            self.check_done.setChecked(bool(args[0]))
            self.l_text.setText(args[1])
            self.change_widget(0)


    def edit(self):
        self.le_editext.setText(self.l_text.text())
        self.change_widget(1)

    def cancel(self):
        if self.new:
            self.bt_delete.click()
        self.le_editext.setText('')
        self.change_widget(0)

    def save(self):
        self.change_widget(0)

    def change_widget(self, idx):
        self.stacked_text.setCurrentIndex(idx)
        self.stacked_buttons.setCurrentIndex(idx)









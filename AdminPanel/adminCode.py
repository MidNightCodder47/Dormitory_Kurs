import sys
import sqlite3

from PyQt6.QtWidgets import QFormLayout, QDialog, QLineEdit


class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Добавить пользователя")
        self.setModal(True)
        self.resize(300, 200)

        layout = QFormLayout(self)

        self.addbutton.clicked.connect(self.on_add_clicked)

    def on_add_clicked(self):
        # user_login, user_password, firstname, lastname,patronymic,room_num,contract,mail

        self.username_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.role_edit = QLineEdit()

        layout.addRow("Имя пользователя:", self.username_edit)
        layout.addRow("Email:", self.email_edit)
        layout.addRow("Роль:", self.role_edit)


        layout.addRow(buttons)

    def get_data(self):
        return {
            'username': self.username_edit.text(),
            'email': self.email_edit.text(),
            'role': self.role_edit.text()
        }

class Admin():
    def __init__(self):
        super().__init__()

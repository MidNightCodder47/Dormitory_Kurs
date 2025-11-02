import sqlite3

import PyQt6
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class postcode(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('postUI.ui', self)
        self.button_send.clicked.connect(self.clicked())
    def clicked(self):
        text = self.text_input.text()
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()

        c.execute('''insert into post''')


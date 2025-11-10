import sys
from pathlib import Path
from PyQt6 import uic

import sqlite3

from PyQt6.QtWidgets import QDialog

conn = sqlite3.connect('hotel.db')
c = conn.cursor()
class win_text(QDialog):
    def __init__(self,app_id):
        super().__init__()
        uic.loadUi('app_window.ui',self)
        self.setWindowTitle("Заявление")
        self.app_id = app_id
        self.load_data(app_id)

    def load_data(self,id):
        self.app_id = id
        c.execute('''SELECT app_title,app_text,app_date FROM application WHERE id_application = ?''',(self.app_id,))
        res = c.fetchone()
        title = res[0]
        text = res[1]
        date = res[2]

        self.app_title.setText(title)
        self.app_text.setText(text)
        self.app_date.setText(date)

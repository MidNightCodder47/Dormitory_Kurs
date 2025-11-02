import sys
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QListWidgetItem
from PyQt6.uic.properties import QtWidgets

from app_win_text_UI import Ui_Dialog
import sqlite3

class win_text(Ui_Dialog):
    def __init__(self,app_id):
        super().__init__()
        self.setupUi(self)
        self.app_id = app_id
        self.load_data(app_id)

    def load_data(self,id):
        try:
            conn = sqlite3.connect('hotel.db')
            c = conn.cursor()
            self.app_id = id
            c.execute('''SELECT app_title,app_text,app_date FROM application WHERE id_application = ?''',(self.app_id,))
            res = c.fetchone()
            title = res[0]
            text = res[1]
            date = res[2]

            self.app_title.setText(title)
            self.app_text.setText(text)
            self.app_date.setText(date)

            conn.close()
        except Exception as e:
            print(e)



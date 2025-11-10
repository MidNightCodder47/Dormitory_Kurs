import sqlite3
from datetime import date

import PyQt6
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox


class postcode(QDialog):
    def __init__(self,mainwin=None):
        super().__init__()
        uic.loadUi('postUI.ui', self)
        self.setWindowTitle("Новый пост")
        self.main_window = mainwin
        self.button_send.clicked.connect(self.clicked)
    def clicked(self):
        try:
            text = self.post_text.toPlainText()
            if not text:
                QMessageBox.warning(self, "Ошибка", "Введите все поля")
                return
            conn = sqlite3.connect('hotel.db')
            c = conn.cursor()

            c.execute('''insert into post (post_title,post_date)
                        VALUES (?,?)''',(text,str(date.today())))
            conn.commit()
            conn.close()
            self.main_window.fill_posts()
            self.close()
        except Exception as e:
            print("Post code / clicked")
            print(e)
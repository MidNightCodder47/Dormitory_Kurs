import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QListWidgetItem, QWidget, QVBoxLayout, QLabel
from pathlib import Path

from PyQt6 import QtGui

import app_win_text_code
import addUserCode

class TextItemWidget(QWidget):
    def __init__(self,text):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(10,5,10,5)

        self.label = QLabel(text)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        layout.addWidget(self.label)
        self.setLayout(layout)


class Admin(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_AdminWindow()
        uic.loadUi('adminwindow.ui', self)
        try:
            self.load_data()
            self.addUserBtn.clicked.connect(self.on_addusr_clicked)
            self.appList.itemClicked.connect(self.on_app_clicked)
            self.fill_posts()
        except Exception as e:
            print(e)
    def load_data(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()

        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["id","Фамилия","Имя","Отчество","Логин","Пароль", "Комната", "Почта","Телефон","Контракт"])

        c.execute('SELECT * FROM user')
        rows = c.fetchall()

        self.tableWidget.setRowCount(len(rows))
        for row_num, row in enumerate(rows):
            for col_num, value in enumerate(row):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(value)))

        self.appList.clear()



        c.execute('''SELECT id_application,app_title,app_date FROM application ''')
        applications = c.fetchall()


        for id, title, date_app in applications:
            app_text = f"{id} {title} {date_app}"

            app = QListWidgetItem(app_text)

            self.appList.addItem(app)

        conn.close()
    def on_app_clicked(self,item):
        try:
            app_id = int(item.text().split()[0])
            self.app_text_window = app_win_text_code.win_text(app_id)
            self.app_text_window.show()
        except Exception as e:
            print(e)
    def on_addusr_clicked(self):
        self.addUser_window = addUserCode.addUserCode()
        self.addUser_window.show()

    def fill_posts(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()
        c.execute('''SELECT post_title, post_date FROM post ORDER BY id_post DESC''')
        posts = c.fetchall()
        self.notesList.clear()

        for post_title, post_date in posts:
            text = f"{post_title}\n\n{post_date}"
            widget = TextItemWidget(text)
            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())

            self.notesList.addItem(item)
            self.notesList.setItemWidget(item, widget)
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Admin()
    window.show()
    sys.exit(app.exec())
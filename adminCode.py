import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QListWidgetItem, QWidget, QVBoxLayout, QLabel, \
    QTableWidget
from pathlib import Path

from PyQt6 import QtGui

import app_win_text_code,addUserCode,PostCode,chngSummCode



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
        self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)

        try:
            self.load_data()
            self.addUserBtn.clicked.connect(self.on_addusr_clicked)
            self.appList.itemClicked.connect(self.on_app_clicked)
            self.addpost.clicked.connect(self.on_add_post_clicked)
            self.changesumma.clicked.connect(self.chng_sum_clicked)
            self.fill_posts()
        except Exception as e:
            print("админ инит")
            print(e)
    def load_data(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()

        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["id","Фамилия","Имя","Отчество","Логин","Пароль", "Комната", "Контракт","Телефон","Почта"])

        c.execute('SELECT * FROM user')
        rows = c.fetchall()

        self.tableWidget.setRowCount(len(rows))
        for row_num, row in enumerate(rows):
            for col_num, value in enumerate(row):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(value)))

        self.tableWidget.cellChanged.connect(self.on_cell_changed)


        self.appList.clear()

        c.execute('''SELECT a.id_application,u.lastname, u.firstname,u.patronymic,a.app_title,a.app_date FROM application a INNER JOIN user u ON a.user_id = u.id_user ''')
        applications = c.fetchall()


        for id, lastname,firsname,patronymic,title, date_app in applications:
            app_text = f"{id} {lastname} {firsname} {patronymic} {title} {date_app}"

            app = QListWidgetItem(app_text)

            self.appList.addItem(app)

        conn.close()

    def on_cell_changed(self, row, column):
        try:
            if column == 0:  # Не позволяем редактировать ID
                return

            user_id = self.tableWidget.item(row, 0).text()
            new_value = self.tableWidget.item(row, column).text()

            field_names = ["", "lastname", "firstname", "patronymic", "login",
                           "password", "room_number", "email", "phone", "contract"]

            if 1 <= column < len(field_names):
                field_name = field_names[column]
                self.update_user_in_db(user_id, field_name, new_value)
        except Exception as e:
            print(f"Ошибка при обновлении: {e}")

    def update_user_in_db(self, user_id, field_name, new_value):
        try:
            conn = sqlite3.connect('hotel.db')
            c = conn.cursor()


            query = f'UPDATE user SET {field_name} = ? WHERE id_user = ?'
            c.execute(query, (new_value, user_id))

            conn.commit()
            conn.close()
            print(f"Обновлен пользователь {user_id}: {field_name} = '{new_value}'")

        except Exception as e:
            print(f"Ошибка БД при обновлении {field_name}: {e}")


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
    def chng_sum_clicked(self):
        self.chng_sum_win = chngSummCode.chngsumma()
        self.chng_sum_win.show()
    def on_add_post_clicked(self):
        try:
            self.addPost_window = PostCode.postcode(self)
            self.addPost_window.show()
        except Exception as e:
            print("on_add_post_clicked")
            print(e)
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
from PyQt6.QtGui import QFont, QMouseEvent
from PyQt6.QtWidgets import QDialog, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, \
    QMainWindow
from PyQt6 import QtGui, QtCore,uic

import app_win_text_code
import applicationCode

import sys
import sqlite3



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
        self.label.setContentsMargins(10,5,10,5)

        layout.addWidget(self.label)
        self.setLayout(layout)


class MainUserWindow(QDialog):
    def __init__(self,user_id):
        super().__init__()

        uic.loadUi('MainWindowV2.ui',self)
        self.setWindowTitle("Личный кабинет")

        self.setup_window()
        self.user_id = user_id
        self.list_post = QListWidget()

        self.fill_posts()
        self.get_user_data()
        self.load_operations()
        self.button_add_doc.clicked.connect(self.on_add_app_clicked)
        self.appList.itemClicked.connect(self.on_app_clicked)

    def setup_window(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.setGeometry(screen_geometry)
        self.setFixedSize(self.size())
        self.center_window()

    def center_window(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())
    def get_user_data(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()

        c.execute("SELECT firstname, lastname, patronymic, room_num, contract, phone, mail, user_login FROM user WHERE id_user = ?",(self.user_id,))
        result = c.fetchone()

        self.firstname = result[0]
        self.lastname = result[1]
        self.patronymic = result[2]
        self.room_num = result[3]
        self.contract = result[4]
        self.phone = result[5]
        self.mail = result[6]
        self.login = result[7]

        self.user_name.setText(f"{self.lastname} {self.firstname} {self.patronymic}")
        self.user_mail.setText(f"Почта: {self.mail}")
        self.user_phone.setText(f"Телефон: {self.phone}")
        self.user_contract.setText(f"Договор: №{self.contract}")
        self.user_login.setText(f"Логин: {self.login}")
        self.user_room.setText(f"Номер комнаты: {self.room_num}")


        c.execute('''SELECT lastname,firstname,patronymic FROM user WHERE room_num = ? and id_user != ?''', (self.room_num,self.user_id,))
        neighbours = c.fetchall()

        for last_name, first_name, middle_name in neighbours:
            full_name = f"{last_name} {first_name} {middle_name or ''}"

            label = QListWidgetItem(full_name)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(15)
            label.setFont(font)

            self.neighboursList.addItem(label)



        c.execute(
            "SELECT user_balance,month_price FROM finance WHERE contract = ?",(self.contract,))
        result = c.fetchone()
        if not result:
            print("Ошибка подгрузки баланса и стоимости")
            self.balance = "Error"
            self.month_price = "Error"
        else:
            self.balance = result[0]
            self.month_price = result[1]

        self.user_credit.setText(f"{self.balance}")
        self.price_per_month.setText(f"{self.month_price}")

        self.appList.clear()

        c.execute('''SELECT id_application,app_title,app_date FROM application WHERE user_id = ?''',(self.user_id,))
        applications = c.fetchall()

        for id,title,date_app in applications:
            app_text = f"{id} {title} {date_app}"
            app = QListWidgetItem(app_text)

            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)

            app.setFont(font)

            self.appList.addItem(app)

        conn.close()
    def upd_applications(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()
        self.appList.clear()

        c.execute('''SELECT id_application,app_title,app_date FROM application WHERE user_id = ?''',
                       (self.user_id,))
        applications = c.fetchall()

        for id, title, date_app in applications:
            app_text = f"{id} {title} {date_app}"
            app = QListWidgetItem(app_text)

            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)

            app.setFont(font)

            self.appList.addItem(app)
        conn.close()

    def on_add_app_clicked(self):
        self.appwindow = applicationCode.Application(self.user_id,self)
        self.appwindow.show()

    def on_app_clicked(self,item):
        try:
            app_id = int(item.text().split()[0])
            self.app_text_window = app_win_text_code.win_text(app_id)
            self.app_text_window.show()
        except Exception as e:
            print(e)

    def open_application(self,event,app_id):
        try:
            if isinstance(event, QMouseEvent):
                self.app_text_window = app_win_text_code.win_text(app_id)
                self.app_text_window.show()
        except Exception as e:
            print("error in open_application")
            print(e)
    def load_operations(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()

        c.execute('''SELECT summa,oper_text,oper_date FROM operations WHERE contract = ?''',(self.contract,))
        operations = c.fetchall()
        for summa,oper_text,oper_date in operations:
            app_text = f"{summa} {oper_text} {oper_date}"
            app = QListWidgetItem(app_text)

            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)

            app.setFont(font)

            self.operationsList.addItem(app)
        conn.close()

    def fill_posts(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()
        c.execute('''SELECT post_title, post_date FROM post ORDER BY id_post DESC''')
        posts = c.fetchall()

        for post_title, post_date in posts:
            text = f"{post_title}\n\n{post_date}"
            widget = TextItemWidget(text)
            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())

            self.postList.addItem(item)
            self.postList.setItemWidget(item, widget)
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainUserWindow(1)
    window.setWindowTitle("Личный кабинет")
    window.show()
    sys.exit(app.exec())

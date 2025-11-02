from PyQt6.QtGui import QFont, QMouseEvent
from PyQt6.QtWidgets import QDialog, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt6 import QtGui, QtCore

import app_win_text_code
import applicationCode
from MainWindowV2 import MainWindow
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

        layout.addWidget(self.label)
        self.setLayout(layout)


class MainUserWindow(MainWindow):
    def __init__(self,user_id):
        super().__init__()
        self.user_id = user_id
        self.list_post = QListWidget()

        self.fill_posts()
        self.scroll_layout_4.addWidget(self.list_post)
        self.scroll_layout_4.addStretch()
        self.get_user_data()
        self.button_add_doc.clicked.connect(self.on_add_app_clicked)

    def upd_applications(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()
        while self.scroll_layout_app.count():
            current = self.scroll_layout_app.takeAt(0)
            if current.widget():
                current.widget().deleteLater()

        c.execute('''SELECT id_application,app_title,app_date FROM application WHERE user_id = ?''',
                       (self.user_id,))
        applications = c.fetchall()

        for id, title, date_app in applications:
            app = f"{id} {title} {date_app}"
            label_app = QLabel(app)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)
            label_app.setFont(font)
            label_app.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
            label_app.setWordWrap(True)

            label_app.mousePressEvent = lambda e, app_id=id: self.open_application(e, app_id)
            self.scroll_layout_app.addWidget(label_app)
        self.scroll_layout_app.addStretch()
        conn.close()
    def on_add_app_clicked(self):
        self.appwindow = applicationCode.Application(self.user_id,self)
        self.appwindow.show()

    def open_application(self,event,app_id):
        try:
            if isinstance(event, QMouseEvent):
                self.app_text_window = app_win_text_code.win_text(app_id)
                self.app_text_window.show()
        except Exception as e:
            print(e)
    def get_user_data(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()

        c.execute("SELECT firstname,lastname,patronymic,room_num,contract,phone,mail,user_login FROM user WHERE id_user = ?",(self.user_id,))
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
        self.user_ident.setText(f"ID: {self.user_id}")
        self.user_mail.setText(f"Почта: {self.mail}")
        self.user_phone.setText(f"Телефон: {self.phone}")
        self.user_contract.setText(f"Договор: №{self.contract}")
        self.user_login.setText(f"Логин: {self.login}")
        self.user_room.setText(f"Номер комнаты: {self.room_num}")


        c.execute('''SELECT lastname,firstname,patronymic FROM user WHERE room_num = ? and id_user != ?''', (self.room_num,self.user_id,))
        neighbours = c.fetchall()

        for last_name, first_name, middle_name in neighbours:
            full_name = f"{last_name} {first_name} {middle_name or ''}"
            label = QLabel(full_name)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)
            label.setFont(font)
            self.scroll_layout_2.addWidget(label)
        self.scroll_layout_2.addStretch()


        c.execute(
            "SELECT user_balance,month_price FROM finance WHERE contract = ?",(self.contract,))
        result = c.fetchone()

        self.balance = result[0]
        self.month_price = result[1]

        self.user_credit.setText(f"{self.balance}")
        self.price_per_month.setText(f"{self.month_price}")

        c.execute('''SELECT id_application,app_title,app_date FROM application WHERE user_id = ?''',(self.user_id,))
        applications = c.fetchall()

        for id,title,date_app in applications:
            app = f"{id} {title} {date_app}"
            label_app = QLabel(app)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)
            label_app.setFont(font)
            label_app.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
            label_app.setWordWrap(True)

            label_app.mousePressEvent = lambda e, app_id=id:self.open_application(e,app_id)
            self.scroll_layout_app.addWidget(label_app)
        self.scroll_layout_app.addStretch()
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

            self.list_post.addItem(item)
            self.list_post.setItemWidget(item, widget)
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUserWindow(2)
    window.setWindowTitle("Home page")
    window.show()
    sys.exit(app.exec())

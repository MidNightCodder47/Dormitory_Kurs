from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QMouseEvent
from PyQt6.QtWidgets import QDialog, QApplication, QLabel
from PyQt6.uic.Compiler.qtproxies import QtWidgets
from PyQt6 import QtGui, QtCore

import applicationCode
from MainWindowV2 import MainWindow
import sys
import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()

class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()


class MainUserWindow(MainWindow):


    def __init__(self,user_id):
        super().__init__()
        self.user_id = user_id
        self.get_user_data()
        self.button_add_doc.clicked.connect(self.on_add_app_clicked)
    def upd_applications(self):

        while self.scroll_layout_app.count():
            current = self.scroll_layout_app.takeAt(0)
            if current.widget():
                current.widget().deleteLater()
        self.c.execute('''SELECT id_application,app_title,app_date FROM application WHERE user_id = ?''',
                       (self.user_id,))
        applications = self.c.fetchall()

        for id, title, date_app in applications:
            app = f"{id} {title} {date_app}"
            label_app = QLabel(app)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)
            label_app.setFont(font)
            self.scroll_layout_app.addWidget(label_app)
        self.scroll_layout_app.addStretch()

    def on_add_app_clicked(self):
        self.appwindow = applicationCode.Application(self.user_id,self)
        self.appwindow.show()

    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()

    def open_application(self,event,id):
        if isinstance(event, QMouseEvent):
            print(f"переход{id}")

    def get_user_data(self):
        self.conn = sqlite3.connect('hotel.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT firstname,lastname,patronymic,room_num,contract,phone,mail,user_login FROM user WHERE id_user = ?",(self.user_id,))
        result = self.c.fetchone()

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


        self.c.execute('''SELECT lastname,firstname,patronymic FROM user WHERE room_num = ? and id_user != ?''', (self.room_num,self.user_id,))
        neighbours = self.c.fetchall()

        for last_name, first_name, middle_name in neighbours:
            full_name = f"{last_name} {first_name} {middle_name or ''}"
            label = QLabel(full_name)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift")
            font.setPointSize(13)
            label.setFont(font)
            self.scroll_layout_2.addWidget(label)
        self.scroll_layout_2.addStretch()



        self.c.execute(
            "SELECT user_balance,month_price FROM finance WHERE contract = ?",(self.contract,))
        result = self.c.fetchone()

        self.balance = result[0]
        self.month_price = result[1]

        self.user_credit.setText(f"{self.balance}")
        self.price_per_month.setText(f"{self.month_price}")
        try:
            # welcome_label = ClickLabel('ТЕСТ')
            # welcome_label.clicked.connect(lambda: welcome_label.setText("OK"))
            # welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            # welcome_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            # form_layout.addWidget(welcome_label)

            self.c.execute('''SELECT id_application,app_title,app_date FROM application WHERE user_id = ?''',(self.user_id,))
            applications = self.c.fetchall()

            for id,title,date_app in applications:
                app = f"{id} {title} {date_app}"
                label_app = ClickLabel(app)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift")
                font.setPointSize(13)
                label_app.setFont(font)
                label_app.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
                label_app.setWordWrap(True)

                label_app.mousePressEvent = self.open_application(id=id,event=QMouseEvent)

                self.scroll_layout_app.addWidget(label_app)
            self.scroll_layout_app.addStretch()


        except Exception as e:
            print(e)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUserWindow(2)
    window.setWindowTitle("Home page")
    window.show()
    sys.exit(app.exec())


    







from PyQt6.QtWidgets import QDialog, QApplication, QLabel
from PyQt6.uic.Compiler.qtproxies import QtWidgets
from PyQt6 import QtGui

from MainWindowV2 import MainWindow
import sys
import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()


class MainUserWindow(MainWindow):
    def __init__(self,user_id):
        super().__init__()
        self.user_id = user_id
        self.get_user_data()
        # self.load_neighbours()


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





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUserWindow(2)
    window.setWindowTitle("Home page")
    window.show()
    sys.exit(app.exec())


    







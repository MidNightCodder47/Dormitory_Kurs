import sys
import sqlite3
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QMessageBox
from  PyQt6 import uic


class addUserCode(QDialog):
    def __init__(self,mainwin=None):
        super().__init__()
        self.main_window = mainwin
        uic.loadUi('adduserwin.ui', self)
        self.setWindowTitle("Добавление пользователя")
        self.adduser.clicked.connect(self.on_add_clicked)

    def on_add_clicked(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()
        try:
            lastname = self.ntrlast.text()
            firstname = self.ntrfirst.text()
            patr = self.ntrthird.text()
            login = self.ntrlogin.text()
            password = self.ntrpassword.text()
            roomnum = self.ntrroomnum.text()
            contract = self.ntrcontract.text()
            phone = self.ntrphone.text()
            mail = self.ntrmail.text()
            mprice = self.ntrmonthprice.text()


            count = 0
            for i in (lastname, firstname, patr,login, password, roomnum, contract, phone, mail, mprice):
                if not i:
                    count += 1
            if count>=1:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
            else:
                c.execute(f'''Insert into user(lastname, firstname,patronymic,user_login, user_password,room_num,contract,phone,mail)
                            Values (?,?,?,?,?,?,?,?,?)''', (lastname, firstname, patr,login, password, roomnum, contract, phone, mail))
                c.execute('''INSERT INTO finance(contract,month_price) values(?,?)''',(contract,mprice))
                conn.commit()
                conn.close()
                self.main_window.user_upd()
                self.close()
        except Exception as e:
            print("AddUserCode")
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = addUserCode()
    window.show()
    sys.exit(app.exec())
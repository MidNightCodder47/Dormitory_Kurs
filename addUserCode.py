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

    def valid_mail(self,mail):
        if not mail or '@' not in mail:
            QMessageBox.warning(self, "Ошибка", "Email должен содержать символ @")
            return False

        parts = mail.split('@')
        if len(parts) != 2 or '.' not in parts[1]:
            QMessageBox.warning(self, "Ошибка","Некорректный формат email")
            return False
        return True

    def validate_phone(self,phone):
        if not phone.isdigit():
            QMessageBox.warning(self, "Ошибка","Телефон должен содержать только цифры")
            return False
        if len(phone) != 11:
            QMessageBox.warning(self,"Ошибка", "Телефон должен содержать 11 цифр")
            return False
        if not phone.startswith('7'):
            QMessageBox.warning(self, "Ошибка","Телефон должен начинаться с 7")
            return False
        return True

    def validate_fio(self,fio):
        if any(char.isdigit() for char in fio):
            QMessageBox.warning(self,"Ошибка", "ФИО не должно содержать цифр")
            return False
        return True

    def validate_month_price(self,price):
        if not price.isdigit():
            QMessageBox.warning(self,"Ошибка", "Сумма не число")
            return False
        return True

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
            elif(self.validate_fio(f"{lastname} {firstname} {patr}") and self.validate_phone(phone) and self.valid_mail(mail)):

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
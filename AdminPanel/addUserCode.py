import sys
import sqlite3
from itertools import count
from pathlib import Path

from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QMessageBox
from  PyQt6 import uic
root_dir = Path(__file__).parent.parent
conn = sqlite3.connect(str(root_dir / 'hotel.db'))
c = conn.cursor()

class addUserCode(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('adduserwin.ui', self)
        self.adduser.clicked.connect(self.on_add_clicked)
    def on_add_clicked(self):
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


            count = 0
            for i in (lastname, firstname, patr,login, password, roomnum, contract, phone, mail):
                if not i:
                    count += 1
            if count>=1:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
            else:
                c.execute(f'''Insert into user(lastname, firstname,patronymic,user_login, user_password,room_num,contract,phone,mail)
                            Values (?,?,?,?,?,?,?,?,?)''', (lastname, firstname, patr,login, password, roomnum, contract, phone, mail))
                conn.commit()
                conn.close()
                self.close()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = addUserCode()
    window.show()
    sys.exit(app.exec())
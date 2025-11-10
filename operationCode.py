import sqlite3
from datetime import date

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic

class addoperation(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addoperation.ui', self)
        self.setWindowTitle("Добавление транзакций")
        self.addbtn.clicked.connect(self.on_add_clicked)
    def on_add_clicked(self):
        try:
            conn = sqlite3.connect('hotel.db')
            c = conn.cursor()

            contract = self.ntrcontract.text()
            summa = self.ntrsum.text()
            comment = self.ntrcomm.text()
            if not contract or not summa or not comment:
                QMessageBox.warning(self, "Ошибка", "Введите все поля")

            c.execute('''INSERT INTO operations(contract,summa,oper_text,oper_date) VALUES(?,?,?,?)''',(contract,summa,comment,str(date.today())))
            conn.commit()
            conn.close()
            self.close()
        except Exception as e:
            print(e)



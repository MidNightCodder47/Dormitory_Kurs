import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets,uic
from PyQt6.QtWidgets import QMessageBox, QDialog


class chngsumma(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('chngsumma.ui', self)
        self.setWindowTitle("Изменение счета проживающего")
        self.chngbtn.clicked.connect(self.on_btn_clicked)
    def on_btn_clicked(self):
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()
        try:
            contr = self.ntrcontract.text().strip()
            summa = self.ntrsum.text().strip()

            if not contr or not summa:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")

            c.execute('''Update finance set user_balance = ? where contract = ?''', (summa, contr))
            conn.commit()
            conn.close()
            self.close()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Проверьте вводимые данные")
        except Exception as e:
            print("chngsummacode")
            print(e)

import sqlite3
import sys
from datetime import date

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QLabel


from applicationUi import Ui_Dialog


conn = sqlite3.connect('hotel.db')
c = conn.cursor()


class Application(Ui_Dialog):
    def __init__(self,user_id,mainwin=None):
        super().__init__()
        self.main_window = mainwin
        self.user_id = user_id
        self.setupUi(self)
        self.button_send.clicked.connect(self.on_send_clicked)

    def on_send_clicked(self):
        try:

            title_ap = self.title_input.text()
            text_ap = self.text_input.toPlainText()


            if not text_ap or not title_ap:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
                return

            c.execute('''INSERT INTO application (app_title,app_text, user_id,app_date) VALUES (?,?,?,?)''',(title_ap,text_ap,self.user_id, str(date.today())))
            conn.commit()
            self.main_window.upd_applications()
            self.close()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application(1)
    window.setWindowTitle("Application")
    window.show()
    sys.exit(app.exec())
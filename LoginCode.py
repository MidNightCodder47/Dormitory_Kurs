import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMessageBox

import MainWindowCode
from LoginUI import Ui_MainWindow

conn = sqlite3.connect('hotel.db')
c = conn.cursor()


class Login(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.current_id = None

        self.logIn_btn.clicked.connect(self.on_login_clicked)

    def open_home_page(self,user_id):
        self.main_window = MainWindowCode.MainUserWindow(user_id)
        self.main_window.show()
        self.close()

    def on_login_clicked(self):
        login = self.login_widget.text()
        password = self.password_widget.text()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")

        c.execute(f'''SELECT id_user FROM user 
            WHERE user_login = ? AND user_password = ? ''', (login, password))

        result = c.fetchone()

        if result:
            self.current_user_id = result[0]
            self.open_home_page(self.current_user_id)

        else:
            QMessageBox.warning(self, "Ошибка", "Проверьте данные")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QMessageBox QLabel {
            color: black;
        }
        QMessageBox {
            background-color: white;
        }
        QMessageBox QPushButton {
            color: black;
        }
    """)

    window = Login()
    window.setWindowTitle("Login page")
    window.show()
    sys.exit(app.exec())


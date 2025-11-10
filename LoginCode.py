import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QLineEdit
from PyQt6 import uic
import MainWindowCode
import adminCode


conn = sqlite3.connect('hotel.db')
c = conn.cursor()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            uic.loadUi('Login.ui',self)
            self.setWindowTitle("Личный кабинет")
            self.current_id = None
            self.logIn_btn.clicked.connect(self.on_login_clicked)
            self.checkBox.toggled.connect(self.toggle_login_password_visibility)
        except Exception as e:
            print(e)
    def toggle_login_password_visibility(self, checked):
        try:
            if checked:
                self.password_widget.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.password_widget.setEchoMode(QLineEdit.EchoMode.Password)
        except Exception as e:
            print(e)
    def open_home_page(self,user_id):
        self.main_window = MainWindowCode.MainUserWindow(user_id)
        self.main_window.show()
        self.close()

    def on_login_clicked(self):
        try:
            login = self.login_widget.text()
            password = self.password_widget.text()

            if not login or not password:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
            if login == "admin" or password == "adm123":
                self.admin_window = adminCode.Admin()
                self.admin_window.show()
                self.close()
            else:
                c.execute(f'''SELECT id_user FROM user 
                    WHERE user_login = ? AND user_password = ? ''', (login, password))

                result = c.fetchone()

                if result:
                    self.current_user_id = result[0]
                    self.open_home_page(self.current_user_id)

                else:
                    QMessageBox.warning(self, "Ошибка", "Проверьте данные")
        except Exception as e:
            print(e)

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
    window.setWindowTitle("Авторизация")
    window.show()
    sys.exit(app.exec())


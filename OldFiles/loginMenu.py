import sys
import sqlite3

from PyQt6 import QtCore,QtWidgets


from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QHBoxLayout, QVBoxLayout,QLabel, QLineEdit, QPushButton, QMessageBox

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

import MainWindowCode
import MainWindowV2

conn = sqlite3.connect('../hotel.db')
c = conn.cursor()

class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(700, 500)
        self.current_id = None


        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addStretch()

        center_layout = QHBoxLayout()
        center_layout.addStretch()

        form_layout = QVBoxLayout()
        # элементы добавляются сюда

        center_layout.addLayout(form_layout)
        center_layout.addStretch()


        main_layout.addLayout(center_layout)
        main_layout.addStretch()

        welcome_label = ClickLabel('ТЕСТ')
        welcome_label.clicked.connect(lambda: welcome_label.setText("OK"))
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        form_layout.addWidget(welcome_label)

        # Добавляем отступ
        form_layout.addSpacing(30)

        # Поле для логина
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Введите логин")
        self.login_input.setFixedSize(200,40)

        form_layout.addWidget(QLabel("Логин:"))
        form_layout.addWidget(self.login_input)

        # Поле для пароля
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setFixedSize(200,40)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Скрываем пароль
        form_layout.addWidget(QLabel("Пароль:"))
        form_layout.addWidget(self.password_input)

        # Добавляем отступ
        form_layout.addSpacing(20)

        # Кнопка входа
        login_button = QPushButton("Войти")
        login_button.setFixedSize(200,40)
        login_button.clicked.connect(self.on_login_clicked)
        form_layout.addWidget(login_button)

        # Добавляем растягивающийся элемент для центрирования
        form_layout.addStretch()

    def open_home_page(self,user_id):
        self.main_window = MainWindowCode.MainUserWindow(user_id)
        self.main_window.show()
        self.close()

    def on_login_clicked(self):
        """Обработчик нажатия кнопки Войти"""
        login = self.login_input.text()
        password = self.password_input.text()


        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")

        c.execute(f'''SELECT id_user FROM user 
            WHERE user_login = ? AND user_password = ? ''', (login, password))

        result = c.fetchone()


        if result:
            self.current_user_id = result[0]
            # QMessageBox.warning(self, "Успех", f"Добро пожаловать, {login}!")
            self.open_home_page(self.current_user_id)

        else:

            QMessageBox.warning(self, "Ошибка", "Проверьте данные")
            return


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
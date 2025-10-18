# import sys
# import sqlite3
# from PyQt6.QtWidgets import QTabWidget, QLabel, QWidget, QPushButton, QScrollArea, QApplication, QDialog, QFrame, \
#     QVBoxLayout
# from PyQt6.QtCore import QRect,QMetaObject
# from PyQt6.QtGui import QFont,QTextFrame
#
#
# class MainWindow(QDialog):
#     def __init__(self,user_id):
#         super().__init__()
#         screen_geometry = QApplication.primaryScreen().geometry()
#         self.setFixedSize(screen_geometry.width(),screen_geometry.height())
#
#         self.setStyleSheet("background-color: #fffff;")
#
#         self.user_id = user_id
#         self.load_user_data()
#         self.setupUi(self)
#
#     def load_user_data(self):
#         self.conn = sqlite3.connect('../hotel.db')
#         self.c = self.conn.cursor()
#         self.c.execute("SELECT firstname,lastname,patronymic,room_num,contract,phone FROM user WHERE id_user = ?",(self.user_id,))
#         result = self.c.fetchone()
#
#         self.user_firstname = result[0]
#         self.user_lastname = result[1]
#         self.user_patronymic = result[2]
#         self.user_room_num = result[3]
#         self.user_contract = result[4]
#         self.user_phone = result[5]
#
#         self.c.execute("select user_balance from finance where contract = ?",(self.user_contract,))
#         result = self.c.fetchone()
#         self.user_balance = result[0]
#
#     def setupUi(self, Dialog):
#
#         Dialog.setObjectName(u"Dialog")
#
#         # Создание фиджета вкладок
#         self.tabWidget = QTabWidget(Dialog)
#         screen_geometry = QApplication.primaryScreen().geometry()
#         self.tabWidget.setGeometry(QRect(0, 100, screen_geometry.width(), screen_geometry.height()))
#
#         #Разметка контейнера профиля
#         self.Profile = QWidget()
#
#         self.label_5 = QLabel(self.Profile)
#         self.label_5.setText("Профиль")
#         self.label_5.setGeometry(QRect(15, 10, 101, 31))
#
#
#
#         self.label = QLabel(self.Profile)
#         self.label.setGeometry(QRect(15, 10, 400, 25))
#         self.label.setText(f"ФИО: {self.user_lastname}  {self.user_firstname}  {self.user_patronymic}")
#         self.label.setFont(QFont("Trebuchet MS", 14))
#
#
#
#         self.label_2 = QLabel(self.Profile)
#         self.label_2.setGeometry(QRect(15, 45, 200, 25))
#         self.label_2.setText(f"Номер Комнаты: {self.user_room_num}")
#         self.label_2.setFont(QFont("Trebuchet MS", 14))
#
#         self.label_3 = QLabel(self.Profile)
#         self.label_3.setGeometry(QRect(15, 80, 400, 25))
#         self.label_3.setText(f"Номер договора: {self.user_contract}")
#         self.label_3.setFont(QFont("Trebuchet MS", 14))
#
#
#         self.label_4 = QLabel(self.Profile)
#         self.label_4.setGeometry(QRect(15, 115, 400, 31))
#         self.label_4.setText(f"Номер телефона: {self.user_phone}")
#         self.label_4.setFont(QFont("Trebuchet MS", 14))
#
#
#
#         self.tabWidget.addTab(self.Profile, "Профиль")
#         self.tabWidget.setStyleSheet("background-color: #1e1e1e;")
#
#         self.tab_2 = QWidget()
#         self.tab_2.setObjectName(u"tab_2")
#
#
#         self.label_9 = QLabel(self.tab_2)
#         self.label_9.setGeometry(QRect(15, 15, 400, 25))
#         self.label_9.setText(f"Текущая сумма счета: {self.user_balance}")
#         self.label_9.setFont(QFont("Trebuchet MS", 14))
#
#
#         self.label_10 = QLabel(self.tab_2)
#         self.label_10.setGeometry(QRect(15, 50, 400, 50))
#         self.label_10.setText('''Реквизиты
#          10010100 123251 12423 (17)''')
#
#         self.label_11 = QLabel(self.tab_2)
#         self.label_11.setGeometry(QRect(15, 110, 400, 25))
#         self.label_11.setText(f"Стоимость в месяц: price")
#
#         self.label_12 = QLabel(self.tab_2)
#         self.label_12.setObjectName(u"label_12")
#         self.label_12.setGeometry(QRect(80, 360, 111, 16))
#
#
#         self.tabWidget.addTab(self.tab_2, "Финансы")
#
#
#         self.tab_3 = QWidget()
#         self.tab_3.setObjectName(u"tab_3")
#
#         self.pushButton = QPushButton(self.tab_3)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(30, 30, 161, 31))
#
#
#         self.scrollArea = QScrollArea(self.tab_3)
#         self.scrollArea.setObjectName("scrollArea")
#         self.scrollArea.setGeometry(QRect(20, 100, 820, 420))
#         # self.scrollArea.setLayoutDirection(Qt.LayoutDirection.)
#         self.scrollArea.setWidgetResizable(True)
#         self.scrollAreaWidgetContents = QWidget()
#         self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
#         self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 118, 78))
#         self.scrollArea.setWidget(self.scrollAreaWidgetContents)
#
#         self.tabWidget.addTab(self.tab_3, "Заявления")
#         self.tab_4 = QWidget()
#         self.tabWidget.addTab(self.tab_4, "Новости")
#         self.tabWidget.setCurrentIndex(0)
#
#         QMetaObject.connectSlotsByName(Dialog)
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#
#     window = MainWindow(1)
#     window.show()
#     sys.exit(app.exec())


import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class UserProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Профиль пользователя')
        self.setFixedSize(600, 500)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)

        # Заголовок
        title_label = QLabel("Добро пожаловать")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # ФИО
        fio_frame = QFrame()
        fio_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        fio_layout = QVBoxLayout(fio_frame)

        fio_label = QLabel("ФИО:")
        fio_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        fio_layout.addWidget(fio_label)

        # Поля для ФИО в одну строку
        name_layout = QHBoxLayout()

        # Фамилия
        lastname_layout = QVBoxLayout()
        lastname_label = QLabel("Фамилия:")
        lastname_label.setFont(QFont("Arial", 10))
        self.lastname_value = QLabel("Иванов")
        self.lastname_value.setFrameStyle(QFrame.Shape.Box)
        self.lastname_value.setMinimumHeight(25)
        lastname_layout.addWidget(lastname_label)
        lastname_layout.addWidget(self.lastname_value)

        # Имя
        firstname_layout = QVBoxLayout()
        firstname_label = QLabel("Имя:")
        firstname_label.setFont(QFont("Arial", 10))
        self.firstname_value = QLabel("Иван")
        self.firstname_value.setFrameStyle(QFrame.Shape.Box)
        self.firstname_value.setMinimumHeight(25)
        firstname_layout.addWidget(firstname_label)
        firstname_layout.addWidget(self.firstname_value)

        # Отчество
        patronymic_layout = QVBoxLayout()
        patronymic_label = QLabel("Отчество:")
        patronymic_label.setFont(QFont("Arial", 10))
        self.patronymic_value = QLabel("Иванович")
        self.patronymic_value.setFrameStyle(QFrame.Shape.Box)
        self.patronymic_value.setMinimumHeight(25)
        patronymic_layout.addWidget(patronymic_label)
        patronymic_layout.addWidget(self.patronymic_value)

        name_layout.addLayout(lastname_layout)
        name_layout.addLayout(firstname_layout)
        name_layout.addLayout(patronymic_layout)

        fio_layout.addLayout(name_layout)
        main_layout.addWidget(fio_frame)

        # Разделитель
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(line)

        # Секция "Данные"
        data_label = QLabel("Данные")
        data_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        main_layout.addWidget(data_label)

        # Поля данных
        data_widget = QWidget()
        data_form_layout = QVBoxLayout(data_widget)
        data_form_layout.setSpacing(10)

        # ID пользователя
        id_layout = self.create_info_row("ID:", "12345")

        # Логин
        login_layout = self.create_info_row("Логин:", "ivanov_i")

        # Пароль (скрытый)
        password_layout = self.create_info_row("Пароль:", "••••••••")

        # Почта
        mail_layout = self.create_info_row("Почта:", "ivanov@example.com")

        # Телефон
        phone_layout = self.create_info_row("Телефон:", "+7 (123) 456-78-90")

        # Договор
        contract_layout = self.create_info_row("Договор:", "Д-2024-001")

        data_form_layout.addLayout(id_layout)
        data_form_layout.addLayout(login_layout)
        data_form_layout.addLayout(password_layout)
        data_form_layout.addLayout(mail_layout)
        data_form_layout.addLayout(phone_layout)
        data_form_layout.addLayout(contract_layout)

        main_layout.addWidget(data_widget)

        # Разделитель
        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)
        line2.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(line2)

        # Информация о комнате
        room_label = QLabel("Информация о комнате")
        room_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        main_layout.addWidget(room_label)

        room_widget = QWidget()
        room_layout = QVBoxLayout(room_widget)
        room_layout.setSpacing(10)

        # Номер комнаты
        room_num_layout = self.create_info_row("Номер комнаты:", "101")

        # Соседи
        neighbors_layout = QVBoxLayout()
        neighbors_label = QLabel("Соседи:")
        neighbors_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.neighbors_value = QLabel("Петров Петр\nСидоров Алексей")
        self.neighbors_value.setFrameStyle(QFrame.Shape.Box)
        self.neighbors_value.setMinimumHeight(60)
        self.neighbors_value.setWordWrap(True)
        neighbors_layout.addWidget(neighbors_label)
        neighbors_layout.addWidget(self.neighbors_value)

        room_layout.addLayout(room_num_layout)
        room_layout.addLayout(neighbors_layout)

        main_layout.addWidget(room_widget)

        # Добавляем растягивающийся элемент в конец
        main_layout.addStretch()

    def create_info_row(self, label_text, value_text):
        """Создает строку с меткой и значением"""
        layout = QHBoxLayout()

        label = QLabel(label_text)
        label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        label.setFixedWidth(100)

        value = QLabel(value_text)
        value.setFrameStyle(QFrame.Shape.Box)
        value.setMinimumHeight(25)
        value.setStyleSheet("background-color: white;")

        layout.addWidget(label)
        layout.addWidget(value)
        layout.setStretchFactor(label, 1)
        layout.setStretchFactor(value, 3)

        return layout

    def set_user_data(self, user_data):
        """Установка данных пользователя"""
        self.lastname_value.setText(user_data.get('lastname', ''))
        self.firstname_value.setText(user_data.get('firstname', ''))
        self.patronymic_value.setText(user_data.get('patronymic', ''))

        # Находим виджеты значений по их тексту метки
        for i in range(self.centralWidget().layout().count()):
            widget = self.centralWidget().layout().itemAt(i).widget()
            if isinstance(widget, QWidget):
                self.update_widget_values(widget, user_data)

    def update_widget_values(self, widget, user_data):
        """Рекурсивно обновляет значения в виджетах"""
        layout = widget.layout()
        if layout:
            for i in range(layout.count()):
                item = layout.itemAt(i)
                if item.layout():
                    self.update_layout_values(item.layout(), user_data)
                elif item.widget():
                    self.update_widget_values(item.widget(), user_data)

    def update_layout_values(self, layout, user_data):
        """Обновляет значения в layout"""
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QHBoxLayout) or isinstance(item, QVBoxLayout):
                self.update_layout_values(item, user_data)
            elif item.widget() and isinstance(item.widget(), QLabel):
                label = item.widget()
                # Если это значение (а не метка), обновляем его
                if label.frameStyle() == QFrame.Shape.Box:
                    # Определяем какое это поле по предыдущей метке
                    prev_index = i - 1
                    if prev_index >= 0:
                        prev_item = layout.itemAt(prev_index)
                        if prev_item and prev_item.widget():
                            field_name = self.get_field_name(prev_item.widget().text())
                            if field_name in user_data:
                                label.setText(user_data[field_name])

    def get_field_name(self, label_text):
        """Преобразует текст метки в имя поля"""
        mapping = {
            "ID:": "id_user",
            "Логин:": "user_login",
            "Пароль:": "user_password",
            "Фамилия:": "lastname",
            "Имя:": "firstname",
            "Отчество:": "patronymic",
            "Почта:": "mail",
            "Телефон:": "phone",
            "Договор:": "contract",
            "Номер комнаты:": "room_num"
        }
        return mapping.get(label_text.strip(), "")


def main():
    app = QApplication(sys.argv)

    window = UserProfileWindow()

    # Пример данных пользователя
    user_data = {
        'id_user': '12345',
        'user_login': 'ivanov_i',
        'user_password': '••••••••',
        'firstname': 'Иван',
        'lastname': 'Иванов',
        'patronymic': 'Иванович',
        'room_num': '101',
        'contract': 'Д-2024-001',
        'phone': '+7 (123) 456-78-90',
        'mail': 'ivanov@example.com'
    }

    window.set_user_data(user_data)
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
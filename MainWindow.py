import sys
import sqlite3
from PyQt6.QtWidgets import QTabWidget, QLabel, QWidget, QPushButton, QScrollArea, QApplication, QDialog, QFrame, \
    QVBoxLayout
from PyQt6.QtCore import QRect,QMetaObject
from PyQt6.QtGui import QFont,QTextFrame


class MainWindow(QDialog):
    def __init__(self,user_id):
        super().__init__()
        screen_geometry = QApplication.primaryScreen().geometry()
        self.setFixedSize(screen_geometry.width(),screen_geometry.height())

        self.setStyleSheet("background-color: #fffff;")

        self.user_id = user_id
        self.load_user_data()
        self.setupUi(self)

    def load_user_data(self):
        self.conn = sqlite3.connect('hotel.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT firstname,lastname,patronymic,room_num,contract,phone FROM user WHERE id_user = ?",(self.user_id,))
        result = self.c.fetchone()

        self.user_firstname = result[0]
        self.user_lastname = result[1]
        self.user_patronymic = result[2]
        self.user_room_num = result[3]
        self.user_contract = result[4]
        self.user_phone = result[5]

        self.c.execute("select user_balance from finance where contract = ?",(self.user_contract,))
        result = self.c.fetchone()
        self.user_balance = result[0]

    def setupUi(self, Dialog):

        Dialog.setObjectName(u"Dialog")

        # Создание фиджета вкладок
        self.tabWidget = QTabWidget(Dialog)
        screen_geometry = QApplication.primaryScreen().geometry()
        self.tabWidget.setGeometry(QRect(0, 100, screen_geometry.width(), screen_geometry.height()))

        #Разметка контейнера профиля
        self.Profile = QWidget()

        self.label_5 = QLabel(self.Profile)
        self.label_5.setText("Профиль")
        self.label_5.setGeometry(QRect(15, 10, 101, 31))



        self.label = QLabel(self.Profile)
        self.label.setGeometry(QRect(15, 10, 400, 25))
        self.label.setText(f"ФИО: {self.user_lastname}  {self.user_firstname}  {self.user_patronymic}")
        self.label.setFont(QFont("Trebuchet MS", 14))



        self.label_2 = QLabel(self.Profile)
        self.label_2.setGeometry(QRect(15, 45, 200, 25))
        self.label_2.setText(f"Номер Комнаты: {self.user_room_num}")
        self.label_2.setFont(QFont("Trebuchet MS", 14))

        self.label_3 = QLabel(self.Profile)
        self.label_3.setGeometry(QRect(15, 80, 400, 25))
        self.label_3.setText(f"Номер договора: {self.user_contract}")
        self.label_3.setFont(QFont("Trebuchet MS", 14))


        self.label_4 = QLabel(self.Profile)
        self.label_4.setGeometry(QRect(15, 115, 400, 31))
        self.label_4.setText(f"Номер телефона: {self.user_phone}")
        self.label_4.setFont(QFont("Trebuchet MS", 14))

       

        self.tabWidget.addTab(self.Profile, "Профиль")
        self.tabWidget.setStyleSheet("background-color: #1e1e1e;")

        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")


        self.label_9 = QLabel(self.tab_2)
        self.label_9.setGeometry(QRect(15, 15, 400, 25))
        self.label_9.setText(f"Текущая сумма счета: {self.user_balance}")
        self.label_9.setFont(QFont("Trebuchet MS", 14))


        self.label_10 = QLabel(self.tab_2)
        self.label_10.setGeometry(QRect(15, 50, 400, 50))
        self.label_10.setText('''Реквизиты 
         10010100 123251 12423 (17)''')

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setGeometry(QRect(15, 110, 400, 25))
        self.label_11.setText(f"Стоимость в месяц: price")

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 360, 111, 16))


        self.tabWidget.addTab(self.tab_2, "Финансы")


        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")

        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 30, 161, 31))


        self.scrollArea = QScrollArea(self.tab_3)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(20, 100, 820, 420))
        # self.scrollArea.setLayoutDirection(Qt.LayoutDirection.)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 118, 78))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.tabWidget.addTab(self.tab_3, "Заявления")
        self.tab_4 = QWidget()
        self.tabWidget.addTab(self.tab_4, "Новости")
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow(1)
    window.show()
    sys.exit(app.exec())
import sys
import sqlite3
from PyQt6.QtWidgets import QTabWidget, QLabel, QWidget, QPushButton, QScrollArea, QApplication, QDialog
from PyQt6.QtCore import QRect,QMetaObject
from PyQt6.QtGui import QFont





class MainWindow(QDialog):
    def __init__(self,user_id):
        super().__init__()
        self.setFixedSize(700, 500)
        self.setStyleSheet("background-color: #fffff;")

        self.user_id = user_id
        self.load_user_data()
        self.setupUi(self)

    def load_user_data(self):
        self.conn = sqlite3.connect('hotel.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT firstname,lastname,patronymic,room_num,phone FROM user WHERE id_user = ?",(self.user_id,))
        result = self.c.fetchone()

        self.user_firstname = result[0]
        self.user_lastname = result[1]
        self.user_patronymic = result[2]
        self.user_room_num = result[3]
        self.user_phone = result[4]

    def setupUi(self, Dialog):

        Dialog.setObjectName(u"Dialog")
        Dialog.resize(860, 540)
        # Создание фиджета вкладок
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 860, 540))


        #Разметка контейнера профиля
        self.Profile = QWidget()

        self.label = QLabel(self.Profile)
        self.label.setGeometry(QRect(15, 10, 400, 25))
        self.label.setText(f"ФИО: {self.user_lastname}  {self.user_firstname}  {self.user_patronymic}")
        self.label.setFont(QFont("Trebuchet MS", 14))

        self.label_2 = QLabel(self.Profile)
        self.label_2.setGeometry(QRect(50, 260, 49, 16))
        self.label_2.setText(f"Номер Комнаты: {self.user_room_num}")

        self.label_3 = QLabel(self.Profile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 200, 111, 16))
        self.label_3.setText("Привет")


        self.label_4 = QLabel(self.Profile)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 101, 31))
        self.label_5 = QLabel(self.Profile)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 70, 101, 31))
        self.label_6 = QLabel(self.Profile)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 30, 101, 31))
        self.label_7 = QLabel(self.Profile)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 130, 101, 31))
        self.label_8 = QLabel(self.Profile)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 330, 101, 31))

        self.tabWidget.addTab(self.Profile, "Профиль")
        self.tabWidget.setStyleSheet("background-color: #1e1e1e;")

        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")


        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 190, 49, 16))
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 70, 111, 16))
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, 280, 111, 16))
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
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "Новости")



        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow(1)
    window.show()
    sys.exit(app.exec())
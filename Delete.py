import PyQt6
import sys
import sqlite3

from PyQt6.QtWidgets import QMainWindow, QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class HomeWindow(QMainWindow):
    def __init__(self,user_id):
        super().__init__()
        self.setWindowTitle("Главный экран")
        self.setFixedSize(700, 500)

        self.user_id = user_id
        self.load_user_data()
        self.init_ui()

    def load_user_data(self):
        self.conn = sqlite3.connect('hotel.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT firstname,lastname FROM user WHERE id_user = ?",(self.user_id,))
        result = self.c.fetchone()

        self.user_firstname = result[0]
        self.user_lastname = result[1]

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)



        layout = QVBoxLayout(central_widget)

        name_label = QLabel(f"Добро пожаловать, {getattr(self,'user_firstname')} {getattr(self,'user_lastname')} ")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(name_label)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec())


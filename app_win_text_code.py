import sys
from app_win_text_UI import Ui_Dialog
import sqlite3
connect = sqlite3.connect('hotel.db')
c = connect.cursor()

class win_text(Ui_Dialog):
    def __init__(self,app_id):
        super().__init__()
        self.setupUi(self)
        self.app_id = app_id
        self.load_data(app_id)

    def load_data(self,app_id):
        self.app_id = app_id
        c.execute('''SELECT * FROM application WHERE app_id = ?''',(self.app_id,))

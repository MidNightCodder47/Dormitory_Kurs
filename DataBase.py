import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS user')
c.execute('DROP TABLE IF EXISTS finance')#Для тестов После удалить
c.execute('PRAGMA foreign_keys = ON')
c.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id_user Integer PRIMARY KEY AUTOINCREMENT,
        user_login varchar(20) unique NOT NULL,
        user_password varchar(20) NOT NULL,
        firstname varchar(20) NOT NULL,
        lastname varchar(20) NOT NULL,
        patronymic varchar(20) default '',
        room_num varchar(7) NOT NULL,
        contract varchar(20) unique,
        phone varchar(15) unique,
        mail varchar(40));
        ''')
c.execute('''
    CREATE TABLE IF NOT EXISTS  finance (
        id_bill integer PRIMARY KEY AUTOINCREMENT,
        user_balance integer default 0,
        contract varchar(20) unique,
        month_price integer default 0 not null,
        FOREIGN KEY (contract) REFERENCES user (contract))''')
conn.commit()


c.execute('''INSERT INTO user (user_login, user_password, firstname, lastname,patronymic,room_num,contract,mail) 
          VALUES ('123', '123', 'Petr','Ivanov','Olegovich', '101A','AB001','example@mail.com'),
                ('1234', '1234', 'Vanya','Ptichkin','', '102A','AB002','example2@mail.com')''')


c.execute("Insert Into finance (contract,user_balance) Values ('AB001',100)")
conn.commit()

print("Data inserted successfully.")



c.execute("SELECT * FROM finance")
rows = c.fetchall()
for row in rows:
    print(f"{row[0]}, {row[1]}, {row[2]}")


c.close()
import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS user') #Для тестов После удалить

c.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id_user Integer PRIMARY KEY AUTOINCREMENT,
        user_login varchar(20) unique NOT NULL,
        user_password varchar(20) NOT NULL,
        firstname varchar(20) NOT NULL,
        lastname varchar(20) NOT NULL,
        patronymic varchar(20),
        room_num varchar(7) NOT NULL,
        contract varchar(20) unique,
        phone varchar(15) unique)
        ''')

c.execute("INSERT INTO user (user_login, user_password, firstname, lastname,room_num,contract) VALUES ('123', '123', 'Ivan','Ivanov', '101A','AB001')")
conn.commit()
print("Data inserted successfully.")

c.execute("SELECT * FROM user")

# Fetch all records
rows = c.fetchall()

print("All Food Items:\n")
for row in rows:
    print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[6]}, {row[7]}")

c.close()
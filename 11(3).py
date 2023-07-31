import sqlite3

try:#подключение к базе данных
    connection = sqlite3.connect('data.bd')
    cursor = connection.cursor()#для работы с объектами
except sqlite3.DatabaseError:
    print('Ошибка')
finally:
    connection.close()

class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

def get_users_list(cursor):
    command = '''
    SELECT * FROM users
    '''
    result = cursor.execute(command)#позволяет выполнить запрос
    user = result.fetchall()
    print(user)#позволяет получить результат, вытащить из базы данных

def create_table_user(cursor):#рисуем таблицу
    command = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    gender TEXT);
    '''

    cursor.execute(command)

def add_user(cursor, user):
    command = '''
    INSERT INTO users (name,surname,gender) VALUES (?, ?, ?);
     '''
    cursor.execute(command, (user.name, user.surname, user.gender))

def get_user(cursor, user_id):
    command = '''
    SELECT * FROM users WHERE id = ?;
    '''
    result = cursor.execute(command, (user_id))
    user = result.fetchall()
    print(user)

def update_user_name(cursor, value, user_id):
    command = '''
    UPDATE users SET name = ? WHERE id = ?
    '''
    cursor.execute(command, (value, user_id))

def delete_user(cursor):
    command = '''
    DELETE FROM users
    '''
    cursor.execute(command)

def delete_user_id(cursor, user_id):
    command = '''
    DELETE FROM users WHERE id = ? '''
    cursor.execute(command, (user_id))

def users_gender(cursor,user_gender):
    command = '''
    SELECT * FROM users WHERE gender = ?'''
    result = cursor.execute(command,(user_gender,))
    user = result.fetchall()
    print(user)

if __name__ == '__main__':
    with sqlite3.connect('data.bd') as cursor:
        create_table_user(cursor)
        delete_user(cursor)
        add_user(cursor, User('Maxim','Ivanov','male'))
        add_user(cursor, User('Sveta', 'Semenova', 'female'))
        add_user(cursor, User('Sarah', 'Brown', 'female'))
        get_users_list(cursor)
        users_gender(cursor,'female')


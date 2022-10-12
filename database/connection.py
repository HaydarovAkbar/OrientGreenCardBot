import sqlite3
from datetime import datetime

db = "green_card.db"


class Database:
    def get_direction_if_univerid(self, university_id):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT * FROM direction WHERE university_id={university_id}')
        a = cursor.fetchall()
        connection.close()
        return a

    def get_all_userCOUNT(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT count(id) FROM users')
        a = cursor.fetchone()
        connection.close()
        return a



    def get_about_direction(self, direction_id):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT * FROM about_direction WHERE direction_id={direction_id}')
        a = cursor.fetchone()
        connection.close()
        return a

    def get_university_id(self, university_id):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT * FROM university WHERE id={university_id}')
        a = cursor.fetchone()
        connection.close()
        return a

    def get_direction_id(self, direction_id):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT * FROM direction WHERE id={direction_id}')
        a = cursor.fetchone()
        connection.close()
        return a

    def get_users(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        b = cursor.fetchall()
        connection.close()
        return b

    def get_user_allID(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT chat_id FROM users")
        b = cursor.fetchall()
        connection.close()
        return b

    def get_users_count(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT count(id) FROM users")
        b = cursor.fetchone()
        connection.close()
        return b

    def get_user_if_id(self, chat_id):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users where chat_id = {chat_id}")
        b = cursor.fetchone()
        connection.close()
        return b

    def insert_user(self, chatid, language, username):
        # try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        # sql = 'INSERT INTO users(chatid,first_name,last_name,oblast,region,phone_number,language,status,date_of_created,username) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # cursor.execute(sql, (chatid, first_name, last_name, oblast, region, phone_number, language,"", now, username))
        cursor.execute(
            f"INSERT INTO users(username,lang,chat_id,date_of_created) "
            f"VALUES('{username}','{language}', {chatid},'{now}')")
        connection.commit()
        connection.close()
        return True

    # except Exception as e:
    #     print(e)
    #     return False

    def insert_registration(self, first_name, last_name, birthday_date, information, green_passport, photo, phone_number):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = """INSERT INTO registration(first_name,last_name,birthday_date,information,green_passport,photo,phone_number) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (
            first_name, last_name, birthday_date, information, green_passport, photo, phone_number))
            # connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)
            return False

    def get_admin(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM admins")
        a = cursor.fetchall()
        connection.close()
        return a

    def get_if_id_admin(self, chat_id):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM admins where chat_id = {chat_id}")
        a = cursor.fetchone()
        connection.close()
        return a

    def add_admin(self, name, userID, username):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = 'INSERT INTO admins(name,userid,username) VALUES(%s,%s,%s)'
            cursor.execute(sql, (name, userID, username))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)

    def add_link(self, text, photo, link, user, date, name, category_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = 'INSERT INTO linklar(text,photo,link,user,date,name,category_id) VALUES(%s,%s,%s,%s,%s,%s,%s)'

            cursor.execute(sql, (text, photo, link, user, date, name, category_id))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_link(self, id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM linklar WHERE id={id}")
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    def update_lang(self, lang, id):
        """Bu funksiya orqali userni tilini yangilashi mumkin"""
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"UPDATE users SET lang='{lang}' WHERE chat_id = {id}")
            connection.commit()
        except Exception as e:
            print(f"Error -> {e}")
        # finally:
        #     connation.close()


if __name__ == '__main__':
    db_ = Database()
    db_.insert_user(123131, 'sada', 'asdas', '1', '2', '12313', 'uz', 'qwd')

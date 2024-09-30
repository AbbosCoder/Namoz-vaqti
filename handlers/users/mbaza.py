import sqlite3
import pandas as pd
from loader import dp,bot
# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Jadvalni yaratish
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        joylashuv TEXT DEFAULT '0'
    )
''')
conn.commit()

# Yangi foydalanuvchi qo'shish
def add_user(user_id, first_name, username):
    # Foydalanuvchi ma'lumotlarini tekshiramiz
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    existing_user = cursor.fetchone()
    if not existing_user:
        # Foydalanuvchi mavjud emas, ma'lumotlar bazasiga qo'shamiz
        cursor.execute('''
        INSERT INTO users (id, first_name, username)
        VALUES (?, ?, ?)
    ''', (user_id, first_name, username))
        conn.commit()
        return True
#umumiy foydalanuchilar
def users_count():
    # Execute a query to get the total number of users
    cursor.execute('SELECT COUNT(*) FROM users')
    # Fetch the result of the query
    total_users_count = cursor.fetchone()[0]
    return total_users_count    
    
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[1]  # Assuming the name is at index 1 in the result tuple
    else:
        return None
def get_username(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[2]  # Assuming the name is at index 1 in the result tuple
    else:
        return None
def get_joylashuv(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[3]  # Assuming the balance is at index 4 in the result tuple
    else:
        return None
# Foydalanuvchi ma'lumotlarini o'qish
# def get_user(user_id):
#     cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
#     return cursor.fetchone()[1]
# #balansi ko'rish
# def get_balance(user_id):
#     cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
#     return cursor.fetchone()[4]
#tel raqamni olish

# Raqamni yangilash
def update_location(user_id, joylashuv):
    try:
        # Foydalanuvchi ma'lumotlarini olish
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cursor.fetchone()

        if user:
            # Yangi telefon raqamini ma'lumotlar bazasiga yozish
            cursor.execute("UPDATE users SET joylashuv=? WHERE id=?", (joylashuv, user_id))
            conn.commit()
            return True  # Telefon raqami muvaffaqiyatli o'zgartirildi
        else:
            return False  # Foydalanuvchi bazada topilmadi
    except Exception as e:
        print(f"Xatolik: {e}")
        return False  # Xatolik sodir bo'ldi

    
def export_data_to_excel():
    excel_filename = 'users_data.xlsx'
    database_name = 'users.db'
    try:
        # Ma'lumotlar bazasiga ulanish
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Ma'lumotlarni olish
        cursor.execute("SELECT * FROM users")
        all_users = cursor.fetchall()

        # Ma'lumotlarni Pandas DataFrame ga o'zlashtirish
        columns = ['ID', 'First Name', 'Username', 'Language', 'Balance', 'Phone Number']
        df = pd.DataFrame(all_users, columns=columns)

        # DataFrame ni Exсel fayliga yozish
        df.to_excel(excel_filename, index=False)
        print(f"Ma'lumotlar Exсel fayliga yozildi: {excel_filename}")
        return excel_filename

    except Exception as e:
        print(f"Xatolik: {e}")



import sqlite3
from pprint import pprint

def initiate_db():
    SQL = '''
    CREATE TABLE IF NOT EXISTS Vines (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER,
    pic_fn TEXT);
    '''
    connection = sqlite3.connect('TG_bot_II.db')
    cursor = connection.cursor()
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS Vines (
    # id INTEGER PRIMARY KEY,
    # title TEXT NOT NULL,
    # description TEXT NOT NULL,
    # price INTEGER,
    # pic_fn TEXT);
    # ''')
    cursor.execute(SQL)
    connection.commit()
    connection.close()

def get_all_products():
    SQL = 'SELECT * FROM Vines'
    connection = sqlite3.connect('TG_bot_II.db')
    cursor = connection.cursor()
    cursor.execute(SQL)
    vines = cursor.fetchall()
    # for i in vines:
    #     pprint(i)
    connection.commit()
    connection.close()
    return vines

import sqlite3
from db_bot import sql_req

db= sqlite3.connect('expence_log.db')
cursor= db.cursor()

'''ДЛЯ ИНЛАЙН КЛАВИАТУРЫ С ВЫБОРОМ ГОДА'''
cursor.execute(sql_req.yearsselect)
years = tuple (i[0] for i in cursor.fetchall())
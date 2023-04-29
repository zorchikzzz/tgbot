import sqlite3
from db_bot import sql_req

db= sqlite3.connect('expence_log.db')
cursor= db.cursor()

'''ДЛЯ ИНЛАЙН КЛАВИАТУРЫ С ВЫБОРОМ ГОДА'''
cursor.execute(sql_req.yearsselect)
years = tuple (i[0] for i in cursor.fetchall())

"""ДЛЯ ИНЛАЙН КЛАВИАТУРЫ С ВЫБОРОМ КАТЕГОРИИ"""
def year_in_type(type,year):
    cursor.execute(f'{sql_req.stat_in_year[0]} "{type}"'
                   f'{sql_req.stat_in_year[1]} "{year}" {sql_req.stat_in_year[2]}')
    kategorys = cursor.fetchall()
    return kategorys
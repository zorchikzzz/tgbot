import sqlite3
from db_bot import sql_req

db = sqlite3.connect('expence_log.db')
cursor = db.cursor()

def get_day_statistic():
    cursor.execute(sql_req.rashodday)
    rashod = cursor.fetchone()[0]
    if not rashod: rashod = 0
    cursor.execute(sql_req.dohodday)
    dohod = cursor.fetchone()[0]
    if not dohod: dohod = 0
    balance = dohod - rashod

    return f'СЕГОДНЯ:\n' \
           f'<b>Доход {dohod} рублей \n' \
           f'Расход {rashod} рублей \n' \
           f'Баланс {balance} рублей</b>'
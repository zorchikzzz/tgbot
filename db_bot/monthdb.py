import sqlite3
from db_bot import sql_req


db= sqlite3.connect('expence_log.db')
cursor= db.cursor()

def get_monthInlineButtons(year):
    cursor.execute(f'{sql_req.monthselect} "{year}"')
    montbuttons = tuple(i[0] for i in cursor.fetchall())
    return montbuttons


def get_month_statistic(monthid):
    cursor.execute(sql_req.rashodmonth)
    rashod = cursor.fetchone()[0]
    if not rashod: rashod = 0
    cursor.execute(sql_req.dohodmonth)
    dohod = cursor.fetchone()[0]
    if not dohod: dohod = 0
    balance = dohod - rashod

    return f'<b>Доход {dohod} рублей \n' \
           f'Расход {rashod} рублей \n' \
           f'Баланс {balance} рублей</b>'

"""СТАТИСТИКА ЗА МЕСЯЦ ОБЩАЯ"""

def month_in_type(type, monthid, year):
    cursor.execute(f'{sql_req.stat_in_month[0]} "{type}" {sql_req.stat_in_month[1]} "{monthid}"'
                   f'{sql_req.stat_in_month[2]} "{year}" {sql_req.stat_in_month[3]}')
    kategorys = cursor.fetchall()
    return kategorys

'''СПИСОК РАСХОДОВ В КОНКРЕТНОЙ КАТЕГОРИИИ ЗА ВЫБРАННУЮ ДАТУ'''
def kategory_expances(kategory, monthid, year):
    cursor.execute(f'{sql_req.stat_in_kategory_in_month[0]} "{kategory}" {sql_req.stat_in_kategory_in_month[1]} "{monthid}"'
                   f'{sql_req.stat_in_kategory_in_month[2]} "{year}" {sql_req.stat_in_kategory_in_month[3]}')
    operations = '\n\n'.join([f'{i[0]} {str(i[1])} {i[2][:-3]}' for i in cursor.fetchall()])
    return operations

def summaoftype(type,monthid,year):
    cursor.execute(f'SELECT SUM(sum) FROM log WHERE type = "{type}" AND strftime("%m",date) = "{monthid}"'
                   f'AND strftime("%Y",date) = "{year}"')
    summa = cursor.fetchone()[0]
    return summa


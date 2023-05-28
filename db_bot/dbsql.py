import sqlite3
from db_bot import pars
from db_bot import sql_req

db= sqlite3.connect('expence_log.db')
cursor= db.cursor()

def add_operation(message,date):
    parsMessage = pars.parsingForAddOperation(message,date)
    if parsMessage == 'eror' :
        return 'eror'

    cursor.execute("INSERT INTO log('date','type', 'sum', 'kategory', 'coment', 'message')"
                   " VALUES (?, ?, ?, ?, ?, ? )",(parsMessage))
    db.commit()

def get_balance():
    rashod =(cursor.execute(sql_req.rashod).fetchone())[0]
    dohod =(cursor.execute(sql_req.dohod).fetchone())[0]
    return f"ТЕКУЩИЙ БАЛАНС: \n{str(dohod-rashod)} РУБЛЕЙ"


def kategorysinbase(type):
    cursor.execute(f'{sql_req.kategorys} "{type}" GROUP BY kategory ORDER BY sum(sum) DESC')
    kategorys = '\n'.join([i[0] for i in cursor.fetchall()])#.split()

    return f'<b>{kategorys}</b>'

def kategory_expances(kategory, year, monthid = 0 ):
    if monthid != 0:
        sql = f'AND strftime("%m",date)= "{monthid}" ORDER BY date '
    else:
        sql = f'ORDER BY date'

    cursor.execute(f'SELECT sum, coment, date FROM log WHERE kategory = '
                       f' "{kategory}" AND strftime("%Y",date)= "{year}"'
                       f'{sql} ')

    operations = '\n\n'.join([f'{i[0]} {str(i[1])} {i[2][:-3]}' for i in cursor.fetchall()])
    return operations



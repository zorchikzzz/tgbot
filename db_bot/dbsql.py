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
    cursor.execute(f'{sql_req.kategorys} "{type}"')
    kategorys = '\n'.join(sorted([i[0] for i in cursor.fetchall()]))
    return kategorys



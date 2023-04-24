from db_bot import sql_req
import sqlite3

db= sqlite3.connect('expence_log.db')
cursor= db.cursor()

def getlast10 (deleteMod=False):
    cursor.execute(sql_req.getlast10)
    if deleteMod:
        return [(f'{i[0]} {str(i[1])} {i[2]} {i[3]} {i[4][:-3]} ', f'{i[5]}') for i in cursor.fetchall()]
    return '\n'.join([f'{i[0]} {str(i[1])} {i[2]} {i[3]} {i[4][:-3]}\n' for i in cursor.fetchall()])

def deleteEntry(id):
    cursor.execute('DELETE FROM log WHERE id == ?', (id,))
    db.commit()
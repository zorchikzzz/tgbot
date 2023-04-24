rashod = 'SELECT SUM(sum) FROM log WHERE type = "РАСХОД"'

dohod = 'SELECT SUM(sum) FROM log WHERE type = "ДОХОД"'

rashodmonth = 'SELECT SUM(sum) FROM log WHERE type = "РАСХОД" AND date >' \
              ' DATETIME("now","start of month")'

dohodmonth = 'SELECT SUM(sum) FROM log WHERE type = "ДОХОД" AND date >' \
             'DATETIME("now","start of month")'

rashodday = 'SELECT SUM(sum) FROM log WHERE type = "РАСХОД" AND date >=' \
              ' DATETIME("now")'

dohodday =  'SELECT SUM(sum) FROM log WHERE type = "ДОХОД" AND date >=' \
             'DATETIME("now")'

stat_in_month = ('SELECT kategory, sum(sum), date, coment FROM log WHERE type =', 'AND strftime("%m",date) =',
             'AND strftime("%Y",date)=', 'GROUP BY kategory')

getlast10 = '''SELECT type, sum , kategory, coment, date, id FROM log ORDER BY date DESC LIMIT 10'''

kategorys = ('SELECT DISTINCT kategory FROM log WHERE type =')

stat_in_kategory_in_month = ('SELECT sum, coment, date FROM log WHERE kategory =', 'AND strftime("%m",date) =',
             'AND strftime("%Y",date)=', 'ORDER BY date')
'''узнать колличество месяцев в выбранном году или колличество лет всего'''
yearsselect = 'SELECT DISTINCT strftime("%Y",date) FROM log'
monthselect = 'SELECT DISTINCT strftime("%m",date) FROM log WHERE strftime("%Y",date) ='
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db_bot import monthdb, yeardb

monthindex = ('ЯНВАРЬ', 'ФЕВРАЛЬ', 'МАРТ', 'АПРЕЛЬ', 'МАЙ',
              'ИЮНЬ', 'ИЮЛЬ', 'АВГУСТ', 'СЕНТЯБРЬ', 'ОКТЯБРЬ', 'НОЯБРЬ', 'ДЕКАБРЬ')

chooseMonth = InlineKeyboardButton("ВЫБРАТЬ  МЕСЯЦ", callback_data='chooseM')
chooseYear = InlineKeyboardButton("ВЫБРАТЬ ГОД", callback_data='chooseY')
showyearstatistic = InlineKeyboardButton('СТАТИСТИКА ЗА ГОД', callback_data='showyearstatistic')

# инлайн кнопки в разделе категории для просмотра категорий доходов
kategorys_in_income = InlineKeyboardButton("КАТЕГОРИ В РАЗДЕЛЕ ДОХОД", callback_data='incomekats')
kategorysIncome = InlineKeyboardMarkup().add(kategorys_in_income)

'''ИНЛАЙН КЛАВИАТУРА С МЕСЯЦАМИ'''


def replychooseMonthkb(year):
    chooseMonthKb = InlineKeyboardMarkup(row_width=3)
    for i in monthdb.get_monthInlineButtons(year):
        chooseMonthKb.insert(InlineKeyboardButton(f'{monthindex[int(i) - 1]}', callback_data=f'month_0{int(i)}'))
    chooseMonthKb.add(chooseYear).insert(showyearstatistic)
    return chooseMonthKb


"""ИНЛАЙН КЛАВИАТУРА С КАТЕГОРИЯМИ """


def reply_journalkb(type, monthid=00, year=2023, x=1):
    journalkb = InlineKeyboardMarkup(row_width=2)
    if monthid:
        period = monthdb.month_in_type(type, monthid, year)
        callback = 'ПОДРОБНЕЕМ'


    else:
        period = yeardb.year_in_type(type, year)
        callback = 'ПОДРОБНЕЕГ'

    for i in period:
        journalkb.insert(InlineKeyboardButton(f'{i[0]} {i[1]}', callback_data=f'{callback}{monthid}{year}{i[0]}'))
    journalkb.add(chooseMonth)

    if x == 1:  # x=0 только при переходе в меню доходов ( там не нужно добавлять эти кнопки)
        journalkb.add(InlineKeyboardButton("ПОСМОТРЕТЬ ДОХОДЫ", callback_data=f'viev_{monthid}{year}'))

    return journalkb



'''ИНЛАЙН КЛАВИАТУРА С ГОДАМИ'''
def replyYearKb():
    chooseYearKb = InlineKeyboardMarkup(row_width=4)
    for i in yeardb.years:
        chooseYearKb.insert(InlineKeyboardButton(f'{i}', callback_data= f'year_{i}'))
    return chooseYearKb
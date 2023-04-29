from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db_bot import yeardb

'''ИНЛАЙН КЛАВИАТУРА С ГОДАМИ'''
def replyYearKb():
    chooseYearKb = InlineKeyboardMarkup(row_width=4)
    for i in yeardb.years:
        chooseYearKb.insert(InlineKeyboardButton(f'{i}', callback_data= f'year_{i}'))
    return chooseYearKb


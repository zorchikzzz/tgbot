from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

'''Обычные кнопки'''
month = KeyboardButton('ЖУРНАЛ')
last10 = KeyboardButton('ПОСЛЕДНИЕ 10')
balance = KeyboardButton('БАЛАНС')
kategorys = KeyboardButton('КАТЕГОРИИ')

'''ЗАКРЕПЛЁННАЯ ВНИЗУ КЛАВИАТУРА'''

keyboardclient = ReplyKeyboardMarkup(resize_keyboard=True)
keyboardclient.add(month).insert(balance).add(last10).insert(kategorys)

'''Инлайн кнопки'''




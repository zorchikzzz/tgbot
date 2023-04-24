from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_bot.last10 import getlast10
deleteButton = InlineKeyboardMarkup().add(InlineKeyboardButton('РЕЖИМ УДАЛЕНИЯ', callback_data='deleteMod'))

def ReplyDeleteModKb ():
    deleteModKb = InlineKeyboardMarkup(row_width=1)
    for i in getlast10(deleteMod=True):
        deleteModKb.insert(InlineKeyboardButton(f'{i[0]}', callback_data=f"delete_{i[1]}"))
    return deleteModKb

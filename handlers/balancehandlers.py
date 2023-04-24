from aiogram import types, Dispatcher
from db_bot import dbsql, daydb


async def returnbalance(message: types.Message):
    await message.answer(dbsql.get_balance())
    await message.answer(daydb.get_day_statistic())

def registerbalancehandlers(dp: Dispatcher):
    dp.register_message_handler(returnbalance, text=['БАЛАНС'])

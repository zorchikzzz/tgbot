import os
from aiogram import types, Dispatcher
from aiogram.types import ContentTypes
from db_bot import dbsql
from keyboards import mainKb, journalKb



async def start(message: types.Message):
    await message.answer('КЛАВИАТУРА', reply_markup=mainKb.keyboardclient)


async def downloaddbonpc(messege: types.Message):
    if document := messege.document:
        await document.download(
            destination_file=r"expence_log.db")
        print('DATABASE UPDATED')
        await messege.answer('БАЗА ДАННЫХ УСПЕШНО ОБНОВЛЕНА')


async def addexpence(messege : types.Message):
    date = messege.date
    if dbsql.add_operation(messege, date) != 'eror':
        await messege.answer(f'Запись успешно добавлена в журнал: {messege.text}')

    else:
        await messege.answer('НЕКОРЕКТНЫЙ ВВОД')


async def returnkategorys(message: types.Message):
    await message.answer(dbsql.kategorysinbase('РАСХОД'), reply_markup=journalKb.kategorysIncome)


async def returnDohodkategorys(callback: types.CallbackQuery):
    await callback.message.answer(dbsql.kategorysinbase("ДОХОД"))
    await callback.answer()


async def switchoffcomputer(message: types.Message):
    #os.system("shutdown /s /t 1") windows edition
    os.system('echo pasword | sudo -S shutdown -P +1' )



async def dbinmessage(message: types.Message):
    await message.reply_document(open('expence_log.db', 'rb'))

def register_all(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(returnkategorys, text=['КАТЕГОРИИ'])
    dp.register_message_handler(switchoffcomputer, text='ВЫКЛЮЧИТЬ КОМПЬЮТЕР')
    dp.register_callback_query_handler(returnDohodkategorys, text='incomekats')
    dp.register_message_handler(downloaddbonpc, content_types=ContentTypes.DOCUMENT)
    dp.register_message_handler(dbinmessage, commands='backup')

    dp.register_message_handler(addexpence)

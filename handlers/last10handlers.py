from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db_bot import last10
from keyboards.last10Kb import deleteButton, ReplyDeleteModKb

messegeInDeleteMod = '<b>РЕЖИМ УДАЛЕНИЯ</b> \n(необходимо нажать на запись что-бы удалить её)'

async def returnlast10(messege: types.Message):
    await messege.answer(last10.getlast10(), reply_markup=deleteButton)

async def deletemodKb(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(messegeInDeleteMod, reply_markup = ReplyDeleteModKb())

async def initDeleteEntry(callback: types.CallbackQuery):
    last10.deleteEntry(callback.data[7:])
    await callback.message.answer('<b>РЕЖИМ УДАЛЕНИЯ</b> \n(необходимо нажать на запись что-бы '
                                  'удалить её)', reply_markup=ReplyDeleteModKb())
    await callback.answer("ЗАПИСЬ УДАЛЕНА", show_alert=True)



def register_last10(dp: Dispatcher):
    dp.register_message_handler(returnlast10, text='ПОСЛЕДНИЕ 10')
    dp.register_callback_query_handler(deletemodKb, text='deleteMod')
    dp.register_callback_query_handler(initDeleteEntry, Text(startswith='delete_'))

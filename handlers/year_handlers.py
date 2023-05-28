from aiogram import types, Dispatcher
from keyboards.journalKb import replychooseMonthkb, reply_journalkb, replyYearKb
from aiogram.dispatcher.filters import Text
from db_bot.dbsql import kategory_expances

year = '2023'

'''ВЫЗЫВАЕТСЯ НАЖАТИЕМ КНОПКИ ВЫБРАТЬ ГОД'''
async def chooseYear(callback: types.CallbackQuery):
    await callback.message.answer('ВЫБЕРЕТЕ ГОД', reply_markup=replyYearKb())
    await callback.answer()

'''ВЫЗЫВАЕТСЯ НАЖАТИЕМ КНОПКИ С ЧИСЛОМ ОТОБРАЖАЮЩИМ ГОД'''
async def selectedYearCallback(callback: types.CallbackQuery):
    global year
    year = callback.data[5:]
    await callback.message.answer(f"ВЫБЕРИТЕ МЕСЯЦ", reply_markup=replychooseMonthkb(year))
    await callback.answer()

'''ВЫЗЫВАЕТСЯ НАЖАТИЕМ КНОПКИ ВЫБРАТЬ МЕСЯЦ'''
async def chooseMonth(callback: types.CallbackQuery):
    await callback.message.answer('<b> НАЖМИТЕ НА ИНТЕРЕСУЮЩИЙ МЕСЯЦ</b>', reply_markup=replychooseMonthkb(year))
    await callback.answer()

"""ВЫЗЫВАЕТСЯ НАЖАТИЕМ КНОПКИ "СТАТИСТИКА ЗА ГОД" ИЗ МЕНЮ ЖУРНАЛА"""
async def showyearstatisic(callback: types.CallbackQuery):

    await callback.message.answer(f'СТАТИСТИКА ЗА {year} ГОД', reply_markup= reply_journalkb('РАСХОД',0, year))
    await callback.answer(year)

async def expListYear(callback: types.callback_query):
    print (callback.data)
    await callback.message.answer(kategory_expances(callback.data[15:], callback.data[11:15]))
    await callback.answer(callback.data[16:])


def register_year(dp: Dispatcher):
    dp.register_callback_query_handler(expListYear, Text(startswith='ПОДРОБНЕЕГ'))
    dp.register_callback_query_handler(chooseYear, text='chooseY')
    dp.register_callback_query_handler(chooseMonth, text='chooseM')
    dp.register_callback_query_handler(selectedYearCallback, Text(startswith='year_'))
    dp.register_callback_query_handler(showyearstatisic, text = 'showyearstatistic')


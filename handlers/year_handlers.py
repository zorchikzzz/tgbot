from aiogram import types, Dispatcher
from keyboards.journalKb import replychooseMonthkb, replyYearKb
from aiogram.dispatcher.filters import Text

year = '2023'
'''ВЫЗЫВАЕТСЯ НАЖАТИЕМ КНОПКИ ВЫБРАТЬ ГОД'''


async def chooseYear(callback: types.CallbackQuery):
    await callback.message.answer('ВЫБЕРЕТЕ ГОД', reply_markup=replyYearKb())
    await callback.answer()


'''ВЫЗЫВАЕТСЯ НАЖАТИЕМ КНОПКИ С ГОДОМ'''


async def selectedYearCallback(callback: types.CallbackQuery):
    global year
    year = callback.data[5:]
    await callback.message.answer(f"ВЫБЕРИТЕ МЕСЯЦ ЗА {year[5:]} ГОД", reply_markup=replychooseMonthkb(year))
    await callback.answer()


'''ВЫЗЫВАЕТСЯ НАЖАТИЕМ КНОПКИ ВЫБРАТЬ МЕСЯЦ'''


async def chooseMonth(callback: types.CallbackQuery):
    await callback.message.answer('<b> НАЖМИТЕ НА ИНТЕРЕСУЮЩИЙ МЕСЯЦ</b>', reply_markup=replychooseMonthkb(year))
    await callback.answer()


def register_year(dp: Dispatcher):
    dp.register_callback_query_handler(chooseYear, text='chooseY')
    dp.register_callback_query_handler(chooseMonth, text='chooseM')
    dp.register_callback_query_handler(selectedYearCallback, Text(startswith='year_'))

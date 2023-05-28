from aiogram import types, Dispatcher
from db_bot import monthdb
from db_bot.dbsql import kategory_expances
from keyboards.journalKb import reply_journalkb, showyearstatistic
from aiogram.dispatcher.filters import Text
from handlers import year_handlers



'''ХЭНДЛЕР РЕАГИРУЮЩИЙ НА КНОПКУ ЖУРНАЛ ИЗ ГЛАВНОГО МЕНЮ, В НЁМ УЗНАЁМ ТЕКУЩЕЕ ВРЕМЯ И ПЕРЕДАЁМ ЕГО В ФУНКЦИЮ КОТОРАЯ 
СОБЕРЁТ НАМ ИНЛАЙН КЛАВИАТУРУ'''
async def month_info(message: types.message):
    import time
    named_tuple = time.localtime()
    time_string = time.strftime("%m%Y", named_tuple)
    monthid = time_string[:2]
    year = time_string[2:]

    await message.answer("<b>РАСХОДЫ ЗА ТЕКУЩИЙ МЕСЯЦ</b>",
                         reply_markup=reply_journalkb("РАСХОД", monthid, year).insert(showyearstatistic))
    await message.answer(monthdb.get_month_statistic(monthid))


'''ХЭНДЛЕР РЕАГИРУЮЩИЙ НА ИНЛАЙН КНОПКИ С МЕСЯЦАМИ '''
async def inlinemonth_info(callback: types.CallbackQuery):
    monthid = callback.data[-2:]
    year = year_handlers.year
    sum = monthdb.summaoftype("РАСХОД", monthid, year)
    await callback.message.answer(f'<b>РАСХОДЫ ЗА ВЫБРАННЫЙ МЕСЯЦ {sum}</b>'
                                  , reply_markup=reply_journalkb("РАСХОД", monthid,year))
    await callback.answer(callback.data)


"""РЕАГИРУЕТ НА ИНЛАЙН КНОПКУ ПОСМОТРЕТЬ ДОХОДЫ """
async def viev_income(callback: types.CallbackQuery):
    year = year_handlers.year
    if len(callback.data) == 11:
        period = 'МЕСЯЦ'
        sum = monthdb.summaoftype("ДОХОД", callback.data[5:7], year)
        month = callback.data[5:7]
    else:
        period = f'{year} ГОД'
        sum = ' '
        month = 0

    await callback.message.answer(f'<b>ДОХОДЫ ЗА {period} {sum}</b>',
                                  reply_markup=reply_journalkb('ДОХОД', month, year, 0))

    await callback.answer(callback.data)
    print(callback.data)

'''РАСКРЫВАЕТ ЖУРНАЛ РАСХОДОВ ПО ОТДЕЛЬНОЙ КАТЕГОРИИ (ЭТО КОНЕЧНЫЙ РЕЗУЛЬТАТ ИЗ КОТОРОГО ДАЛЬШЕ
НЕВОЗМОЖНО ПРОВАЛИТЬСЯ)'''
async def expListMonth(callback: types.CallbackQuery):
    print(callback.data)
    await callback.message.answer(kategory_expances(callback.data[16:], callback.data[12:16], callback.data[10:12]))
    await callback.answer(callback.data[16:])


def register_month(dp: Dispatcher):
    dp.register_callback_query_handler(expListMonth, Text(startswith='ПОДРОБНЕЕМ'))
    dp.register_callback_query_handler(viev_income, Text(startswith='viev_'))
    dp.register_callback_query_handler(inlinemonth_info, Text(startswith='month_'))
    dp.register_message_handler(month_info, text=['ЖУРНАЛ'])

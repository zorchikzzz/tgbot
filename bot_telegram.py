import time


def start_bot():
    try:
        from aiogram.utils import executor
        from createbot import dp

        async def on_startup(_):
            print('БОТ РАБОТАЕТ')

        from handlers import other, journal, year_handlers, last10handlers, balancehandlers

        journal.register_month(dp)
        year_handlers.register_year(dp)
        last10handlers.register_last10(dp)
        balancehandlers.registerbalancehandlers(dp)
        other.register_all(dp)


        executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
    except Exception:
        print('ЧТО ТО ПОШЛО НЕ ТАК\nПЕРЕЗАГРУЗКА ЧЕРЕЗ 10 СЕКУНД')
        time.sleep(10)
        print('ЗАПУСК БОТА')
        start_bot()


start_bot()

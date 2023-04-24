import time


def start_bot():
    try:
        from aiogram.utils import executor
        from createbot import dp

        async def on_startup(_):
            print('БОТ РАБОТАЕТ')

        from handlers import all_handlers, month_handlers, year_handlers, last10handlers, balancehandlers

        month_handlers.register_month(dp)
        year_handlers.register_year(dp)
        last10handlers.register_last10(dp)
        balancehandlers.registerbalancehandlers(dp)
        all_handlers.register_all(dp)


        executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
    except Exception:
        print('ЧТО ТО ПОШЛО НЕ ТАК\nПЕРЕЗАГРУЗКА ЧЕРЕЗ 10 СЕКУНД')
        time.sleep(10)
        print('ЗАПУСК БОТА')
        start_bot()


start_bot()

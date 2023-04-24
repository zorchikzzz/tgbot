from aiogram import Bot
from aiogram.dispatcher import Dispatcher

TOKEN='5829830933:AAFm29KTHLtOFoF4YM5_Kq_GN2OEhHKR_oU'
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
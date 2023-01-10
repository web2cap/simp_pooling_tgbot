from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from core.settings import TG_TOKEN
from db.sqlite_db import sql_start

storage = MemoryStorage()

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot, storage=storage)

sql_command = sql_start()
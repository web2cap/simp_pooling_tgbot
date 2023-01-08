from aiogram import Dispatcher, types

from core.create_bot import bot
from core.settings import MESSAGES


# @dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, MESSAGES["hello"])
        await message.delete()
    except Exception as e:
        print(f"error: {e}")
        await message.reply(MESSAGES["only_direct"])

def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
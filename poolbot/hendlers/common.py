from aiogram import Dispatcher, types
from keyboards import client_kb


# @dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    await message.reply(message.text, reply_markup=client_kb.keybord_client)
    # await bot.send_message(message.from_user.id, message.text)


def register_hendlers_common(dp: Dispatcher):
    dp.register_message_handler(echo_send)

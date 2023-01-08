from aiogram import Dispatcher, types


# @dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

def register_hendlers_common(dp: Dispatcher):
    dp.register_message_handler(echo_send)
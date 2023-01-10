from aiogram import Dispatcher, types

from core.create_bot import bot, db
from core.settings import CURRENCY, MESSAGES
from keyboards import client_kb


# @dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    """Send hello message.
    If user make start in group, forward user to bot chat."""

    try:
        await bot.send_message(
            message.from_user.id,
            MESSAGES["hello"],
            reply_markup=client_kb.keybord_client
        )
        await message.delete()
    except Exception as e:
        print(f"error: {e}")
        await message.reply(MESSAGES["only_direct"])

async def command_menu(message: types.Message):
    """Send all menu."""

    menu = await db.get_all()
    for menu_item in menu:
        await bot.send_photo(
            message.from_user.id,
            menu_item[0],
            "\n".join(
                [
                    menu_item[1],
                    f"Description: {menu_item[2]}",
                    f"Price: {menu_item[3]} {CURRENCY}",
                ]
            ),
            reply_markup=client_kb.keybord_client,
        )

def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(command_menu, commands=["menu"])
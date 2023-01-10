from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from core.create_bot import bot, db # , dp
from core.settings import CURRENCY, MESSAGES
from keyboards import admin_kb
from states.admin import FSMPizza

ADMIN_ID = None

# @dp.message_handler(commands=["moderator"], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    """Get admin id from group and start admin session in direct."""

    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(
        message.from_user.id,
        MESSAGES["admin_active"],
        reply_markup=admin_kb.keybord_admin,
    )
    await message.delete()


# dp.message_handler(commands='upload', state=None)
async def cm_start(message: types.Message):
    """Start new item upload."""

    # TODO: replase all cheks if admin to decorator
    if message.from_user.id != ADMIN_ID:
        return
    await FSMPizza.photo.set()
    await message.reply(MESSAGES["admin_upload_photo"])


# @dp.message_handler(state="*", commands="break")
# @dp.message_handler(Text(equals="break", ignore_case=True), state="*")
async def break_upload(message: types.Message, state: FSMContext):
    """Break upload."""

    if message.from_user.id != ADMIN_ID:
        return
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply(MESSAGES["admin_upload_break"])


# @dp.message_handler(content_types=["photo"], state=FSMPizza.photo)
async def load_photo(message: types.Message, state: FSMContext):
    "Catch photo and write to dict."

    if message.from_user.id != ADMIN_ID:
        return
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMPizza.next()
    await message.reply(MESSAGES["admin_upload_name"])


# @dp.message_handler(state=FSMPizza.name)
async def load_name(message: types.Message, state: FSMContext):
    "Catch name and write to dict."

    if message.from_user.id != ADMIN_ID:
        return
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMPizza.next()
    await message.reply(MESSAGES["admin_upload_description"])


# @dp.message_handler(state=FSMPizza.description)
async def load_description(message: types.Message, state: FSMContext):
    "Catch description and write to dict."

    if message.from_user.id != ADMIN_ID:
        return
    async with state.proxy() as data:
        data["description"] = message.text
    await FSMPizza.next()
    await message.reply(MESSAGES["admin_upload_price"])


# @dp.message_handler(state=FSMPizza.price)
async def load_price(message: types.Message, state: FSMContext):
    "Catch price and write to dict. Write data. Close state."

    if message.from_user.id != ADMIN_ID:
        return
    async with state.proxy() as data:
        data["price"] = float(message.text)

    # Debug data
    # async with state.proxy() as data:
    #     await message.reply(str(data))
    query_status = await db.add(state)
    await message.reply(query_status)

    # Close state
    await state.finish()


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith("del "))
async def callback_delete_item(callback_query: types.CallbackQuery):
    """Send callback answer that item deleted."""

    name = callback_query.data.replace("del ", "")
    # TODO: add chech that name is exist
    await db.delete(name)
    await callback_query.answer(
        text=f"The {name} deleted syccessfully.",
        show_alert=True,
    )


# @dp.message_handler(commands="delete")
async def delete_item(message: types.Message):
    """Send all menu with delete button."""

    if message.from_user.id != ADMIN_ID:
        return
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
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(
                    "Delete",
                    callback_data=f"del {menu_item[1]}",
                )
            ),
        )


def register_hendlers_admin(dp: Dispatcher):
    """Register admin hendlers. For call from main file."""

    # Start add pizza
    dp.register_message_handler(cm_start, commands="upload", state=None)
    # Break add pizza
    dp.register_message_handler(break_upload, state="*", commands="break")
    dp.register_message_handler(
        break_upload, Text(equals="break", ignore_case=True), state="*"
    )
    # Add pizza dialog
    dp.register_message_handler(
        load_photo, content_types=["photo"], state=FSMPizza.photo
    )
    dp.register_message_handler(load_name, state=FSMPizza.name)
    dp.register_message_handler(load_description, state=FSMPizza.description)
    dp.register_message_handler(load_price, state=FSMPizza.price)
    # TODO: Delete pizza hendlers
    dp.register_message_handler(delete_item, commands="delete")
    dp.register_callback_query_handler(
        callback_delete_item, lambda x: x.data and x.data.startswith("del ")
    )
    # Admin mode activate and menu
    dp.register_message_handler(
        make_changes_command, commands=["moderator"], is_chat_admin=True
    )

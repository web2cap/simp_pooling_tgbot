from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_upload= KeyboardButton("/upload")
button_break = KeyboardButton("/break")
button_delete = KeyboardButton("/delete")

keybord_admin = ReplyKeyboardMarkup(resize_keyboard=True)
keybord_admin.row(button_upload, button_break, button_delete)
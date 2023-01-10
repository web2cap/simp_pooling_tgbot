from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_help = KeyboardButton("/help")
button_start = KeyboardButton("/menu")
button_share_phone = KeyboardButton("share phone", request_contact=True)
button_share_location = KeyboardButton("share_location", request_location=True)

# replace default keybord to custom
# little buttons and hide after press
keybord_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# keybord_client.add(button_start).insert(button_help)
keybord_client.row(button_help, button_start, button_share_phone, button_share_location)
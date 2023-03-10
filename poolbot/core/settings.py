import os

from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")

DATABASE = {"name": "pizza.db"}

BOT_USERNAME = "username"

MESSAGES = {
    "on_startup": "Bot is online",
    "hello": "Hello! Lets start!!!",
    "only_direct": "You can talk with bot only in derect,"
    f"please start chat with bot https://t.me/{BOT_USERNAME}",
    "admin_upload_photo": "Please upload photo",
    "admin_upload_name": "Write a name",
    "admin_upload_description": "Write a description",
    "admin_upload_price": "Write a price",
    "admin_upload_break": "Canceled!",
    "admin_active": "Admin mode is activate",
}

CURRENCY = "$"

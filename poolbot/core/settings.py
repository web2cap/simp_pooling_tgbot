import os

from dotenv import load_dotenv


load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")

MESSAGES = {
    "on_startup" : "Bot is online",
    "hello" : "Hello! Lets start!!!",
    "only_direct" : "You can talk with bot only in derect,"
                    "please start chat with bot https://t.me/englishdailybot",
    
}
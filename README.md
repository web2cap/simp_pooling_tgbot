# Telegram pooling bot on aiogram: Pizza bot with admin

This is simple pooling telegram bot example with module structure.

Bot contain 2 interfaces: client and admin

By tutorial https://www.youtube.com/watch?v=TYs3-uyjC30&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ

Structure and code improved compared to the code in the tutorial

### Stack

 - Python
 - Aiogram
 - Sqlite3

 ### Local start

 - Clone the repository and go to project folder
 - Create and activate virtual environment(use python 3.8 or older), install requirements:

```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

 - Create your bot and get bot telegram token in https://t.me/BotFather
 - Create .env file with bot telegram token:
 
```
echo TG_TOKEN=YOUR_TOKEN_HERE >> .env
```
 - Specify bot username in poolbot/core/settings.py file in BOT_USERNAME
 - Create telegram group and add your bot to the group like an admin
 - Run bot:

```
./localrun.sh
```

##  Commands

### Admin mode

/moderator (in group chat) - activate admin mode

/upload - upload a pizza

/break - break adding

/delete a pizza


### Client mode
/start - start use bot

/help - get help

/menu - get menu

/share phope - share ypur phone


## Structure
```
├── LICENSE
├── README.md
├── localrun.sh # Local run script
├── poolbot # Bot project
│   ├── core
│   │   ├── create_bot.py # Init Bot, Dispatcher, DB
│   │   └── settings.py # All settings
│   ├── db
│   │   └── sqlite_db.py # DB service
│   ├── hendlers # Bot hendlers
│   │   ├── admin.py
│   │   ├── client.py
│   │   └── common.py
│   ├── keyboards # Bot keyboards
│   │   ├── admin_kb.py
│   │   └── client_kb.py
│   ├── states # Bot states
│   │   └── admin.py
│   └── telegram_bot.py # Main file
└── requirements.txt # Project requirements
```




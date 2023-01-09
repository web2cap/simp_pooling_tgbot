from aiogram.utils import executor

from core.create_bot import dp
from core.settings import MESSAGES
from hendlers import admin, client, common 

async def on_startup(_):
    print(MESSAGES["on_startup"])

client.register_hendlers_client(dp)
admin.register_hendlers_admin(dp)
common.register_hendlers_common(dp)


# Answer on ofline messages
executor.start_polling(dp, skip_updates=False, on_startup=on_startup)




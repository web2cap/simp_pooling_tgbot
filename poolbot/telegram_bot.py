from aiogram.utils import executor

from core.create_bot import dp
from core.settings import MESSAGES
from hendlers import client, common # , admin

async def on_startup(_):
    print(MESSAGES["on_startup"])

client.register_hendlers_client(dp)
common.register_hendlers_common(dp)

# Answer on ofline messages
executor.start_polling(dp, skip_updates=False, on_startup=on_startup)




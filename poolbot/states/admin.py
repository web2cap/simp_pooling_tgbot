from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMPizza(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
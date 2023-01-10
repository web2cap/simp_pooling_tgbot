import sqlite3 as sq

from aiogram.dispatcher import FSMContext

from core.settings import DATABASE


class PizzaDB():
    """Manage data for pizza cafe in db sqlite3."""

    base = None
    cursor = None

    def __init__(self):
        """Init connection and create tables if it not exists."""

        self.base = sq.connect(DATABASE["name"])
        self.cursor = self.base.cursor()
        if not self.base:
            assert("Database connection error")
        sql = """create table if not exists menu(
                    img TEXT,
                    name TEXT PRIMARY KEY,
                    description TEXT, price TEXT
                )"""
        self.cursor.execute(sql)
        self.base.commit()

    async def add(self, state: FSMContext):
        """Add new pizza, from context manager data."""

        async with state.proxy() as data:
            try:
                self.cursor.execute(
                    "INSERT INTO menu VALUES (?, ?, ?, ?)",
                    tuple(data.values())
                )
                self.base.commit()
            except Exception as e:
                print(f"error: {e}")
                return e
            return data["name"]

    async def get_all(self):
        "Get all pizzas."

        sql = "select * from menu"
        result = []
        for ret in self.cursor.execute(sql).fetchall():
            result.append(ret)
        return result
        






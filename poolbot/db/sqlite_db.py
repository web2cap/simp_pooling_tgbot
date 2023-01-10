import sqlite3 as sq

from aiogram.dispatcher import FSMContext
from core.settings import DATABASE


class PizzaDB:
    """Manage data for pizza cafe in db sqlite3."""

    # TODO: add get by name

    base = None
    cursor = None

    def __init__(self):
        """Init connection and create tables if it not exists."""

        self.base = sq.connect(DATABASE["name"])
        self.cursor = self.base.cursor()
        if not self.base:
            assert "Database connection error"
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
            sql = "insert into menu values (?, ?, ?, ?)"
            try:
                self.cursor.execute(sql, tuple(data.values()))
                self.base.commit()
            except Exception as e:
                print(f"error: {e}")
                return e
            return data["name"]

    async def get_all(self):
        "Get all pizzas."

        sql = "select * from menu"
        return self.cursor.execute(sql).fetchall()
        # result = []
        # for ret in self.cursor.execute(sql).fetchall():
        #     result.append(ret)
        # return result

    async def delete(self, name):
        "Delete pizza by name."

        sql = "delete from menu where name == ?"
        self.cursor.execute(sql, (name,))
        self.base.commit()

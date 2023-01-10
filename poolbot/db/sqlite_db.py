import sqlite3 as sq

from aiogram.dispatcher import FSMContext


def sql_start():
    base = sq.connect("pizza.db")
    dbcursor = base.cursor()
    if base:
        print("Database connected")
    sql = "create table if not exists menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)"
    base.execute(sql)
    base.commit()

    async def sql_command(state: FSMContext):
        async with state.proxy() as data:
            try:
                dbcursor.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", tuple(data.values()))
                base.commit()
            except Exception as e:
                print(f"error: {e}")
                return e
            return data["name"]

    return sql_command

# async def sql_command(state: FSMContext):
#     async with state.proxy() as data:
#         dbcursor.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", tuple(data.values()))
#         base.commit()

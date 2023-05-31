import datetime
import sqlite3

sql_request_create_table_if_not_exist = """
    CREATE TABLE IF NOT EXISTS table_with_birds(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       bird_name TEXT NOT NULL,
       date_when_added TEXT NOT NULL
    );
"""

sql_request_add_new_bird = """
    INSERT INTO table_with_birds (bird_name, date_when_added) VALUES (?, ?);
"""

sql_request_check_if_exist = """
    SELECT EXISTS(
        SELECT 1 
        FROM table_with_birds 
        WHERE bird_name = ? 
        LIMIT 1
    )
"""


def log_bird(
    c: sqlite3.Cursor,
    bird_name: str,
    date_time: str
) -> None:
    c.execute(sql_request_add_new_bird, (bird_name, date_time))


def check_if_such_bird_already_seen(
    c: sqlite3.Cursor,
    bird_name: str
) -> bool:
    result, *_ = c.execute(sql_request_check_if_exist, (bird_name,)).fetchone()
    return bool(result)


name = input('Имя птицы\n> ')
count = int(input('Сколько птиц\n> '))
time = datetime.datetime.utcnow().isoformat()
with sqlite3.connect("hw.db") as conn:
    cursor = conn.cursor()
    cursor.execute(sql_request_create_table_if_not_exist)
    if not check_if_such_bird_already_seen(cursor, name):
        log_bird(cursor, name, time)

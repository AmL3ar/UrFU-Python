import sqlite3

sql_request = """
    SELECT COUNT(*)
        FROM(
            SELECT *
            FROM table_truck_with_vaccine 
            WHERE truck_number = ? AND temperature_in_celsius NOT BETWEEN 16 and 20
        )
"""


def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        number: str
) -> bool:
    result, *_ = c.execute(sql_request, (number,)).fetchone()
    # print(result)
    return result >= 3


with sqlite3.connect('hw.db') as conn:
    cursor = conn.cursor()
    truck_number = input("Введите номер грузовика: ")
    print(check_if_vaccine_has_spoiled(cursor, truck_number))

    # result = cursor.execute('SELECT * FROM table_truck_with_vaccine').fetchall()
    # for item in result:
    #     if check_if_vaccine_has_spoiled(cursor, item[2]):
    #         print(item[2])
    #         break

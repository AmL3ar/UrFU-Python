import sqlite3

sql_request_get_salary_employee = """
    SELECT salary
        FROM table_effective_manager
        WHERE name=?
"""

sql_request_drop_employee = """
    DELETE
        FROM table_effective_manager
        WHERE name=?
"""

sql_request_update_salary_employee = """
    UPDATE table_effective_manager
        SET salary=?
        WHERE name=?
"""


def ivan_sovin_the_most_effective(
    c: sqlite3.Cursor,
    name: str,
) -> None:
    salary_ivan_sovin, *_ = c.execute(sql_request_get_salary_employee, ('Иван Совин', )).fetchone()
    salary_employee, *_ = c.execute(sql_request_get_salary_employee, (name, )).fetchone()
    new_salary_employee = int(salary_employee * 1.1)
    if new_salary_employee > salary_ivan_sovin:
        c.execute(sql_request_drop_employee, (name, ))
    else:
        c.execute(sql_request_update_salary_employee, (new_salary_employee, name))

name_employee = input('Имя сотрудника\n> ')
with sqlite3.connect('hw.db') as conn:
    cursor = conn.cursor()
    ivan_sovin_the_most_effective(cursor, name_employee)

import csv
import sqlite3

sql_request = """
    DELETE 
        FROM table_fees
        WHERE truck_number = ? AND timestamp = ?
"""


def delete_wrong_fees(
        c: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    with open(wrong_fees_file, 'r') as f:
        wrong_fees = list(csv.reader(f))
        for truck_number, timestamp in wrong_fees[1:]:
            c.execute(sql_request, (truck_number, timestamp))


with sqlite3.connect("hw.db") as conn:
    cursor = conn.cursor()
    delete_wrong_fees(cursor, "wrong_fees.csv")

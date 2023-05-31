import multiprocessing
from multiprocessing.pool import ThreadPool, Pool
import requests
import time
import sqlite3

characters = []
URL = "https://swapi.dev/api/people/"
sql_add_character_from_dict = """
    INSERT INTO star_wars_characters (name, birth_year, sex) VALUES (?,?,?)
"""


def get_star_wars_character(url: str, i: int):
    global characters
    response = requests.get(url+str(i))
    if response.status_code == 200:
        character_dict = dict(response.json())
        print(character_dict["name"], character_dict["birth_year"], character_dict["gender"])
        if character_dict is not None:
            characters.append((character_dict["name"], character_dict["birth_year"], character_dict["gender"]))


def load_characters_with_threadpool():
    with ThreadPool(processes=multiprocessing.cpu_count() * 5) as pool:
        start = time.time()
        args = []
        for i in range(1, 22):
            args.append((URL, i))
        pool.starmap(get_star_wars_character, args)

        cursor.executemany(sql_add_character_from_dict, characters)
        print("-------------Done in {:4}-------------\n".format(time.time() - start))


def load_characters_with_pool():
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        start = time.time()
        args = []
        for i in range(1, 22):
            args.append((URL, i))
        pool.starmap(get_star_wars_character, args)

        cursor.executemany(sql_add_character_from_dict, characters)
        print("-------------Done in {:4}-------------".format(time.time() - start))


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM star_wars_characters")
        load_characters_with_threadpool()
        cursor.execute("DELETE FROM star_wars_characters")
        load_characters_with_pool()
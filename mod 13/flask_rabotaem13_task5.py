import random
import sqlite3

countries = ['Испания', 'Франция', 'Германия', 'Италия', 'Англия', 'Нидерланды', 'Португалия', 'Бельгия', 'Аргентина', 'Бразилия', 'Россия']

sql_request_insert_teams = """
    INSERT INTO uefa_commands (command_number, command_name, command_country, command_level)
        VALUES (?, ?, ?, ?)
"""

sql_request_insert_draw = """
    INSERT INTO uefa_draw (command_number, group_number)
        VALUES (?, ?)
"""


def generate_test_data(
        c: sqlite3.Cursor,
        number_of_groups: int
) -> None:
    teams = []
    for i in range(number_of_groups * 4):
        name = f'Football team №{i + 1}'
        country = random.choice(countries)
        if i % 4 == 0:
            level = "Сильная"
        elif i % 4 == 1 or i % 4 == 2:
            level = "Средняя"
        else:
            level = "Слабая"
        teams.append((i+1, name, country, level))
    random.shuffle(teams)
    c.execute("DELETE FROM uefa_commands")
    c.executemany(sql_request_insert_teams, teams)

    groups = [[] for _ in range(number_of_groups)]
    strong = list(filter(lambda team: team[3] == 'Сильная', teams))
    medium = list(filter(lambda team: team[3] == 'Средняя', teams))
    soft = list(filter(lambda team: team[3] == 'Слабая', teams))
    for i in range(number_of_groups):
        strong_team = random.choice(strong)
        groups[i].append(strong_team)
        strong.remove(strong_team)

        fst_medium_team, scd_medium_team = random.sample(medium, 2)
        groups[i].extend([fst_medium_team, scd_medium_team])
        medium.remove(fst_medium_team)
        medium.remove(scd_medium_team)

        soft_team = random.choice(soft)
        groups[i].append(soft_team)
        soft.remove(soft_team)
        random.shuffle(groups[i])

    draw = [(team[0], i + 1) for i in range(len(groups)) for team in groups[i]]
    c.execute("DELETE FROM uefa_draw")
    c.executemany(sql_request_insert_draw, draw)


with sqlite3.connect("hw.db") as conn:
    cursor = conn.cursor()
    count_groups = int(input('Количество групп\n> '))
    generate_test_data(cursor, count_groups)

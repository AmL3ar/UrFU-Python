import json
import operator
import os
import re
from collections import Counter
from itertools import groupby

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skillbox_json_messages.log')) as data:
    logs = []
    for log in data.readlines():
        logs.append(json.loads(log))


# Первая задача
def count_levels():
    count_level_dict = dict()
    for level, logs_list in groupby(logs, key=lambda log: log['level']):
        if level in count_level_dict:
            count_level_dict[level] += len(list(logs_list))
        else:
            count_level_dict[level] = len(list(logs_list))
    for level in count_level_dict.keys():
        print(f'{level} - {count_level_dict[level]}')


# Вторая задача
def max_count_logs_by_hour():
    count_logs_by_hours = dict()
    for hour, logs_list in groupby(logs, key=lambda log: log['time'][:2]):
        count_logs_by_hours[hour] = len(list(logs_list))
    result = max(count_logs_by_hours.items(), key=operator.itemgetter(1))[0]
    print(result)


# Третья задача
def count_critical_by_period():
    filtered_logs = list(filter(lambda log: bool(re.search(r"05:[0-1]" and log["level"] == "CRITICAL", log["time"])), logs))
    print(len(filtered_logs))


# Четвертая задача
def count_logs_have_dogs():
    filtered_logs = list(filter(lambda log: "dog" in log["message"], logs))
    print(len(filtered_logs))


# Пятая задача
def frequent_word_in_warning():
    words_list_from_warning = list()
    filtered_logs = list(filter(lambda log: log['level'] == 'WARNING', logs))
    for log in filtered_logs:
        words_list_from_warning += log['message'].split()
    print(Counter(words_list_from_warning).most_common()[0][0])


count_levels()
max_count_logs_by_hour()
count_critical_by_period()
count_logs_have_dogs()
frequent_word_in_warning()

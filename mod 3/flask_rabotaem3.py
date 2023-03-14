from datetime import datetime
from flask import Flask

app = Flask(__name__)

# task 1

week = ("понедельника","вторника","среды","четверга","пятницы","субботы","воскресенья")

@app.route('/hello-world/<name>')
def good_day(name):
    weekday = datetime.today().weekday()
    return f"Привет, {name}. Хорош(-ей/-его) {week[weekday]}"

# task 2
def decrypt(stro):
    res = []
    for el_i in stro:
        res.append(el_i)
        if len(res) > 2 and (res[-1],res[-2])==(".","."):
            res.pop()
            res.pop()
            if res:
                res.pop()
                
    return "".join(el_i for el_i in res if el_i != ".")

# task 3

tracker = dict()

@app.route('/add/<date>/<int:number>')
def add(date,number):
    year, month = date[:4], date[4:6]
    tracker.setdefault(year, {}).setdefault(month, 0)
    if tracker[year][month] == None:
        tracker[year][month] = number
    else:
        tracker[year][month] += number
    return f"Мы сохранили ваши финансы"

@app.route('/calculate/<int:year>')
def calculate_years(year):
    summ = 0
    for _,el_j in enumerate(tracker[str(year)].items()):
        summ += el_j[1]      
    return f"Суммарные траты за {year} год: {summ}"

@app.route('/calculate/<string:year>/<string:month>')
def calculate_years_month(year,month):
    return f"Ваши траты {tracker[year][month]}"




if __name__=="__main__":
    app.run(debug = True)
import datetime
import random
from flask import Flask

app = Flask(__name__)
car = ["Chevrolet", "Renault", "Ford", "Lada"]
cat = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

@app.route('/hello_world')
def inex():
    return "Привет, мир!"

@app.route('/cars')
def cars():
    return ", ".join(car)

@app.route('/cats')
def cats():
    return random.choice(cat)

@app.route('/get_time/now')
def now():    
    current_time = datetime.datetime.now()
    return f"Точное время: {current_time}"

@app.route('/get_time/future')
def future():
    current_time = datetime.datetime.now()
    current_time_after_hour =current_time + datetime.timedelta(hours = 1)
    return f"Точное время через час будет {current_time_after_hour}"

words = 0
with open("war_and_peace.ru.txt","r",encoding="utf-8") as file_name:     
    words = file_name.read().split()
file_name.close()

@app.route('/get_random_word')
def rnd_word(): 
    rand_word = words[random.randint(0,len(words))]       
    return f"Случайное слово из произведения: {rand_word}"
   

@app.route('/counter') 
def counter(): 
   counter.visits += 1 
   return f"Столько раз вы заходили на сайт: {counter.visits}"
 
counter.visits = 0


if __name__=="__main__":
    app.run(debug = True)
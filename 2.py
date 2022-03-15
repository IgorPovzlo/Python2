from flask import Flask
from faker import Faker

app = Flask(__name__)

@app.route("/get_avr_data")
def get_avr_data():
    file=open("hw.csv", encoding= "UTF8")
    next(file)
    weight = 0
    height = 0
    count = 0
    for line in file:
        b = line.split(", " )
        b= [float(i) for i in b]
        count += 1
        weight += b[2]
        height += b[1]

    return  (f"<h1> Средний вес {round(weight/count* 0.45359237, 1)} кг. \
     <br>Средний рост {round((height/count* 2.54), 1)} CM.")



@app.route("/get_requirements")
def get_requirements():
    f = open("requirements.txt", "r")
    list = []
    for i in f:
        list.append(i)
    return "<p>" " ".join(list)


@app.route("/get_random_students")
def get_random_students():
    list = []
    fake = Faker()
    for _ in range(50):
        list.append(fake.name())

    return '<p>'" ".join(list)



app.run(debug=True)


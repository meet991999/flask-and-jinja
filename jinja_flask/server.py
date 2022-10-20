from flask import Flask, render_template
import random
from datetime import date
import requests
app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,20)
    # date_today = datetime.datetime.now()
    today = date.today().year
    return render_template("index.html", num=random_number, dates=today)

@app.route("/api/<name>")
def get_page(name):
    para={"name" : name}
    response = requests.get("https://api.agify.io", params=para)
    a = response.json()
    p_age = a["age"]
    p_name = a["name"]
    gen_res = requests.get("https://api.genderize.io", params=para)
    gender_res = gen_res.json()
    gender = gender_res["gender"]

    return render_template("api.html", a=p_age, n = p_name, g = gender)


if __name__ == "__main__":
    app.run(debug=True)

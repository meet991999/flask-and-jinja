from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/ea151d180bf9463a580d")
data = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", d = data)

@app.route("/1")
def blog_one():
    return render_template("post.html", d=data[0])

@app.route("/2")
def blog_two():
    return render_template("post.html", d=data[1])


if __name__ == "__main__":
    app.run(debug=True)

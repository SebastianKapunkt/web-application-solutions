from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/grades/", methods=["GET"])
def get_grades():
    grades = [
        {
            "grade": 95,
            "name": "Anton"
        },
        {
            "grade": 90,
            "name": "Caesar"
        },
        {
            "grade": 100,
            "name": "Berta"
        }
    ]
    # calculating grades , details ignored
    return jsonify(grades)


app.run()

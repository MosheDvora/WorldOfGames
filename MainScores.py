from flask import Flask, redirect, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    try:
        file = open("score/Scores.txt", "r")
        value = file.readline()
        return render_template('score_server.html', score=value)
    except IOError:
        value = "There was a problem reading the score file"
        return render_template('error.html', error=value)


app.run(host="0.0.0.0", port=5001)

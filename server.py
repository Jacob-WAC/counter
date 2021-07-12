from typing import Counter
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/')
def index():
    if "num_sessions" in session:
        session["num_sessions"] += 1
    else:
        session["num_sessions"] = 0
    print(session["num_sessions"])
    return render_template('index.html', number=session["num_sessions"])


@app.route('/plus2', methods=["POST"])
def plus2():
    session["num_sessions"] += 1
    return redirect('/')


@app.route('/destroy', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = "he's here! the phantom of the opera!"
    app.run(debug=True)

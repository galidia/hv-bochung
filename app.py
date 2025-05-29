
from flask import Flask, render_template, request
from bochung import get_timetable
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    student_id = request.form.get("student_id")
    date = request.form.get("date")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    result_text = get_timetable(student_id, date)
    return render_template("result.html", student_id=student_id, date=date, result=result_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

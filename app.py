from flask import Flask, render_template, request
from bochung import get_timetable
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result_text = None
    if request.method == "POST":
        student_id = request.form["student_id"]
        result_text = get_timetable(student_id)
    return render_template("index.html", result=result_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

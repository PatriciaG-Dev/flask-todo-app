
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

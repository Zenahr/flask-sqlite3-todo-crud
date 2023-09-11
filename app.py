from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path, PurePath

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{PurePath.joinpath(Path(__file__).resolve().parent, 'todo.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/add', methods=["POST"])
def add():
    data = request.form["todo_item"]
    todo = Todo(text=data, complete=False)
    db.session.add(todo)
    db.session.commit()
    # return data # DEBUG REQUEST
    return redirect(url_for("index"))


@app.route('/update', methods=["POST"])
def update():
    completed_ids = [int(i) for i in request.form]
    for todo in Todo.query.all():
        setattr(todo, 'complete', False if todo.id not in completed_ids else True)
    db.session.commit()
    # return request.form # DEBUG REQUEST
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
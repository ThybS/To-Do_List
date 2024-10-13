from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

TODO_FILE = "todos.txt"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return file.readlines()
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        file.writelines(todos)

@app.route('/')
def index():
    todos = load_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo'] + "\n"
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['POST'])
def edit(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        new_todo = request.form['new_todo'] + "\n"
        todos[index] = new_todo
        save_todos(todos)
    return redirect(url_for('index'))

@app.route('/complete/<int:index>', methods=['POST'])
def complete(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos.pop(index)
        save_todos(todos)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
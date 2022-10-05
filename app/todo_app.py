from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Todo

todo_app = Blueprint('todo_app', __name__)




@todo_app.route('/todo')
def index():
    # show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('todo_app.html', todo_list=todo_list)


@todo_app.route("/todo/add", methods=["POST"])
def add():
    # add new item
    title = request.form.get('title')
    content = request.form.get('content')
    new_todo = Todo(title=title, content=content, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('todo_app.index'))


@todo_app.route("/todo/update/<int:item_id>")
def update(item_id):
    # add new item
    todo = Todo.query.filter_by(id=item_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('todo_app.index'))


@todo_app.route("/todo/delete/<int:item_id>")
def delete(item_id):
    # add new item
    todo = Todo.query.filter_by(id=item_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo_app.index'))

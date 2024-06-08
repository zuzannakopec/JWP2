from flask import Flask, render_template, request, redirect, url_for
from models import db, Task, Teacher

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    name = request.form.get('name')
    if name:
        new_task = Task(name=name)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/addTeacher', methods=['POST'])
def add_teacher():
    name = request.form.get('name')
    subject = request.form.get('subject')
    time = request.form.get('time')
    if name:
        new_teacher = Teacher(name=name, subject=subject, time=time)
        db.session.add(new_teacher)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:teacher_id>')
def delete_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')

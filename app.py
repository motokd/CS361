from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration, Login, AddTask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a6da61d6DGASDA65ads6A546asAFDGSADA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    # Will instantiate and display User object as we want it displayed
    def __repr__(self):
        return f"User('{self.username}')"


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(50), nullable=False)
    task_duedate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    task_priority = db.Column(db.String(6), nullable=False)
    task_details = db.Column(db.Text(2500), nullable=True)

    def __repr__(self):
        return f"Task('{self.task_title}', '{self.task_priority}', '{self.task_duedate}')"

user = 'david'
passw = 'Al Adam 1534'

file_path = open('C:\CS 361\Project2\Michael Microservice\CS361Service-main/response.txt', 'r')
f = file_path.readline()
print(f)

tasks = [
    {
        'title': 'Task 1',
        'content': 'details of task content would go here....',
        'priority': 'low',
        'date_posted': '10/27/2021'
    }

]

users = [
    {
        'username': 'david',
        'password': 'password'
    }

]

@app.route("/home")
def home():
    return render_template('home.html', tasks=tasks)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.username.data == user and form.password.data == passw and \
            f == 'true':
            flash('login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/addtask", methods=['GET', 'POST'])
def add():
    form = AddTask()
    if form.validate_on_submit():
        flash(f'Task Added Successfully', 'success')
        return redirect(url_for('login'))
    return render_template('addtask.html', title='Add Task', form=form)


if __name__ == '__main__':
    app.run(debug=True)
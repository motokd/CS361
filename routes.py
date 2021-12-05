from flask import render_template, url_for, flash, redirect, request, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length
from taskmanager.models import User, Task
from flask_login import login_user, LoginManager

#set up the database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a6da61d6DGASDA65ads6A546asAFDGSADA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_mgr = LoginManager(app)

#microservice call to be used to authenticate user
file_path_authenticate = open('/Michael Microservice/CS361Service-main/response.txt', 'r')
f = file_path_authenticate.readline()
print(f)

#microservice call to be use to generate password
file_path_passwordgen = open('/response.txt', 'r')
f = file_path_passwordgen.readline()

def generatePassword():
    return f

@app.route("/home")
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    generatePassword()      #to be used to generate random password from teammates microservice
    if form.validate_on_submit():
        user_register = User(username=form.username.data, password=form.password.data)
        db.session.add(user_register)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        password = User.query.filter_by(password=form.password.data).first()
        if user and password:
            login_user(user, remember=True)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/addtask/new", methods=['GET', 'POST'])
def add():
    form = AddTask()
    if form.validate_on_submit():
        task = Task(task_title=form.add_task_title.data, task_priority=form.priority.data, task_details=form.details.data)
        db.session.add(task)
        db.session.commit()
        flash(f'Task Added', 'success')
        return redirect(url_for('home'))
    return render_template('addtask.html', title='Add Task', form=form)

@app.route("/task/<int:task_id>")
def task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task.html', title=task.task_title, task=task)

@app.route("/task/<int:task_id>/update", methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    form = AddTask()
    if form.validate_on_submit():
        commit_changes()
        flash('Task Updated Successfully', 'success')
        return redirect(url_for('task', task_id=task.task_id))
    elif request.method == 'GET':
        show_current_task()
    return render_template('addtask.html', title='Update Task', form=form, legend='Update Task')

@app.route("/task/<int:task_id>/delete", methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/help")
def help():
    return render_template('help.html', title='Help')


#Forms for flask templates
class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('CREATE ACCOUNT')
    random_password = SubmitField('CLICK HERE')

class Login(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('LOGIN')

class AddTask(FlaskForm):
    add_task_title = StringField('Task Title')
    date = DateField('Due Date')
    priority = SelectField('Priority', coerce=str, choices=[('HIGH'), ('MEDIUM'), ('LOW')])
    details = TextAreaField('Details')
    submit = SubmitField('ADD TASK')

#method to show details of task, used to reduce long method of update_task
def show_current_task(task_id):
    task = Task.query.get(task_id)
    form = AddTask()

    form.add_task_title.data = task.task_title
    form.priority.data = task.task_priority
    form.date.data = task.task_duedate
    form.details.data = task.task_details

#method to commit the changes, used to reduce long method of update_task
def commit_changes(task_id):
    task = Task.query.get(task_id)
    form = AddTask()

    task.task_title = form.add_task_title.data
    task.task_priority = form.priority.data
    task.task_duedate = form.date.data
    task.task_details = form.details.data
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
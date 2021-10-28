from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245dgfbasfhgha'

posts = [
    {
        'title': 'Task 1',
        'content': 'details of task content would go here....',
        'priority': 'low',
        'date_posted' : '10/27/2021'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


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


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.username.data == 'test' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/new-task", methods=['GET', 'POST'])
def addtask():
    form = AddTask()


if __name__ == '__main__':
    app.run(debug=True)
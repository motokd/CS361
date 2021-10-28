from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length


class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('CREATE ACCOUNT')


class Login(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('LOGIN')

class AddTask(FlaskForm):
    add_task = StringField('Task Title')
    date = DateTimeField('Due Date')
    priority = SelectField('Priority', coerce=str, choices=[('HIGH'), ('medium'), ('low')])
    submit = SubmitField('ADD TASK')
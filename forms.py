from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length


class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('CREATE ACCOUNT')
    random_password = SubmitField('CLICK HERE')


class Login(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('LOGIN')

class AddTask(FlaskForm):
    add_task = StringField('Task Title')
    date = DateField('Due Date', format='%y-%m-%d')
    priority = SelectField('Priority', coerce=str, choices=[('HIGH'), ('MEDIUM'), ('LOW')])
    details = TextAreaField('Details')
    submit = SubmitField('ADD TASK')
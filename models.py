from datetime import datetime
from flask_login import LoginManager
from flask_login import UserMixin

@login_mgr.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#model used to create a user in the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    # Will instantiate and display User object as we want it displayed
    def __repr__(self):
        return f"User('{self.username}')"

#model used to create a task in the database
class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(50), nullable=False)
    task_duedate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    task_priority = db.Column(db.String(6), nullable=False)
    task_details = db.Column(db.Text(2500), nullable=True)

    def __repr__(self):
        return f"Task('{self.task_title}', '{self.task_priority}', '{self.task_duedate}', '{self.task_details}')"

from App.models import User #, Alumni, GeneralUser, Friend, Job
from App.database import db

def get_all_users():
    return User.query.all()

def create_user(username, password, firstName, lastName, email):
    newuser = User(username=username, password=password, firstName=firstName, lastName=lastName, email=email)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

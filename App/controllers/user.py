from App.models import User, Alumni, GeneralUser
from App.database import db


def get_all_users():
    return User.query.all()

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def create_alumni (userID, gradYear, programme, department, faculty, firstName, lastName, email):
    newAlumni= Alumni(userID=userID,gradYear=gradYear, programme=programme, department=department, faculty=faculty, firstName=firstName, lastName=lastName, email=email)
    db.session.add(newAlumni)
    db.session.commit()

def delete_alumni (userID):
    alumni= Alumni.query.filter_by(userID=userID).first()
    if not alumni:
        return (f"No alumni with userID {userID} exists")
    db.session.delete(alumni)
    db.session.commit()
    return (f"Alumni with userID {userID} deleted!")

def get_all_alumni():
    return Alumni.query.all()

def get_all_alumni_json():
    alumni = Alumni.query.all()
    if not alumni:
        return []
    alumni = [a.toDict() for a in alumni]
    return alumni

def create_generalUser(userID, company, firstName, lastName, email):
    newGeneralUser= GeneralUser(userID=userID, company=company, firstName=firstName, lastName=lastName, email=email)
    db.session.add(newGeneralUser)
    db.session.commit()

def delete_generalUser (userID):
    generalUser= GeneralUser.query.filter_by(userID=userID).first()
    if not generalUser:
        return (f"No generalUser with userID {userID} exists")
    db.session.delete(generalUser)
    db.session.commit()
    return (f"GeneralUser with userID {userID} deleted!")

def get_all_generalUsers():
    return GeneralUser.query.all()

def get_all_generalUsers_json():
    generalUsers = GeneralUser.query.all()
    if not generalUsers:
        return []
    generalUsers = [g.toDict() for g in generalUsers]
    return generalUsers 
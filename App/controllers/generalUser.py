from App.models import User, GeneralUser
from App.database import db

def create_generalUser(userID, company):
    newGeneralUser= GeneralUser(userID=userID, company=company)
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
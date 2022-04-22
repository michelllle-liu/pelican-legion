from App.models import User, Alumni
from App.database import db

def create_alumni (userID, gradYear, programme, department, faculty):
    newAlumni= Alumni(userID=userID,gradYear=gradYear, programme=programme, department=department, faculty=faculty)
    db.session.add(newAlumni)
    db.session.commit()

def delete_alumni (userID):
    alumni= Alumni.query.filter_by(userID=userID).first()
    if not alumni:
        return -1
    db.session.delete(alumni)
    db.session.commit()
    return 0

def get_all_alumni():
    return Alumni.query.all()

def get_all_alumni_json():
    alumni = Alumni.query.all()
    if not alumni:
        return []
    alumni = [a.toDict() for a in alumni]
    return alumni
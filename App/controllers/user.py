from App.models import User, Alumni, GeneralUser, Friend, Job
from App.database import db
import datetime

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

def create_alumni (userID, gradYear, programme, department, faculty):
    newAlumni= Alumni(userID=userID,gradYear=gradYear, programme=programme, department=department, faculty=faculty)
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

def create_friend (userID, friendUID):
    user= User.query.get(friendUID)
    newFriend= Friend(userID=userID, friendUID=friendUID)
    db.session.add(newFriend)
    db.session.commit()

def get_all_friends_json (userID):
    friends= Friend.query.filter_by(userID=userID)
    if not friends:
        return []
    friends = [f.toDict() for f in friends]
    return friends

def get_all_friends (userID):
    return Friend.query.filter_by(userID=userID)

def delete_friend (friendID):
    friend= Friend.query.get(friendID)
    if not friend:
        return(f'No friend with ID {friendID} exists')
    db.session.delete(friend)
    db.session.commit()
    return (f"Friend with ID {friendID} deleted!")

def delete_all_friends(userID):
    count=0
    friends=Friend.query.filter_by(userID=userID)
    if not friends:
        return ('0')
    for f in friends:
        db.session.delete(f)
        count=count+1
    db.session.commit()
    return(f'{count} friend(s) deleted!')

def create_job (userID, description, link, year, month, day):
    applicationDeadline= datetime.datetime(year, month, day)
    newJob= Job(userID=userID, description=description, link=link, applicationDeadline=applicationDeadline)
    db.session.add(newJob)
    db.session.commit()

def delete_job (jobID):
    job= Job.query.get(jobID)
    if not job:
        return (f'Job with jobID {jobID} does not exist')
    db.session.delete(job)
    db.session.commit()
    return (f'Job with jobID {jobID} deleted')

def get_user_jobs_json (userID):
    jobs= Job.query.filter_by(userID=userID)
    if not jobs:
        return []
    jobs = [j.toDict() for j in jobs]
    return jobs

def get_user_jobs (userID):
    return Job.query.filter_by(userID=userID)

def get_all_jobs_json ():
    jobs= Job.query.all()
    if not jobs:
        return []
    jobs = [j.toDict() for j in jobs]
    return jobs

def get_all_jobs():
    return Job.query.all()
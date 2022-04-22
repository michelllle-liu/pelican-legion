from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    firstName= db.Column(db.String(30), unique=False, nullable=False)
    lastName= db.Column(db.String(30), unique=False, nullable=False) 
    email= db.Column(db.String(40), unique=True, nullable=False)
    gradYear= db.Column(db.Integer, unique=False, nullable=True)
    faculty= db.Column(db.String(60), unique=False, nullable=True)
    department= db.Column(db.String(60), unique=False, nullable=True)
    programme= db.Column(db.String(60), unique=False, nullable=True)

    def __init__(self, username, password, firstName, lastName, email, gradYear, faculty, department, programme):
        self.username = username
        self.set_password(password)
        self.firstName=firstName
        self.lastName= lastName
        self.email=email
        self.gradYear=gradYear
        self.faculty=faculty
        self.department=department
        self.programme=programme

    def toDict(self):
        return{
            'id' : self.id,
            'username' : self.username,
            'firstName' : self.firstName,
            'lastName' :self.lastName,
            'email' :self.email,
            'gradYear' : self.gradYear,
            'faculty' : self.faculty,
            'department' : self.department,
            'programme' : self.programme
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Alumni (db.Model):
    alumniID= db.Column('alumniID', db.Integer, primary_key=True)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.id')) 
    gradYear= db.Column(db.Integer, unique=False, nullable=False)    
    programme= db.Column(db.String(60), unique=False, nullable=False)
    department= db.Column(db.String(60), unique=False, nullable=False)
    faculty= db.Column(db.String(60), unique=False, nullable=False)

    def toDict(self):
        return{
            'alumniID': self.alumniID,
            'gradYear': self.gradYear,
            'programme': self.programme,
            'department': self.department,
            'faculty': self.faculty
        }

class GeneralUser (db.Model):
    generalUserID= db.Column('generalUserID', db.Integer, primary_key=True)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.id')) 
    company= db.Column (db.String(80), unique=False, nullable=True) 

    def toDict(self):
        return{
            'generalUserID': self.generalUserID,
            'company': self.company
        }

class ProfilePicture (db.Model):
    picID=db.Column(db.Integer, primary_key=True)
    filename= db.Column(db.String, nullable=False)
    url=db.Column(db.String, nullable=False)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.id'))

    def __init__(self, filename, url):
        self.filename=filename
        self.url=url

class Friend (db.Model):
    friendID=db.Column(db.Integer, primary_key=True)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.id'))   
    friendUID= db.Column(db.Integer, nullable=False) 

    def toDict(self):
        return{
            'friendID':self.friendID,
            'userID':self.userID,
            'friendUID':self.friendUID
        }

class JobSpec (db.Model):
    fileID=db.Column(db.Integer, primary_key=True)
    filename= db.Column(db.String, nullable=False)
    url=db.Column(db.String, nullable=False)
    jobID= db.Column('jobID', db.Integer, db.ForeignKey('job.jobID'))

    def __init__(self, filename, url):
        self.filename=filename
        self.url=url

class Job (db.Model):
    jobID=db.Column(db.Integer, primary_key=True)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.id'))
    description= db.Column(db.String, nullable=True)
    link= db.Column(db.String, nullable=True)
    applicationDeadline= db.Column(db.DateTime, nullable=False)

    def toDict(self):
        return{
            'jobID': self.jobID,
            'userID':self.userID,
            'description': self.description,
            'link':self.link,
            'applicationDeadline':self.applicationDeadline,
        }

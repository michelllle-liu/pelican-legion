from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'userID': self.userID,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Alumni (db.Model):
    alumniID= db.Column('alumniID', db.Integer, primary_key=True)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.userID')) #Foreign Key userID
    gradYear= db.Column(db.Integer, unique=False, nullable=True)    #all made nullable to allow choice between alumni amd general account
    programme= db.Column(db.String(60), unique=False, nullable=True)
    department= db.Column(db.String(60), unique=False, nullable=True)
    faculty= db.Column(db.String(60), unique=False, nullable=True)

    firstName= db.Column(db.String(30), unique=False, nullable=True)
    lastName= db.Column(db.String(30), unique=False, nullable=True) 
    email= db.Column(db.String(40), unique=True, nullable=True) 

    def toDict(self):
        return{
            'alumniID': self.alumniID,
            'firstName':self.firstName,
            'lastName':self.lastName,
            'email':self.email,
            'gradYear': self.gradYear,
            'programme': self.programme,
            'department': self.department,
            'faculty': self.faculty
        }

class GeneralUser (db.Model):
    generalUserID= db.Column('generalUserID', db.Integer, primary_key=True)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.userID')) #Foreign Key userID
    company= db.Column (db.String(80), unique=False, nullable=True) #all made null to allow choice between alumni amd general account

    firstName= db.Column(db.String(30), unique=False, nullable=True)
    lastName= db.Column(db.String(30), unique=False, nullable=True) 
    email= db.Column(db.String(40), unique=True, nullable=True) 

    def toDict(self):
        return{
            'generalUserID': self.generalUserID,
            'firstName':self.firstName,
            'lastName':self.lastName,
            'email':self.email,
            'company': self.company
        }

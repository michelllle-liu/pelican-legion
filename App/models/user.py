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
    alumni= db.relationship('Alumni', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, firstName, lastName, email, alumni):
        self.username = username
        self.set_password(password)
        self.firstName=firstName
        self.lastName= lastName
        self.email=email
        self.alumni=alumni

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'firstName': self.firstName,
            'lastName':self.lastName,
            'email':self.email,
            'alumni': [alumni.toDict() for alumni in self.alumni],
            'alumni_programme':[alumni.toDict()['programme'] for alumni in self.alumni]
            
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


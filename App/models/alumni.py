from App.database import db

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
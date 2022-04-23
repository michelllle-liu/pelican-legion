from App.database import db

class Job (db.Model):
    jobID = db.Column(db.Integer, primary_key=True)
    userID = db.Column('userID', db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    deadline= db.Column(db.DateTime, nullable=True)

    def toDict(self):
        return{
            'jobID': self.jobID,
            'userID':self.userID,
            'title':self.title,
            'description': self.description,
            'deadline':self.deadline,
        }

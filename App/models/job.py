from App.database import db

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

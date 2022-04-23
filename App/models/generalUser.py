from App.database import db

class GeneralUser (db.Model):
    generalUserID= db.Column('generalUserID', db.Integer, primary_key=True)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.id')) 
    company= db.Column (db.String(80), unique=False, nullable=True) 

    def toDict(self):
        return{
            'generalUserID': self.generalUserID,
            'company': self.company
        }
from App.database import db

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
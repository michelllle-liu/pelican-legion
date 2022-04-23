from App.database import db

class ProfilePicture (db.Model):
    picID=db.Column(db.Integer, primary_key=True)
    filename= db.Column(db.String, nullable=False)
    url=db.Column(db.String, nullable=False)
    userID= db.Column('userID', db.Integer, db.ForeignKey('user.id'))

    def __init__(self, filename, url):
        self.filename=filename
        self.url=url
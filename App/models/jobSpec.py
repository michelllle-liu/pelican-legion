from App.database import db

class JobSpec (db.Model):
    fileID=db.Column(db.Integer, primary_key=True)
    filename= db.Column(db.String, nullable=False)
    url=db.Column(db.String, nullable=False)
    jobID= db.Column('jobID', db.Integer, db.ForeignKey('job.jobID'))

    def __init__(self, filename, url):
        self.filename=filename
        self.url=url
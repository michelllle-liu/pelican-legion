from App.models import User, Job
from App.database import db
import datetime

def create_job (userID, description, link, year, month, day):
    y= int(year)
    m= int (month)
    d= int (day)
    applicationDeadline= datetime.date(y, m, d)
    newJob= Job(userID=userID, description=description, link=link, applicationDeadline=applicationDeadline)
    db.session.add(newJob)
    db.session.commit()

def delete_job (jobID):
    job= Job.query.get(jobID)
    if not job:
        return (f'Job with jobID {jobID} does not exist')
    db.session.delete(job)
    db.session.commit()
    return (f'Job with jobID {jobID} deleted')

def get_user_jobs_json (userID):
    jobs= Job.query.filter_by(userID=userID)
    if not jobs:
        return []
    jobs = [j.toDict() for j in jobs]
    return jobs

def get_user_jobs (userID):
    return Job.query.filter_by(userID=userID)

def get_all_jobs_json ():
    jobs= Job.query.all()
    if not jobs:
        return []
    jobs = [j.toDict() for j in jobs]
    return jobs

def get_all_jobs():
    return Job.query.all()
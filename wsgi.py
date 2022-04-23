import click
from flask import Flask
from flask.cli import with_appcontext

from App.database import create_db
from App.main import app, migrate
from App.controllers import ( 
    create_user, 
    get_all_users_json, 
    create_alumni, 
    delete_user,
    get_all_alumni_json, 
    create_generalUser, 
    get_all_generalUsers_json,
    delete_alumni,
    delete_generalUser,
    create_friend,
    get_all_friends_json,
    delete_friend,
    delete_all_friends,
    create_job,
    delete_job,
    get_user_jobs_json,
    get_all_jobs_json
)

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("create-user")
def create_user_command():
    username=input('Enter a username: ')
    password=input('Enter a password: ')
    firstName=input('Enter a firstName: ')
    lastName=input('Enter a lastName: ')
    email=input('Enter an email: ')
    create_user(username, password, firstName, lastName, email)
    print(f'{username} created!')

@app.cli.command("get-users")
def get_users():
    print(get_all_users_json())

@app.cli.command("delete-user")
def delete_user_command():
    id=input('Enter a user ID: ')
    message= delete_user(id);
    print(message);

@app.cli.command("create-alumni")   
def create_alumni_command():
    userID= input ('Enter a userID: ')
    gradYear= input('Enter a gradYear: ')
    programme= input('Enter a programme: ')
    department= input('Enter a department: ')
    faculty= input('Enter a faculty: ')
    create_alumni (userID,gradYear, programme, department, faculty)
    print ('Alumni created!')

@app.cli.command("get-alumni")
def get_all_alumni ():
    print(get_all_alumni_json())

@app.cli.command("delete-alumni")
def delete_alumni_command():
    userID= input ('Enter a userID: ')
    message= delete_alumni (userID)
    print (message)

@app.cli.command("create-generalUser")
def create_generalUser_command ():
    userID= input ('Enter a userID: ')
    company= input('Enter a company: ')
    create_generalUser (userID, company)
    print ('General User created!')

@app.cli.command("get-generalUsers")
def get_all_generalUsers ():
    print(get_all_generalUsers_json())

@app.cli.command("delete-generalUser")
def delete_generalUser_command():
    userID= input ('Enter a userID: ')
    message= delete_generalUser (userID)
    print (message)

@app.cli.command("create-friend")
def create_friend_command():
    userID= input ('Enter a userID: ')
    friendUID= input ('Enter a friendUID: ')
    create_friend(userID, friendUID)
    print('Friend created!')

@app.cli.command("get-friends")
def get_all_friends_command ():
    userID= input ('Enter a userID: ')
    print (get_all_friends_json(userID))

@app.cli.command("delete-friend")
def delete_friend_command():
    friendID= input ('Enter a friendID: ')
    message=delete_friend(friendID)
    print(message)

@app.cli.command("delete-all-friends")
def delete_all_friends_command():
    userID= input ('Enter a userID: ')
    message=delete_all_friends(userID)
    print(message)

@app.cli.command("create-job")
def create_job_command():
    userID= input ('Enter a userID: ')
    description= input ('Enter a description: ')
    link= input ('Enter a link: ')
    year= input ('Enter an applicationDeadline Year: ')
    month= input ('Enter an applicationDeadline Month: ')
    day= input ('Enter an applicationDeadline Day: ')
    create_job(userID, description, link, year, month, day)
    print('Job created!')

@app.cli.command("delete-job")
def delete_job_command():
    jobID= input ('Enter a jobID: ')
    message= delete_job(jobID)
    print (message)

@app.cli.command("get-user-jobs")
def get_user_jobs_command():
    userID= input ('Enter a userID: ')
    print(get_user_jobs_json(userID))

@app.cli.command("get-all-jobs")
def get_all_jobs_command():
    print(get_all_jobs_json())

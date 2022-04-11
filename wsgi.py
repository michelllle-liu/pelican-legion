import click
from flask import Flask
from flask.cli import with_appcontext

from App.database import create_db
from App.main import app, migrate
from App.controllers import ( 
    create_user, 
    get_all_users_json, 
    create_alumni, 
    get_all_alumni_json, 
    create_generalUser, 
    get_all_generalUsers_json,
    delete_alumni,
    delete_generalUser
)


@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

@app.cli.command("get-users")
def get_users():
    print(get_all_users_json())

@app.cli.command("create-alumni")   
def create_alumni_command():
    userID= input ('Enter a userID: ')
    gradYear= input('Enter a gradYear: ')
    programme= input('Enter a programme: ')
    department= input('Enter a department: ')
    faculty= input('Enter a faculty: ')
    firstName= input('Enter a firstName: ')
    lastName= input('Enter a lastName: ')
    email= input('Enter an email: ')
    create_alumni (userID,gradYear, programme, department, faculty, firstName, lastName, email)
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
    firstName= input('Enter a firstName: ')
    lastName= input('Enter a lastName: ')
    email= input('Enter an email: ')
    create_generalUser (userID, company, firstName, lastName, email)
    print ('General User created!')

@app.cli.command("get-generalUsers")
def get_all_generalUsers ():
    print(get_all_generalUsers_json())

@app.cli.command("delete-generalUser")
def delete_generalUser_command():
    userID= input ('Enter a userID: ')
    message= delete_generalUser (userID)
    print (message)
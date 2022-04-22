from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField, RadioField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms.fields import DateField

class SignUp(FlaskForm):
    firstName = StringField('First Name', validators=[InputRequired()])
    lastName = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Create Account', render_kw={'type' : 'submit', 'class' : 'col s12 btn btn-large waves-effect waves-light indigo'})

class LogIn(FlaskForm):
    username = StringField('Enter your username', validators=[InputRequired()])
    password = PasswordField('Enter your password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'type' : 'submit', 'class' : 'col s12 btn btn-large waves-effect waves-light indigo'})

    
class NewJob(FlaskForm):
    JobTitle = StringField('Job Title', validators=[InputRequired()])
    JobDescrip = StringField('Job Description') 
    appDeadline = DateField('Deadline for Application')
    add = SubmitField('Add Job', render_kw={'type' : 'submit', 'class' : 'col s12 btn btn-large waves-effect waves-light indigo'})
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField, RadioField, DateField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange, EqualTo, Email

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

class AlumnusInfo(FlaskForm):
    gradYear = IntegerField('Graduation Year', validators=[NumberRange(min=0, max=4)])
    faculty = StringField('Faculty')
    department = StringField('Department')
    programme = StringField('Programme')
    save = SubmitField('Save', render_kw={'type' : 'submit', 'class' : 'col s12 btn btn-large waves-effect waves-light indigo'})
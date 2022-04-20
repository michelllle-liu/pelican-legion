from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email

class SignUp(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

class LogIn(FlaskForm):
    username = StringField('Enter your username', validators=[InputRequired()])
    password = PasswordField('Enter your password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'type' : 'submit', 'class' : 'col s12 btn btn-large waves-effect waves-light indigo'})
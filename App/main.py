import os
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_jwt import JWT, jwt_required, current_identity
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta, datetime

from App.models.user import db, User
from App.models.alumni import db, Alumni
from App.models.job import db, Job

from App.forms import LogIn, SignUp, AlumnusInfo, NewJob

from App.database import init_db, create_db, get_migrate

from App.controllers import (
    setup_jwt
)

from App.views import (
    user_views,
    api_views
)

views = [
    user_views,
    api_views
]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        # app.config['DBURI'] = "postgresql://iyvpyncuikxtmm:748440c014d5f7ef36a34bdb6c760242e8a47224975631a0c07edcb9ee057710@ec2-54-80-122-11.compute-1.amazonaws.com:5432/dbt01ad2m2e482"
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] =  timedelta(days=int(os.environ.get('JWT_EXPIRATION_DELTA')))
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
    for key, value in config.items():
        app.config[key] = config[key]

'''Begin Flask Login Functions'''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
'''End Flask Login Functions'''

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app, views)
    create_db(app)
    login_manager.init_app(app)
    setup_jwt(app)
    app.app_context().push()
    return app

app = create_app()
# db.drop_all()
# db.create_all()
migrate = get_migrate(app)

''' Set up JWT here '''

def authenticate(uname, password):
  user = User.query.filter_by(username=uname).first()
  if user and user.check_password(password):
    return user

def identity(payload):
  return User.query.get(payload['identity'])

jwt = JWT(app, authenticate, identity)    # auto creates /auth route

''' End JWT Setup '''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    form = LogIn()
    return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def loginAction():
    form = LogIn()
    if form.validate_on_submit():
        data = request.form
        user = User.query.filter_by(username = data['username']).first()
        if user and user.check_password(data['password']):
            flash('Logged in successfully.')
            login_user(user)
            return redirect(url_for('dashboard'))
    flash('Invalid credentials.')
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out!')
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET'])
def show_signup():
    form = SignUp()
    return render_template('signup.html', form=form)

@app.route('/signup', methods=['POST'])
def signupAction():
    form = SignUp()
    if form.validate_on_submit():
        user_data = request.form

        # checking if user already exists

        old_user = User.query.filter_by(username=user_data['username']).first()

        if not old_user:
            old_user = User.query.filter_by(email=user_data['email']).first()
  
        if old_user:
            flash('This username or email is already in use')
            return redirect(url_for('show_signup'))
  
        # if username or email does not already exist
        new_user = User(firstName=user_data['firstName'], lastName=user_data['lastName'], username=user_data['username'], email=user_data['email'], password=user_data['password'])
        # new_user.set_password(user_data['password'])    # hashing password

        db.session.add(new_user)
        db.session.commit()
        flash('Account created!')
        return redirect(url_for('login'))
    flash('Error: Invalid input')
    return redirect(url_for('/dashboard'))

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    alumnus_info = Alumni.query.filter_by(userID=current_user.id).first()

    if not alumnus_info:
        alumnus_info = Alumni(userID=current_user.id, gradYear=None, faculty=None, department=None, programme=None)

    return render_template('dashboard.html', current_user=current_user, alumnus_info=alumnus_info)

"""
@app.route('/alumni')
@login_required
def show_alumni():
    return render_template('alumni.html')
"""

@app.route('/jobs')
@login_required
def show_jobs():
    jobs = Job.query.all()

    if jobs is None:
        jobs = []     # if there are no jobs, pass an empty list
    
    return render_template('jobs.html', jobs=jobs, current_user=current_user)

@app.route('/jobs/<jobID>', methods=['GET', 'DELETE'])
@login_required
def delete_job(jobID):
    job = Job.query.filter_by(jobID=jobID).first()
    if job:
        db.session.delete(job)
        db.session.commit()
        flash('Job deleted')
    return redirect(url_for('show_jobs'))

@app.route('/addjob', methods=['GET'])               #added form to get new job to board
@login_required
def show_jobform():
    form = NewJob()
    return render_template('newjob.html', form=form)

@app.route('/addjob', methods=['POST'])
@login_required
def addJobAction():
    form = NewJob()
    data = request.form

    new_job = Job(userID=current_user.id, title=data['title'], description=None, deadline=None)

    if 'description' in data:
        new_job.description = data['description']
    if ('deadline' in data) and (data['deadline'] != ''):
        new_job.deadline = datetime.strptime(data['deadline'], '%Y-%m-%d %H:%M:%S')
    
    db.session.add(new_job)
    db.session.commit()
    flash('Job has been added to the Job Board!')
    return redirect(url_for('show_jobs'))

@app.route('/editProfile', methods=['GET'])
@login_required
def editProfile():
    form = AlumnusInfo()
    alumnus_info = Alumni.query.filter_by(userID=current_user.id).first()

    return render_template('editProfile.html', form=form, alumnus_info=alumnus_info)

@app.route('/editProfile', methods=['POST'])
@login_required
def editProfileAction():
    form = SignUp()
    data = request.form
    alumnus_info = Alumni.query.filter_by(userID=current_user.id).first()

    if not alumnus_info:
        alumnus_info = Alumni(userID=current_user.id, gradYear=None, faculty=None, department=None, programme=None)

    if 'gradYear' in data:
        alumnus_info.gradYear = data['gradYear']
    if 'faculty' in data:
        alumnus_info.faculty = data['faculty']
    if 'department' in data:
        alumnus_info.department = data['department']
    if 'programme' in data:
        alumnus_info.programme = data['programme']

    db.session.add(alumnus_info)
    db.session.commit()
    flash('Your profile has been updated!')
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

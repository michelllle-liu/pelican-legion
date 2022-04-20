#hello 
#hello again
#TESTING 123
import os
from flask import Flask, render_template
from flask_jwt import JWT, jwt_required, current_identity
from flask_login import LoginManager, current_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta


from App.database import init_db, get_migrate

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
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] =  timedelta(days=int(os.environ.get('JWT_EXPIRATION_DELTA')))
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
    for key, value in config.items():
        app.config[key] = config[key]

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
    init_db(app)
    setup_jwt(app)
    app.app_context().push()
    return app

app = create_app()
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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def show_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    user_data = request.get_json()    # receives new user data from the post request, i.e. the body

    # checking if user already exists

    old_user = User.query.filter_by(username=user_data['username']).first()

    if not old_user:
        old_user = User.query.filter_by(email=user_data['email']).first()
  
    if old_user:
        return 'username or email already exists'
  
    # if username or email does not already exist
    new_user = User(username=user_data['username'], email=user_data['email'])
    new_user.set_password(user_data['password'])    # hashing password

    db.session.add(new_user)
    db.session.commit()

    return 'user created'

@app.route('/dashboard')
# @jwt_required()
def show_dashboard():
    return render_template('dashboard.html')

@app.route('/alumni')
def show_alumni():
    return render_template('alumni.html')

@app.route('/jobs')
def show_jobs():
    return render_template('jobs.html')
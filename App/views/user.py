from flask import Blueprint, render_template, jsonify, request, send_from_directory, redirect, flash, url_for
from flask_jwt import JWT, jwt_required, current_identity

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    delete_user,
    get_all_alumni_json
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/alumni')
def client_app():
    users = get_all_users_json()
    return render_template('alumni.html', users=users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/users/delete', methods=['DELETE'])
@jwt_required()
def delete_user_account():
    message=delete_user(id=current_identity.id)
    flash(message)
    return redirect(url_for('show_signup'))


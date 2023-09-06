from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from main.models import User
from main import db

import bcrypt


def check_user(id):
    student = User.query.filter_by(id=id).all()
    if len(student) == 0:
        return True


def get_all_users():
    user = User.query.all()
    user_list = []
    for i in user:
        user_info = {
            'name': i.name,
            'gender': i.gender,
            'age': i.birth,
            'belong': i.belong,
            'local': i.local,
            'point': i.point,
            'rival_id': i.rival_id
        }
        user_list.append(user_info)
    return user_list


def get_users(id):
    user = User.query.filter_by(id=id).first()
    user_info = {
        'name': user.name,
        'gender': user.gender,
        'age': user.birth,
        'belong': user.belong,
        'local': user.local,
        'point': user.point,
        'rival_id': user.rival_id
    }
    return user_info


def get_pw(id):
    student = User.query.filter_by(id=id).first()
    return student.passwd


def pw_check(get_passwd, save_passwd):
    return bcrypt.checkpw(get_passwd.encode('utf-8'), save_passwd.encode('utf-8'))


def sign_up(user_info):
    sign_std = User(id=user_info['id'],
                    name=user_info['name'],
                    birth=user_info['birth'],
                    belong=user_info['belong'],
                    gender=user_info['gender'],
                    local=user_info['local'],
                    rival_id=user_info['rival_id'],
                    passwd=user_info['passwd'],
                    join_date=user_info['join_date'],
                    login_token=user_info['token'])
    db.session.add(sign_std)
    db.session.commit()
    return 'Success'


def insert_token(id, token):
    student_to_update = User.query.filter_by(id=id).first()

    if student_to_update:
        student_to_update.login_token = token

        db.session.commit()

        return 'Succes'
    else:
        return 'Fail'


def delete_token(id):
    student_to_update = User.query.filter_by(id=id).first()

    if student_to_update:
        student_to_update.login_token = None

        db.session().commit()

        return 'Succes'
    else:
        return 'Fail'


def resign_user(id):
    student_to_resign = User.query.filter_by(id=id).first()

    if student_to_resign:
        db.session().delete(student_to_resign)
        db.session().commit()

        return 'Succes'
    else:
        return 'Fail'


def user_validation():
    def user_auth_decorator(f):
        @wraps(f)
        @jwt_required(locations=["cookies"], optional=True)
        def _user_auth_decorator(*args, **kwargs):
            current_user_id = get_jwt_identity()
            if not current_user_id:
                return {'status': 'Authentication failed'}
            return f(*args, **kwargs)

        return _user_auth_decorator

    return user_auth_decorator

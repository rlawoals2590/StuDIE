from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from main.models import User
from main import db

import bcrypt


def get_users(stid):
    student = User.query.filter_by(stid=stid).all()
    if len(student) == 0:
        return True


def get_pw(stid, name, belong):
    student = User.query.filter_by(stid=stid, name=name, belong=belong).first()
    return student.passwd


def pw_check(get_passwd, save_passwd):
    return bcrypt.checkpw(get_passwd.encode('utf-8'), save_passwd.encode('utf-8'))


def sign_up(user_info):
    sign_std = User(id=user_info['id'],
                    stid=user_info['stid'],
                    name=user_info['name'],
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


def insert_token(stid, belong, token):
    student_to_update = User.query.filter_by(stid=stid, belong=belong).first()

    if student_to_update:
        student_to_update.login_token = token

        db.session.commit()

        return 'Succes'
    else:
        return 'Fail'


def delete_token(stid, belong):
    student_to_update = User.query.filter_by(stid=stid, belong=belong).first()

    if student_to_update:
        student_to_update.login_token = None

        db.session().commit()

        return 'Succes'
    else:
        return 'Fail'


def resign_user(stid, belong):
    student_to_resign = User.query.filter_by(stid=stid, belong=belong).first()

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
                result = '''
                        잘못된 접근입니다.
                    '''
                return result
            return f(*args, **kwargs)

        return _user_auth_decorator

    return user_auth_decorator

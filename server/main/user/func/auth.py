from main.models import Student
from main import db


def get_users(stid):
    student = Student.query.filter_by(stid=stid).all()
    if len(student) == 0:
        return True


def sign_up(user_info):
    sign_std = Student(stid=user_info['stid'],
                       passwd=user_info['passwd'],
                       name=user_info['name'],
                       gender=user_info['gender'],
                       school=user_info['school'],
                       local=user_info['local'],
                       join_date=user_info['join_date'],
                       rival=user_info['rival'],
                       login_token=user_info['token'])
    db.session.add(sign_std)
    db.session.commit()
    return True

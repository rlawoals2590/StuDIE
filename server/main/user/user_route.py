from datetime import datetime

from flask import Blueprint, request

from main.models import Student

from .func.user_model import Model
from .func.auth import get_users, sign_up

user_route = Blueprint("user_route", __name__, url_prefix='/user')


@user_route.route('/list/')
def _list():
    # student_list = Student.query.order_by(Student.join_date.desc())

    return 'list'


@user_route.route('/detail/<int:stid>/')
def detail(stid):
    student = Student.query.get_or_404(stid)
    return student.name


@user_route.route('/register/', methods=['POST'])
def register():
    stid = request.form['stid']
    passwd = request.form['passwd']
    name = request.form['name']
    gender = request.form['gender']
    school = request.form['school']
    local = request.form['local']
    rival = request.form['rival']

    if get_users(stid):
        student_info = Model(stid=stid, passwd=passwd, name=name, gender=gender, school=school, local=local, rival=rival)
        return sign_up(student_info.user_model())
    else:
        return f'''
                    <script>
                        alert('{name}님은 이미 등록되어있습니다.')
                        location.href = '/user/list/'
                    </script>
                '''

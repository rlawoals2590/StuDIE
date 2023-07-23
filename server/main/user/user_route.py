from flask_jwt_extended import create_access_token, get_jwt

from flask import Blueprint, request, make_response, redirect, session
from markupsafe import escape

from main.models import Student

from .func.user_model import Model
from .func.auth import get_users, get_pw, sign_up, pw_check, insert_token, user_validation, delete_token

user_route = Blueprint("user_route", __name__, url_prefix='/user')
jwt_blocklist = set()


@user_route.route('/')
@user_validation()
def index():
    return 'test'


@user_route.route('/detail/<int:stid>/')
def detail(stid):
    student = Student.query.get_or_404(stid)
    print(student)
    return student.name


@user_route.route('/register/', methods=['POST'])
def register():
    stid = request.form['stid']
    passwd = request.form['passwd']
    name = request.form['name']
    gender = request.form['gender']
    school = request.form['school']
    local = request.form['local']

    if get_users(stid):
        student_info = Model(stid=stid, passwd=passwd, name=name, gender=gender, school=school, local=local)
        return sign_up(student_info.user_model())
    else:
        return f'''
                    <script>
                        alert('{name}님은 이미 등록되어있습니다.')
                        location.href = '/user/'
                    </script>
                '''


@user_route.route('/login/', methods=['POST'])
def login():
    stid = request.form['stid']
    get_passwd = request.form['passwd']
    name = request.form['name']
    school = request.form['school']

    if not get_users(stid):
        save_passwd = get_pw(stid, name, school)
        if pw_check(get_passwd, save_passwd):
            access_token = create_access_token(identity=stid)
            resp = make_response(redirect('/user/'))
            resp.set_cookie('user_access_token', access_token)
            insert_token(stid, school, access_token)
            session['stid'] = stid
            session['school'] = school
            return resp
        else:
            return '아이디 및 비밀번호 틀림'
    else:
        return '존재하지 않는 학생'


@user_route.route('/logout/')
@user_validation()
def logout():
    delete_token(escape(session['stid']), escape(session['school']))
    session.pop('stid', None)
    session.pop('school', None)

    token = get_jwt()
    jti = token['jti']
    jwt_blocklist.add(jti)

    resp = make_response('''
                        로그아웃을 성공하였습니다! <a href='/user/'>홈으로</a>이동하세요!
                    ''')
    resp.set_cookie('user_access_token', '', expires=0)  # 쿠키 만료 시간을 0으로 설정하여 삭제

    return resp

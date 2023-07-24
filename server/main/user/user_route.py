from flask_jwt_extended import create_access_token, get_jwt

from flask import Blueprint, request, make_response, redirect, session
from markupsafe import escape

from .func.user_model import Model
from .func.auth import get_users, get_pw, sign_up, pw_check, insert_token, \
    user_validation, delete_token, resign_user

user_route = Blueprint("user_route", __name__, url_prefix='/user')
jwt_blocklist = set()


@user_route.route('/')
@user_validation()
def index():
    return 'test'


@user_route.route('/register/', methods=['POST'])
def register():
    stid = request.form['stid']
    passwd = request.form['passwd']
    name = request.form['name']
    gender = request.form['gender']
    belong = request.form['belong']
    local = request.form['local']

    if get_users(stid):
        student_info = Model(stid=stid, name=name, belong=belong, gender=gender, local=local, passwd=passwd)
        return sign_up(student_info.user_model())
    else:
        return '이미 등록된 유저입니다.'


@user_route.route('/login/', methods=['POST'])
def login():
    stid = request.form['stid']
    get_passwd = request.form['passwd']
    name = request.form['name']
    belong = request.form['belong']

    if not get_users(stid):
        save_passwd = get_pw(stid, name, belong)
        if pw_check(get_passwd, save_passwd):
            access_token = create_access_token(identity=stid)
            resp = make_response(redirect('/user/'))
            resp.set_cookie('user_access_token', access_token)
            insert_token(stid, belong, access_token)
            session['stid'] = stid
            session['belong'] = belong
            return resp
        else:
            return '아이디 및 비밀번호 틀림'
    else:
        return '존재하지 않는 학생'


@user_route.route('/logout/')
@user_validation()
def logout():
    delete_token(escape(session['stid']), escape(session['belong']))
    session.pop('stid', None)
    session.pop('belong', None)

    token = get_jwt()
    jti = token['jti']
    jwt_blocklist.add(jti)

    resp = make_response('''
                        로그아웃을 성공하였습니다!
                    ''')
    resp.set_cookie('user_access_token', '', expires=0)  # 쿠키 만료 시간을 0으로 설정하여 삭제

    return resp


@user_route.route('/resign/')
@user_validation()
def resign():
    resign_user(escape(session['stid']), escape(session['belong']))
    session.pop('stid', None)
    session.pop('belong', None)

    token = get_jwt()
    jti = token['jti']
    jwt_blocklist.add(jti)

    resp = make_response('''
                        회원 탈퇴가 성공하였습니다!
                    ''')
    resp.set_cookie('user_access_token', '', expires=0)  # 쿠키 만료 시간을 0으로 설정하여 삭제

    return resp



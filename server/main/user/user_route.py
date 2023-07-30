from flask_jwt_extended import create_access_token, get_jwt

from flask import request, make_response, session, jsonify
from markupsafe import escape
from flask_restx import Resource, Namespace, fields

from .func.user_model import Model
from .func.auth import get_users, get_pw, sign_up, pw_check, insert_token, \
    user_validation, delete_token, resign_user, check_user


user_api = Namespace('user_api')
jwt_blocklist = set()


user_login = user_api.model('user_api', strict=True, model={
    'id': fields.String(title='아이디', default='abcde1234', required=True),
    'passwd': fields.String(title='비밀번호', default='Abcd@1234', required=True),
})


@user_api.route('/')
class Index(Resource):
    @user_validation()
    def get(self):
        return {'status': 'user'}


@user_api.route('/get_users/<string:id>/')
class OtherUsers(Resource):
    # @user_validation()
    def get(self, id=None):
        if id is None:
            print('test')
            return 'test'
        return jsonify(get_users(id))


@user_api.route('/get_users/')
class Users(Resource):
    # @user_validation()
    def get(self):
        id = escape(session['id'])
        return jsonify(get_users(id))


@user_api.route('/register/')
class Register(Resource):
    @user_api.expect(user_api.model('user register', {
            'id': fields.String(title='아이디', default='abcde1234', required=True),
            'passwd': fields.String(title='비밀번호', default='Abcd@1234', required=True),
            'name': fields.String(title='이름', default='홍길동', required=True),
            'birth': fields.Date(title='생년', default='2005', required=True),
            'gender': fields.Integer(title='성별', default=0, required=True),
            'belong': fields.String(title='소속', default='세명컴퓨터고등학교', required=True),
            'local': fields.String(title='지역', default='서울', required=True),
            'vision': fields.String(title='목표', default='서울대 가기', required=True),
    }))
    def post(self):
        id = request.json.get('id')
        passwd = request.json.get('passwd')
        name = request.json.get('name')
        birth = request.json.get('birth')
        gender = request.json.get('gender')
        belong = request.json.get('belong')
        local = request.json.get('local')
        vision = request.json.get('vision')

        if check_user(id):
            student_info = Model(id=id, name=name, birth=birth, belong=belong, gender=gender, local=local, passwd=passwd, vision=vision)
            return sign_up(student_info.user_model())
        else:
            return {'status': 'Registration failed'}


@user_api.route('/login/')
class Login(Resource):
    @user_api.expect(user_api.model('user login', {
        'id': fields.String(title='아이디', default='abcde1234', required=True),
        'passwd': fields.String(title='비밀번호', default='Abcd@1234', required=True),
    }))
    def post(self):
        # id = request.form['id']
        # get_passwd = request.form['passwd']

        id = request.json.get('id')
        get_passwd = request.json.get('passwd')

        if not check_user(id):
            save_passwd = get_pw(id)
            if pw_check(get_passwd, save_passwd):
                access_token = create_access_token(identity=id)
                resp = make_response({'status': 'Success'})
                resp.set_cookie('user_access_token', access_token)
                insert_token(id, access_token)
                session['id'] = id
                return resp
            else:
                return {'status': 'Login failed (ID and password incorrect)'}
        else:
            return {'status': 'Login failed (User without)'}


@user_api.route('/logout/')
class Logout(Resource):
    @user_validation()
    def get(self):
        delete_token(escape(session['id']))
        session.pop('id', None)

        token = get_jwt()
        jti = token['jti']
        jwt_blocklist.add(jti)

        resp = make_response({'status': 'Success'})
        resp.set_cookie('user_access_token', '', expires=0)  # 쿠키 만료 시간을 0으로 설정하여 삭제

        return resp


@user_api.route('/resign')
class Resign(Resource):
    @user_validation()
    def get(self):
        resign_user(escape(session['id']))
        session.pop('id', None)

        token = get_jwt()
        jti = token['jti']
        jwt_blocklist.add(jti)

        resp = make_response({'status': 'Success'})
        resp.set_cookie('user_access_token', '', expires=0)  # 쿠키 만료 시간을 0으로 설정하여 삭제

        return resp



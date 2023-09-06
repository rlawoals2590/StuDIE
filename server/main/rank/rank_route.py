from flask import jsonify, session
from main.models import User
from flask_restx import Resource, Namespace
from markupsafe import escape

from .func.ranking import local_ranking, belong_ranking, personal_ranking, user_ranking
from ..user.func.auth import user_validation

rank_api = Namespace('rank_api')


@rank_api.route('/')
class Index(Resource):
    @user_validation()
    def get(self):
        return {'status': 'rank'}


@rank_api.route('/local/')
class Local(Resource):
    @user_validation()
    def get(self):
        return jsonify(local_ranking(User.local, User.point, User.id))


@rank_api.route('/belong/')
class Belong(Resource):
    @user_validation()
    def get(self):
        return jsonify(belong_ranking(User.belong, User.point, User.id))


@rank_api.route('/personal/')
class Personal(Resource):
    @user_validation()
    def get(self):
        return jsonify(personal_ranking(User.name, User.point, User.id))


@rank_api.route('/ranking/')
class UserRanking(Resource):
    @user_validation()
    def get(self):
        id = escape(session['id'])

        return user_ranking(User.name, User.point, User.id, id)

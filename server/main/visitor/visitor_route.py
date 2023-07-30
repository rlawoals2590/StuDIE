from flask import jsonify
from main import db
from main.models import User
from sqlalchemy import func
from flask_restx import Resource, Namespace

from ..user.func.auth import user_validation

visitor_api = Namespace('visitor_api')


@visitor_api.route('/count/')
class Visitor(Resource):
    @user_validation()
    def get(self):
        result = db.session().query(func.count(User.id)).filter(User.login_token.isnot(None)).all()
        return jsonify({'count': result[0][0]})

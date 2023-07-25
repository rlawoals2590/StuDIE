from flask import Blueprint, jsonify
from main import db
from main.models import User, Point
from sqlalchemy import func

visitor_route = Blueprint("visitor_route", __name__, url_prefix='/visitor')


@visitor_route.route('/count/')
def visitor():
    result = db.session().query(func.count(User.id)).filter(User.login_token.isnot(None)).all()
    return jsonify({'count': result[0][0]})
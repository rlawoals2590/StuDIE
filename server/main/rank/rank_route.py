from flask import Blueprint, jsonify
from main.models import User, Point

from .func.ranking import local_ranking, belong_ranking, personal_ranking

rank_route = Blueprint("rank_route", __name__, url_prefix='/rank')


@rank_route.route('/')
def index():
    return 'rank index'


@rank_route.route('/local/')
def local():
    return jsonify(local_ranking(User.local, Point.point, User.id, Point.id))


@rank_route.route('/belong/')
def belong():
    return jsonify(belong_ranking(User.belong, Point.point, User.id, Point.id))


@rank_route.route('/personal/')
def personal():
    return jsonify(personal_ranking(User.name, Point.point, User.id, Point.id))
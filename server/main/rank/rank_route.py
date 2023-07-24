from flask import Blueprint
from main.models import User, Point
from main import db
from sqlalchemy import func

rank_route = Blueprint("rank_route", __name__, url_prefix='/rank')


@rank_route.route('/')
def index():
    return 'rank index'

# @rank_route.route('/')


@rank_route.route('/personal/')
def personal():
    local_rank = db.session().query(User.name, func.max(Point.point)).filter(User.id == Point.id).first()
    return local_rank[0]
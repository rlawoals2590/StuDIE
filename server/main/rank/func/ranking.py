from main import db
from sqlalchemy import func
from main.models import User


def sum_rank_over(point):
    rank_over = func.rank().over(order_by=func.sum(point).desc()).label('rank')
    return rank_over


def local_ranking(local, point, user_id):
    result = db.session().query(local, func.sum(point), sum_rank_over(point)).filter(id == user_id).group_by(local).all()
    local_rank = [[i[2], i[0]] for i in result]

    return local_rank


def belong_ranking(belong, point, user_id):
    result = db.session().query(belong, func.sum(point), sum_rank_over(point)).filter(id == user_id).group_by(belong).all()
    belong_rank = [[i[2], i[0]] for i in result]

    return belong_rank


def personal_ranking(name, point, user_id):
    rank_over = func.rank().over(order_by=point.desc()).label('rank')
    result = User.query.with_entities(name, point, rank_over).filter(id == user_id).all()
    personal_rank = [[i[2], i[0]] for i in result]

    return personal_rank

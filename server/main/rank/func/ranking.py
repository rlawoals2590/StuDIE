from sqlalchemy import func
from main.models import User
import numpy as np


def sum_rank_over(point):
    rank_over = func.rank().over(order_by=func.sum(point).desc()).label('rank')
    return rank_over


def local_ranking(local, point, user_id):
    result = User.query.with_entities(local, func.sum(point), sum_rank_over(point)).filter(User.id == user_id).group_by(local).limit(30).all()
    local_rank = [[i[2], i[0]] for i in result]
    dict_blocal_rank = []

    for i in local_rank:
        dict_blocal_rank.append({'name': i[1], 'ranking': i[0]})

    return dict_blocal_rank


def belong_ranking(belong, point, user_id):
    result = User.query.with_entities(belong, func.sum(point), sum_rank_over(point)).filter(User.id == user_id).group_by(belong).limit(30).all()
    belong_rank = [[i[2], i[0]] for i in result]
    dict_belong_rank = []

    for i in belong_rank:
        dict_belong_rank.append({'name': i[1], 'ranking': i[0]})

    return dict_belong_rank


def personal_ranking(point, user_id):
    rank_over = func.rank().over(order_by=point.desc()).label('rank')
    result = User.query.with_entities(user_id, point, rank_over).filter(User.id == user_id).limit(30).all()
    personal_rank = [[i[2], i[0]] for i in result]
    dict_personal_rank = []

    for i in personal_rank:
        dict_personal_rank.append({'id': i[1], 'ranking': i[0]})

    return dict_personal_rank


def user_ranking(user_point, user_id, id):
    user_info = User.query.filter_by(id=id).first()
    id = user_info.id

    rank_over = func.rank().over(order_by=user_point.desc()).label('rank')
    result = User.query.with_entities(user_id, user_point, rank_over).filter(User.id == user_id).all()
    personal_rank = [[i[2], i[0]] for i in result]

    for i in personal_rank:
        if i[1] == id:
            user_rank = [
                {'id': i[1], 'ranking': i[0]}
            ]

    return user_rank
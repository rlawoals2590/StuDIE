from main import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Text(), primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    birth = db.Column(db.Integer, nullable=False)
    belong = db.Column(db.Text())
    gender = db.Column(db.Integer, nullable=False)
    local = db.Column(db.Text())
    rival_id = db.Column(db.Integer)
    passwd = db.Column(db.Text(), nullable=False)
    join_date = db.Column(db.DateTime(), nullable=False)
    login_token = db.Column(db.Text())
    point = db.Column(db.Integer)










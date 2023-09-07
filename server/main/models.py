from main import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Text(), primary_key=True)
    belong = db.Column(db.Text())
    local = db.Column(db.Text())
    passwd = db.Column(db.Text(), nullable=False)
    login_token = db.Column(db.Text())
    point = db.Column(db.Integer)
from main import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Text(), primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    birth = db.Column(db.DateTime(), nullable=False)
    belong = db.Column(db.Text())
    gender = db.Column(db.Integer, nullable=False)
    local = db.Column(db.Text())
    rival_id = db.Column(db.Integer)
    passwd = db.Column(db.Text(), nullable=False)
    join_date = db.Column(db.DateTime(), nullable=False)
    login_token = db.Column(db.Text())


class Point(db.Model):
    __tablename__ = 'Point'

    id = db.Column(db.Text(), primary_key=True)
    point = db.Column(db.Integer)

    # stid 외래 키 제약의 이름을 'fk_stid'로 지정
    db.ForeignKeyConstraint(['id'], ['User.id'], name='fk_id')









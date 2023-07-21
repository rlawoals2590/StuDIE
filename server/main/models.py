from main import db


class Student(db.Model):                                    # 학생 테이블
    stid = db.Column(db.Integer, primary_key=True)          # 학번
    passwd = db.Column(db.Text(), nullable=False)           # 비밀번호
    name = db.Column(db.Text(), nullable=False)             # 이름
    gender = db.Column(db.Integer, nullable=False)          # 성별
    school = db.Column(db.Text(), nullable=False)           # 학교 이름
    local = db.Column(db.Text(), nullable=False)            # 지역 이름
    join_date = db.Column(db.DateTime(), nullable=False)    # 가입 날짜
    rival = db.Column(db.Integer)                           # 라이벌
    login_token = db.Column(db.Text())                      # 로그인 토큰


class Point(db.Model):                                                              # 포인트 테이블
    stid = db.Column(db.Integer, db.ForeignKey(Student.stid), primary_key=True)     # 학번 (학생 테이블의 학번 참조)
    name = db.Column(db.Integer, nullable=False)                                    # 이름
    school = db.Column(db.Text(), nullable=False)                                   # 학교 이름
    local = db.Column(db.Text(), nullable=False)                                    # 지역 이름
    point = db.Column(db.Integer, nullable=False)                                   # 포인트









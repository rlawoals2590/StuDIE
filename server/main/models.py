from main import db


class Student(db.Model):                                    # 학생 테이블
    stid = db.Column(db.Integer, primary_key=True)          # 학번
    passwd = db.Column(db.Text(), nullable=False)           # 비밀번호
    name = db.Column(db.Text(), nullable=False)             # 이름
    gender = db.Column(db.Integer, nullable=False)          # 성별
    school = db.Column(db.Text(), primary_key=True)         # 학교 이름
    local = db.Column(db.Text(), nullable=False)            # 지역 이름
    join_date = db.Column(db.DateTime(), nullable=False)    # 가입 날짜
    rival = db.Column(db.Integer)                           # 라이벌
    rival_school = db.Column(db.Text())                     # 라이벌 학생의 학교
    login_token = db.Column(db.Text())                      # 로그인 토큰

    __table_args__ = (
        db.PrimaryKeyConstraint('stid', 'school', name='pk_stid_school_student2'),
    )


# class Point(db.Model):                                                              # 포인트 테이블
#         stid = db.Column(db.Integer, primary_key=True)                                  # 학번 (학생 테이블의 학번 참조)
#     db.ForeignKeyConstraint(['stid'], ['Student.stid'], name='fk_stid')
#     name = db.Column(db.Integer, nullable=False)                                    # 이름
#     school = db.Column(db.Text(), primary_key=True)                                 # 학교 이름
#     db.ForeignKeyConstraint(['school'], ['Student.school'], name='fk_school')
#     local = db.Column(db.Text(), nullable=False)                                    # 지역 이름
#     point = db.Column(db.Integer, nullable=False)                                   # 포인트
#
#     __table_args__ = (
#         db.PrimaryKeyConstraint('stid', 'school', name='pk_stid_school_point2'),
#     )

class Point(db.Model):
    stid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    school = db.Column(db.Text(), primary_key=True)
    local = db.Column(db.Text(), nullable=False)
    point = db.Column(db.Integer, nullable=False)

    # stid 외래 키 제약의 이름을 'fk_stid'로 지정
    db.ForeignKeyConstraint(['stid'], ['Student.stid'], name='fk_stid')

    # school 외래 키 제약의 이름을 'fk_school'로 지정
    db.ForeignKeyConstraint(['school'], ['Student.school'], name='fk_school')

    # stid와 school로 구성된 복합 기본 키 제약의 이름을 'pk_stid_school_point2'로 지정
    __table_args__ = (
        db.PrimaryKeyConstraint('stid', 'school', name='pk_stid_school_point2'),
    )










import os
from datetime import timedelta

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'StuDIE.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config:
    JWT_SECRET_KEY = 'b\'_5#y2L"F4Q8z\n\xec]/'
    SESSION_SECRET_KEY = 'S&DYAUIDH&WFIU82768@$!'
    COOKIE_NAME = 'user_access_token'
    SESSION_LIMIT = timedelta(hours=24)
    ACCESS_TOKEN = timedelta(hours=24)
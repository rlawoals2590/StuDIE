from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Api

from config import Config
import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config)
    app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
    app.secret_key = Config.SESSION_SECRET_KEY
    app.config["PERMANENT_SESSION_LIFETIME"] = Config.SESSION_LIMIT
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = Config.ACCESS_TOKEN
    app.config['JWT_ACCESS_COOKIE_NAME'] = Config.COOKIE_NAME
    app.config['JWT_TOKEN_LOCATION'] = ["headers", "cookies", "json", "query_string"]

    # from flask_socketio import SocketIO
    # socketio = SocketIO(logger=True, engineio_logger=True)

    jwt = JWTManager(app)

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # socketio.init_app(app)

    from .user.user_route import user_api
    api.add_namespace(user_api, '/user')

    from .room.room_route import room_api
    api.add_namespace(room_api, '/room')

    # from .rank.rank_route import rank_api
    # api.add_namespace(rank_api, '/rank')

    from .visitor.visitor_route import visitor_api
    api.add_namespace(visitor_api, '/visitor')

    # from .room.events import ChatNamepsace
    #  socketio.on_namespace(ChatNamepsace('/room/chat/'))

    return app

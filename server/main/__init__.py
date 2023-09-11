from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_cors import CORS

from config import Config
import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    from .index.index_route import index_route
    app.register_blueprint(index_route)

    CORS(app)
    api = Api(app, doc="/swagger")

    app.config.from_object(config)
    app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
    app.secret_key = Config.SESSION_SECRET_KEY
    app.config["PERMANENT_SESSION_LIFETIME"] = Config.SESSION_LIMIT
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = Config.ACCESS_TOKEN
    app.config['JWT_ACCESS_COOKIE_NAME'] = Config.COOKIE_NAME
    app.config['JWT_TOKEN_LOCATION'] = ["headers", "cookies", "json", "query_string"]

    jwt = JWTManager(app)

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .user.user_route import user_api
    api.add_namespace(user_api, '/user')

    from .room.room_route import room_api
    api.add_namespace(room_api, '/room')

    from .room.room_route import room_app
    app.register_blueprint(room_app)

    from .rank.rank_route import rank_api
    api.add_namespace(rank_api, '/rank')

    from .visitor.visitor_route import visitor_api
    api.add_namespace(visitor_api, '/visitor')

    return app

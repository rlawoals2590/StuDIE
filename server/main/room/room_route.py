from flask import Blueprint, request, session, redirect, url_for, render_template, make_response, jsonify
from functools import wraps
from ..user.func.auth import user_validation
from markupsafe import escape
from main.models import User
from main import db
from main.ai_models.checkout_studying import CHECKOUT_STUDYING

from flask_restx import Resource, Namespace, fields, cors
import base64


room_api = Namespace('room_api', decorators=[cors.crossdomain(origin="*")])
room_app = Blueprint('main', __name__)

detection = CHECKOUT_STUDYING(5)


@room_api.route('/')
class Index(Resource):
    def get(self):
        return make_response(render_template('studyRoom.html'))


@room_api.route('/upload')
class UploadImage(Resource):
    @room_api.expect(room_api.model('image upload', {
        'image': fields.String(required=True, description='Base64 encoded image data'),
    }))
    def post(self):
        image_data = request.json['image']
        image_data = image_data.split(',')[1]
        print(image_data[:100])

        with open('main/ai_models/image/image.jpg', 'wb') as image_file:
            image_file.write(base64.b64decode(image_data))

        return {'message': "Image uploaded successfully"}, 200


@room_api.route('/score/')
class Score(Resource):
    def get(self):
        id = escape(session['id'])
        score = detection.start_detection("main/ai_models/image/image.jpg", id)

        return {'score': score}, 200

    def post(self):
        data = request.json
        id = escape(session['id'])
        detection.stop_detection(id)
        return jsonify({"message": "Score reset successfully!"})


@room_api.route('/save/<int:score>')
class Save(Resource):

    def get(self, score):
        id = escape(session['id'])

        user_score_save = User.query.filter_by(id=id).first()

        if user_score_save:
            user_score_save.point += score

            db.session().commit()

            return 'Succes'
        else:
            return 'Fail'



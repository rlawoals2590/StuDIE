from flask import Blueprint, request, session, redirect, url_for, render_template
from ..user.func.auth import user_validation
from markupsafe import escape

from main.ai_models.checkout_studying import CHECKOUT_STUDYING

from flask_restx import Resource, Namespace, fields
import base64

room_api = Namespace('room_api')

detection = CHECKOUT_STUDYING(5)


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
        score = detection.start_detection("main/ai_models/image/image.jpg")

        user_score = {
            id: score
        }

        print(user_score)
        return {'score': user_score}, 200



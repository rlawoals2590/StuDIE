from flask import Blueprint, request, session, redirect, url_for, render_template
from ..user.func.auth import user_validation

from main.ai_models.checkout_studying import CHECKOUT_STUDYING

from flask_restx import Resource, Namespace, fields
import base64

room_api = Namespace('room_api')


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

        detection = CHECKOUT_STUDYING()
        score = detection.start_detection("main/ai_models/image/image.jpg")
        print(score)

        return {'message': "Image uploaded successfully"}, 200




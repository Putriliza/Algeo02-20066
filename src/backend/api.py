from flask import Blueprint, request
from flask_restx import Api, Resource
from img_process import compress_image
from time import time

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
rest_api = Api(api_blueprint)

@api_blueprint.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

@rest_api.route('/compress')
class Test(Resource):
    def get(self):
        return {'request': 'Success'}

    def post(self):
        image_body = str(request.json['image']).split(",")
        compress_ratio = int(request.json['ratio'])
        image_mime = image_body[0]
        image_base64 = image_body[1]

        t1 = time()
        try:
            img_str, diff = compress_image(image_base64, compress_ratio)
        except:
            img_str, diff = "err", 0
        t2 = time()

        if img_str == "err":
            return {
                'success': False,
                'message': "An error occurred!"
            }
        else:
            return {
                'success': True,
                'image': image_mime + "," + img_str.decode("utf-8"),
                'diff': diff,
                'time': round(t2 - t1, 2)
            }

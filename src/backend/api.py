from flask import Blueprint, request, send_file
from flask_restx import Api, Resource
from PIL import Image
from io import BytesIO
from img_process import img_to_matrix, matrix_to_img


api_blueprint = Blueprint('api', __name__, url_prefix='/api')
rest_api = Api(api_blueprint)

@api_blueprint.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

@rest_api.route('/test')
class Test(Resource):
    def get(self):
        return {'request': 'Success'}
    
    # def post(self):
    #     img = Image.open(request.files.get('test').stream)
    #     buffer = img_to_matrix(img)
    #     buffer = matrix_to_img(buffer, 'hello')
    #     byte_io = BytesIO()
    #     buffer.save(byte_io, 'PNG')
    #     byte_io.seek(0)
    #     return send_file(buffer, mimetype='image/png')

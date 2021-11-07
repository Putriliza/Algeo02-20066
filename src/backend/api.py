from flask import Blueprint, request
from flask_restx import Api, Resource
from PIL import Image
from io import BytesIO
import base64
from img_process import img_to_matrix, matrix_to_img, compress_matrix, svd_to_matrix
from numpy.linalg import svd
from numpy import diag
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

        image = base64.b64decode(str(image_base64))
        image = Image.open(BytesIO(image))

        t1 = time()
        r, g, b = img_to_matrix(image)

        ru,rs,rv=svd(r)
        gu,gs,gv=svd(g)
        bu,bs,bv=svd(b)

        new_r = compress_matrix([ru, diag(rs), rv], compress_ratio)
        new_g = compress_matrix([gu, diag(gs), gv], compress_ratio)
        new_b = compress_matrix([bu, diag(bs), bv], compress_ratio)

        new_r = svd_to_matrix(new_r)
        new_g = svd_to_matrix(new_g)
        new_b = svd_to_matrix(new_b)

        buffer = [new_r, new_g, new_b]

        buffer, img_type = matrix_to_img(buffer)
        t2 = time()

        bytes_buffer = BytesIO()
        buffer.save(bytes_buffer, img_type)
        img_str = base64.b64encode(bytes_buffer.getvalue())
        return {
            'image': image_mime + "," + img_str.decode("utf-8"),
            'time': round(t2 - t1, 2)
            }

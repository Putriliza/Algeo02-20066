from PIL import Image
from numpy import asarray, ma, clip
from numpy import uint8
from numpy.lib.shape_base import dstack
from base64 import b64decode, b64encode
from io import BytesIO
from SVD import getSVD
from time import time

def img_to_matrix(image, mode):
    imageAr = asarray(image)

    if mode == "L" or mode == "P":
        return [imageAr]
    if mode == "LA":
        color = 2
    elif mode == "RGB":
        color = 3
    elif mode == "RGBA" or mode == "CMYK":
        color = 4

    buffer = []
    for i in range(color):
        buffer.append(imageAr[:, :, i])

    return buffer


def compress_matrix(matrix_svd, diff):
    rank = len(matrix_svd[1][0])
    subtr = round((diff / 100) * rank)
    new_rank = rank - subtr
    u, e, vt = matrix_svd
    new_svd = [u[:, :new_rank], e[:new_rank, :new_rank], vt[:new_rank, :]]
    return new_svd


def svd_to_matrix(matrix_svd):
    u, e, vt = matrix_svd
    return u @ e @ vt


def matrix_to_img(buffer, convert=None):
    if len(buffer) > 1:
        return Image.fromarray(uint8(dstack(buffer))).convert(convert)
    else:
        return Image.fromarray(uint8(buffer[0])).convert(convert)


def mask_png(buffer, mask):
    newBuffer = []
    for i in range(len(buffer)):
        mask_array = mask[i]
        png_arr = buffer[i]

        m = ma.masked_where(mask_array == 0, mask_array, copy=False)
        png_arr = ma.masked_where(ma.getmask(m), png_arr, copy=False)
        png_arr = png_arr.filled(0)
        png_arr = png_arr.astype(uint8)
        newBuffer.append(png_arr)
    return newBuffer


def compress_image(b64Img: str, ratio: int):
    image = b64decode(b64Img)
    image = Image.open(BytesIO(image))
    original_mode = image.mode
    if original_mode == "P":
        image = image.convert("RGBA")
        mode = image.mode
    elif original_mode == "CMYK":
        image = image.convert("RGB")
        mode = image.mode
    else:
        mode = original_mode

    buffer = img_to_matrix(image, mode)
    new_buffer = []

    if mode == "RGB" or mode == "L":
        img_type = "JPEG"
        for color in buffer:
            u, s, vt = getSVD(color)
            new_color = compress_matrix([u, s, vt], ratio)
            new_color = svd_to_matrix(new_color)
            clip(new_color, 0, 255, out=new_color)
            new_buffer.append(new_color)
        img = matrix_to_img(new_buffer, original_mode)

    elif mode == "RGBA" or mode == "LA":
        img_type = "PNG"
        for color in buffer[:-1]:
            u, s, vt = getSVD(color)
            new_color = compress_matrix([u, s, vt], ratio)
            new_color = svd_to_matrix(new_color)
            clip(new_color, 0, 255, out=new_color)
            new_buffer.append(new_color)
        new_buffer = mask_png(new_buffer, buffer[:-1])
        new_buffer.append(buffer[-1])
        img = matrix_to_img(new_buffer, original_mode)

    image_buffer = BytesIO()
    img.save(image_buffer, format=img_type)
    img_str = b64encode(image_buffer.getvalue())
    return img_str
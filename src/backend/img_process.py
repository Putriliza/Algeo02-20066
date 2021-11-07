from PIL import Image
from numpy import asarray, ma
from numpy import uint8
from numpy.lib.shape_base import dstack

def img_to_matrix(image):
    imageAr = asarray(image)
    imgType = len(imageAr[0][0])
    buffer = []
    for i in range(imgType):
        buffer.append(imageAr[:,:,i])
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

def matrix_to_img(buffer):
    buffer_length = len(buffer)
    if buffer_length == 3:
        img_type = "JPEG"
    elif buffer_length == 4:
        img_type = "PNG"

    return Image.fromarray(uint8(dstack(buffer))), img_type

def mask_png(buffer, mask):
    newBuffer = []
    for i in range(len(buffer)):
        mask_array = mask[i]                
        png_arr = buffer[i]

        m = ma.masked_where(mask_array==0, mask_array, copy=False)
        png_arr = ma.masked_where(ma.getmask(m), png_arr, copy=False)
        png_arr = png_arr.filled(0)
        png_arr = png_arr.astype(uint8)
        newBuffer.append(png_arr)
    return newBuffer
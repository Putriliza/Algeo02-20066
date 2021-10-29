from PIL import Image
from numpy import asarray, ma
from numpy import uint8
from numpy.lib.shape_base import dstack
from numpy import diag

def img_to_matrix(image):
    im_1 = Image.open(rf"{image}")
    imageAr = asarray(im_1)
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

def matrix_to_img(buffer, filename):
    imgType = len(buffer)
    data = Image.fromarray(uint8(dstack(buffer)))

    type = ""
    if imgType == 4:
        type = ".png"
    elif imgType == 3:
        type = ".jpg"

    data.save("./img_output/" + filename + type, bitmap_format="png")

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


#Testing Proses kompresi JPG
# buffer = img_to_matrix("../../test/wal.png")
# r,g,b,a = buffer

# ratio=99

# ru,rs,rv=svd(r)
# gu,gs,gv=svd(g)
# bu,bs,bv=svd(b)

# new_r = compress_matrix([ru, diag(rs), rv], ratio)
# new_g = compress_matrix([gu, diag(gs), gv], ratio)
# new_b = compress_matrix([bu, diag(bs), bv], ratio)

# new_r = svd_to_matrix(new_r)
# new_g = svd_to_matrix(new_g)
# new_b = svd_to_matrix(new_b)

# buffer = mask_png([new_r, new_g, new_b],[r,g,b])

# buffer.append(a)

# matrix_to_img(buffer, "jova")
from PIL import Image
from numpy import array
from numpy import uint8
from numpy.core.fromnumeric import squeeze
from numpy.lib.shape_base import dstack

def img_to_matrix(image):

    im_1 = Image.open(rf"{image}")
    imageAr = array(im_1)

    width = im_1.size[0]
    height = im_1.size[1]

    imgType = len(imageAr[0][0])
    buffer = []
    # buffer = [[],[],[]]
    # for i in range(height):
    #     rm, gm, bm = [],[],[]
    #     for j in range(width):
    #         rgba = imageAr[i][j]
    #         r,g,b = rgba
    #         rm.append(r)
    #         gm.append(g)
    #         bm.append(b)
    #     buffer[0].append(rm)
    #     buffer[1].append(gm)
    #     buffer[2].append(bm)
        
    imageAr = imageAr.transpose(2,0,1).reshape(3,-1)
    for i in range(len(imageAr)):
        a = squeeze(imageAr[i])
        a = a.reshape(height, width)
        buffer.append(a)
    return buffer[:imgType]

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
    # height = len(buffer[0])
    # width = len(buffer[0][0])

    # imgAr = [[[0 for _ in range(imgType)] for _ in range(width)] for _ in range(height)]

    # for i in range(height):
    #     for j in range(width):
    #         for k in range(imgType):
    #             imgAr[i][j][k] = buffer[k][i][j]

    # data = Image.fromarray(uint8(imgAr))
    data = Image.fromarray(uint8(dstack(buffer)))

    type = ""
    if imgType == 4:
        type = ".png"
    elif imgType == 3:
        type = ".jpg"

    data.save("./img_output/" + filename + type)


#Testing Proses kompresi JPG
buffer = img_to_matrix("../../test/aaaaa.jpg")
# r,g,b = buffer

# ratio=50
# r = compress_matrix(svd(r), ratio)
# g = compress_matrix(svd(g), ratio)
# b = compress_matrix(svd(b), ratio)

# r = svd_to_matrix(r)
# g = svd_to_matrix(g)
# b = svd_to_matrix(b)
# buffer = [r,g,b]
matrix_to_img(buffer, "jova")
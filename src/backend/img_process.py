from PIL import Image
from numpy import array

def img_to_matrix(image):

    im_1 = Image.open(rf"{image}")
    imageAr = array(im_1)

    width = im_1.size[0]
    height = im_1.size[1]

    imgType = len(imageAr[0][0])

    bufferR = [[0 for _ in range(width)] for _ in range(height)]
    bufferG = [[0 for _ in range(width)] for _ in range(height)]
    bufferB = [[0 for _ in range(width)] for _ in range(height)]
    bufferA = [[0 for _ in range(width)] for _ in range(height)]
    buffer = [bufferR, bufferG, bufferB, bufferA]

    for i in range(height):
        for j in range(width):
            rgba = imageAr[i][j]
            for k in range(imgType):
                buffer[k][i][j] = rgba[k]
    
    return buffer[:imgType]

# ubah ke numpy arrray
u = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
e = [
    [4,0],
    [0,2],
    [0,0]
]
vt = [
    [1,2],
    [3,4]
]
svd_example = [u,e,vt]

def compress_matrix(matrix_svd, diff):
    rank = len(matrix_svd[1][0])
    subtr = (diff / 100) * rank
    new_rank = rank - subtr
    u, e, vt = matrix_svd
    new_svd = [u[:, :new_rank], e[:new_rank, :new_rank], vt[:new_rank, :]]
    return new_svd

def svd_to_matrix(matrix_svd):
    u, e, vt = matrix_svd
    return u @ e @ vt

def matrix_to_img(buffer, filename):
    imgType = len(buffer)
    height = len(buffer[0])
    width = len(buffer[0][0])

    imgAr = [[[0 for _ in range(imgType)] for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            for k in range(imgType):
                imgAr[i][j][k] = buffer[k][i][j]
    
    imgAr = array(imgAr)
    data = Image.fromarray(imgAr)

    type = ""
    if imgType == 4:
        type = ".png"
    elif imgType == 3:
        type = ".jpg"

    data.save("./img_output/" + filename + type)


# Testing
buffer = img_to_matrix("../../test/aaaaa.jpg")
matrix_to_img(buffer, "jova")
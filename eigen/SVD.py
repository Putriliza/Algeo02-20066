import numpy as np
import math as math
from copy import deepcopy
from numpy.core.fromnumeric import shape
from numpy.linalg import eig, qr

def getLambdaUV(m):   # m sudah harus matriks simetris
    n = len(m)
    mVector = np.identity(n)
    for i in range(0, n**2):
        q, r = qr(m)
        mVector = np.matmul(mVector, q)
        m = np.matmul(r, q)
        # if i == math.floor(n**2/4):
        #     print("25%")
        # elif i == math.floor(n**2/2):
        #     print("50%")
        # elif i == math.floor(3*n**2/4):
        #     print("75%")
    lamda = np.diag(m, k=0)
    return lamda, mVector

def getSigma(m):
    m1 = np.matmul(m, np.transpose(m))
    lamda, U = getLambdaUV(m1)
    sigma = np.sqrt(lamda)
    S = np.zeros(shape(m))
    for i in range (min(shape(m))) :
        S[i][i] = sigma[i]

    return S

def getSVD(m) :
    leftSingular = np.matmul(m, np.transpose(m))        # A.A^T untuk U
    rightSingular = np.matmul(np.transpose(m), m)       # A^T.A untuk V^T
    lamda, U = getLambdaUV(leftSingular)
    lamda, V = getLambdaUV(rightSingular)
    VT = np.transpose(V)
    S = getSigma(m)
    # SVD = np.matmul(U,S)
    # SVD = np.matmul(SVD, VT)
    return U, S, VT
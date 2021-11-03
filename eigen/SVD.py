import numpy as np
import math as math
from copy import deepcopy
from numpy.core.fromnumeric import shape
from numpy.linalg import eig, qr

def getLambdaUV(m):   # m sudah harus matriks simetris
    n = len(m)
    mVector = np.identity(n)
    for i in range(0, 100):
        q, r = qr(m)
        mVector = np.matmul(mVector, q)
        m = np.matmul(r, q)
    lamda = np.diag(m, k=0)
    return lamda, mVector

def getSigma(m, lamda):
    sigma = np.sqrt(lamda)
    S = np.zeros(shape(m))
    for i in range (min(shape(m))) :
        S[i][i] = sigma[i]

    return S

def getSVD(m) :
    leftSingular = np.matmul(m, np.transpose(m))        # A.A^T untuk U
    rightSingular = np.matmul(np.transpose(m), m)       # A^T.A untuk V^T
    lamda1, U = getLambdaUV(leftSingular)
    lamda2, V = getLambdaUV(rightSingular)
    VT = np.transpose(V)
    S = getSigma(m, lamda1)
    # SVD = np.matmul(U,S)
    # SVD = np.matmul(SVD, VT)
    return U, S, VT
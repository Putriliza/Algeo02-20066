import numpy as np
from numpy.linalg import qr

def getLambdaUV(m):   # m sudah harus matriks simetris
    n = len(m)
    mVector = np.identity(n)
    for _ in range(0, 1):
        q, r = qr(m)
        mVector = np.matmul(mVector, q)
        m = np.matmul(r, q)
    lamda = np.diag(m, k=0)
    return lamda, mVector

def getSigma(m, lamda):
    new_lamda = lamda.copy()
    np.absolute(new_lamda, out=new_lamda)
    sigma = np.sqrt(new_lamda[:min(m.shape)])
    return np.diag(sigma)

def getSVD(m: np.ndarray) :
    height, width = m.shape
    min_s = min(height, width)
    if width >= height:
        lamda1, U = getLambdaUV(m @ m.T)
    elif width < height:
        lamda1, VT = getLambdaUV(m.T @ m)
    
    S = getSigma(m, lamda1)
    if width >= height:
        VT = np.linalg.inv(S) @ (U.T)[:height, :] @ m
    elif width < height:
        U = m @ (VT.T)[:, :width] @ np.linalg.inv(S)
    
    return U[:, :min_s], S, VT[:min_s, :]

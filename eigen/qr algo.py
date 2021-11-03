import numpy as np
import math as math
from copy import deepcopy
from numpy.linalg import eig, qr

def eigenQR(m):   # m sudah harus matriks simetris
    n = len(m)
    mVector = np.identity(n)
    for i in range(0, 30):
        q, r = qr(m)
        mVector = np.matmul(mVector, q)
        m = np.matmul(r, q)
        if i == 7:
            print("25%")
        elif i == 15:
            print("50%")
        elif i == 23:
            print("75%")
    mVector = mVector.round(decimals=3)
    m = np.diag(m, k=0)
    m = m.round(decimals=2)
    print(m)
    print(mVector)
    return m, mVector

m = np.random.randint(0, 255, (1024, 500))
m = np.matmul(m, np.transpose(m))

eigenQR(m)
print(eig(m))
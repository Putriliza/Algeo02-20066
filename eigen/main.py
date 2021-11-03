# Buat testing

import numpy as np
import math as math
from numpy.core.fromnumeric import shape
from numpy.linalg import eig

from SVD import *

# m = np.random.randint(0, 255, (1024, 500))
m = np.array([[-2,2], [-1,1], [2,-2]])

#versi pakai eig
l1, U1 = eig(np.matmul(m, np.transpose(m)))        # A.A^T untuk U
l2, V1 = eig(np.matmul(np.transpose(m), m))       # A^T.A untuk V^T
print(U1)
print(np.transpose(V1))
print("\n")

#versi pakai fungsi kita
U, S, VT = getSVD(m)
print(U)
print(S)
print(VT)

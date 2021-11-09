import numpy as np
import math as math
from numpy.core.fromnumeric import shape

from SVD import getSVD

def compressMatrix(M):
    U,S,VT = getSVD(M)
    # print(U)
    # print(S)
    # print(VT)
    CR = int(input("Compression Rate (1-99%): "))
    m,n = shape(M)
    k = math.floor((m*n)/((CR/100)*(m+n+1)))
    # RUMUS : CR = (m*n/(k*(m+n+1))
    print(f"k= {k}")
    UNew = U[:, :k]         # ambil K kolom pertama
    SNew = S[:k, :k]        # ambil matriks KxK pojok kiri atas
    VTNew = VT[:k, :]       # ambil K baris pertama
    CompressedM = np.matmul(UNew,SNew)
    CompressedM = np.matmul(CompressedM, VTNew)
    return CompressedM

# m = np.random.randint(0, 255, (1024, 500))

# print(compressMatrix(m))
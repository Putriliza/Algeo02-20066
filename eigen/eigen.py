import numpy as np
import math as math
from copy import deepcopy
# ini buat tess!!
from numpy.linalg import eig

# menentukan nilai eigen dan vektor eigen dari matriks simetris!! 
# matriks harus dikaliin sama matriks transposenya
def eigen(m):
    n = len(m)
    mB = np.identity(n)    # inisiasi matriks untuk vektor eigenn

    maxVal = 0
    p = 0
    q = 0    # baris (p) dan kolom (q) pada matrix m yang menampung maxVal
    i = 0
    j = 1
    while (i < n):      # loop pada matriks bagian segitiga atas, karena pasti matriks simetris
        while (j < n):
            if abs(m[i][j]) > maxVal:   # mencari nilai max
                p = i
                q = j
                maxVal = abs(m[i][j])
            j += 1
        i += 1
        j = i + 1

    subs = m[p][p] - m[q][q]
    if subs == 0:
        tetha = 45
    else:
        tetha = abs((math.degrees(math.atan((2 * m[p][q])/subs))) / 2)

    stheta = round(math.sin(math.radians(tetha)), 3)
    ctheta = round(math.cos(math.radians(tetha)), 3)

    nRot = 0
    maxRot = (5 * (n ** 2))
    while (stheta != 0) and (maxVal != 0) and (nRot < maxRot):  # kondisi ketika iterasi terpenuhi
        nRot += 1
        mJ = deepcopy(m)    # matriks jacobi
        mJ = mJ.astype(np.float32)

        mJ[p][q] = stheta * -1
        mJ[q][p] = stheta
        mJ[p][p] = ctheta
        mJ[q][q] = ctheta

        i = 0
        j = 1
        while (i < n):      # mengubah semua nilai nondiagonal matriks, kecuali m[p][q] dan m[q][p] menjadi 0
            while (j < n):
                if not((i == p) and (j == q)):
                    mJ[i][j] = 0
                    mJ[j][i] = 0
                j += 1
            i += 1
            j = i + 1
        for k in range(0, n):
            if ((k != p) and (k != q)):
                mJ[k][k] = 1
        #print("MJ")
        #print(mJ) 
        #print("MB")
        mB = np.matmul(mB, mJ)      # menghitung vektor 
        #print(mB)
        m = np.matmul(np.matmul(np.transpose(mJ), m), mJ)
        
        #print(m)

        maxVal = 0
        p = 0
        q = 0    # baris (p) dan kolom (q) tempat max val
        i = 0
        j = 1
        while (i < n):
            while (j < n):
                if abs(m[i][j]) > maxVal:
                    p = i
                    q = j
                    maxVal = abs(m[i][j])
                j += 1
            i += 1
            j = i + 1
    
        subs = m[p][p] - m[q][q]
        if subs == 0:
            tetha = 45
        else:
            tetha = abs((math.degrees(math.atan((2 * m[p][q])/subs))) / 2)
        stheta = round(math.sin(math.radians(tetha)), 3)
        ctheta = round(math.cos(math.radians(tetha)), 3)

    eigValsArr = []
    for k in range(0, n):
        if abs(m[k][k]) < 0.009:
            eigValsArr.append(0)
        else:
            eigValsArr.append(round(m[k][k], 0))

    mB = mB.round(decimals=2)
    #print(mB)
    return eigValsArr, mB


# tes inisialisasi random matrix           
m = np.array([[10,0,2], [0,10,4], [2,4,2]])
mt = np.array([[11,1], [1,11]])
m2 = np.array([[8, -1, 3, -1], [-1, 6, 2, 0], [3, 2, 9, 1], [-1, 0, 1, 7]])
m3 = np.random.randint(0, 255, (200, 3))
m3 = np.matmul(m3, np.transpose(m3))

# tes eigen
print(eig(m3))      # eigen python
vals, mb = eigen(m3)
print(vals, mb)
#DiamondCoder 18.10.2022
import math
import matplotlib.pyplot as plt



def initRaster(nrows: int, ncols: int, v) -> list:
    return [[v]*ncols] * nrows
print(initRaster(2, 2, 5))

ras = initRaster(256,256,0)

for y in range(256):
    for x in range(256):
        ras[y][x] = (y*y + x*x)**.5
        
plt.imshow(ras)
plt.show()


"""
chs=[]
UwU = True
for y in range(8):
    line=[]
    for x in range(8):
        line.append(1 if UwU else 0)
        UwU = not UwU
    chs.append(line)
    UwU = not UwU
plt.imshow(chs, cmap='gray')
plt.show()

chess=[[1,0]*4, [0,1]*4]*4
plt.imshow(chess)
plt.show()
"""
#DiamondCoder 08.11.2022
import math
import matplotlib.pyplot as plt
import numpy as np


img=plt.imread('PsViragokSzurkeKicsi.jpg')
KRNL = '1 0 -1' + \
    '2 0 -2' + \
    '1 0 -1'

def convole(kernel: str, img):
    a,b,c, \
    d,e,f, \
    g,h,i = map(float, kernel.split())
    
    for y in range(1, rows-1):
        r1 = img[y-1]
        r2 = img[y]
        r3 = img[y+1]
        for x in range(1, cols-1):
            ret[y-1][x-1] = a*r1[x-1][0] + b*r1[x][0] + c*r1[x+1][0] + \
                d*r2[x-1][0] + e*r2[x][0] + f*r2[x+1][0] + \
                g*r3[x-1][0] + h*r3[x][0] + i*r3[x+1][0]
    return ret
    #return

rows, cols, *_ = img.shape
ret = np.empty((rows-2, cols-2), dtype='int16')

plt.imshow(convole(KRNL, img), cmap='gray')
plt.show()



"""
c=6
print(math.radians(c))

n=[4,5,9,44,84.5]
r = map(math.radians, n)
print(list(r))

st='1 3 4 5 99 -1'
integers = map(int, st.split())
#print(list(integers))
#print(list(map(subtract, n)))
"""
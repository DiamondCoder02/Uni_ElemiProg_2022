#DiamondCoder 25.10.2022
import math
import matplotlib.pyplot as plt

#dalia = plt.imread('dalia.jpg')

def getUnitString(n: int, unit: str) -> str:
    if n==0: return ''
    if n==1:
        return f'{n} {unit}'
    return f'{n} {unit}s'
def getHumanReadableString(seconds:int) -> str:
    M=60
    H=60*M
    D=24*H
    Y=365*D
    year, seconds = divmod(seconds, Y)
    day, seconds = divmod(seconds, D)
    hour, seconds = divmod(seconds, H)
    minute, seconds = divmod(seconds, M)
    
    unitList = [getUnitString(year, 'year'), 
                getUnitString(day, 'day'), 
                getUnitString(hour, 'hour'), 
                getUnitString(minute, 'minute'), 
                getUnitString(seconds, 'second')
                ]
    
    joined = ', '.join([x for x in unitList if x!=''])[::-1]
    return joined.replace(' ,', ' dna ', 1)[::-1]
    print(year, day, hour, minute, seconds)

#print(getUnitString(1, 'year'))
print(getHumanReadableString(1087645504))


"""
def showLayers(ras):
    rr, gr, br = ras.copy(), ras.copy(), ras.copy()
    nrows, ncols, layers = dalia.shape

    for y in range(nrows):
        for x in range(ncols):
            p=ras[y][x]
            rr[y][x]=[p[0],0,0]
            gr[y][x]=[0,p[1],0]
            br[y][x]=[0,0,p[2]]
    plt.imshow(rr)
    plt.show()
    plt.imshow(gr)
    plt.show()
    plt.imshow(br)
    plt.show()
"""
#showLayers(dalia)

"""
r=[0]*256
g=[0]*256
b=[0]*256
nrows, ncols, layers = dalia.shape

for y in range(nrows):
    for x in range(ncols):
        p=dalia[y][x]
        r[p[0]] +=1
        g[p[0]] +=1
        b[p[0]] +=1
plt.plot(r, c="red")
plt.plot(g, c="green")
plt.plot(b, c="blue")
#plt.show()

x,y = range(256), range(256)
X,Y = plt.np.meshgrid(x,y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(X,Y, plt.np.array(ras))
#plt.show()
"""

def clamp(x:int) -> int:
    if x<0:
        return 0
    if x>255:
        return 255
    return 
def changeLumin(ras, c:int):
    cras = ras.copy()
    nrows, ncols, layers = cras.shape
    for y in range(nrows):
        for x in range(ncols):
            p=cras[y][x]
            p[0] = clamp(p[0]+c)
            p[1] = clamp(p[1]+c)
            p[2] = clamp(p[2]+c)
    return cras

#drk = changeLumin(dalia, -50)
#plt.imshow(drk)
#plt.show()
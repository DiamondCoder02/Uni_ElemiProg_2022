import matplotlib.pyplot as plt

path = "fire.txt"
sx = 0.0
sy = 0.0
n = 0

with open(path) as file:
    for row in file:
        x,y = row.split(',')
        x,y = float(x), float(y)
        
        sx+=x
        sy+=y
        n+=1
        plt.scatter(x,y, c="red")

print(sx/n, '|', sy/n)

avx, avy = sx/n, sy/n
plt.scatter(avx, avy, marker="x", c='blue')

plt.show()

minx, miny, maxx, maxy = 9999999999.,9999999999.,-9999999999.,0.0

with open(path) as file:
    for row in file:
        x,y = row.split(',')
        x,y = float(x), float(y)
        plt.scatter(x,y, c="red")
        
        if x < minx:
            minx=x
        if y < miny:
            miny=y
        if x > maxx:
            maxx=x
        if y > maxy:
            maxy=y
plt.scatter((minx+maxx)/2, (miny+maxy)/2)

def Distance(x0,x1,y0,y1):
    dx= x1-x0
    dy= y1-y0
    return (dx*dx+dy*dy) **0.5

print(Distance(5,5,7,7))

plt.show()

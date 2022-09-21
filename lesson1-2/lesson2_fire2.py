import matplotlib.pyplot as plt

path = "fire.txt"
X,Y = [], []

with open(path) as file:
    for row in file:
        x,y = row.split(',')
        x,y = float(x), float(y)
        plt.scatter(x,y, c="red")
        
        X.append(x)
        Y.append(y)

avx, avy = sum(X)/len(X), sum(Y)/len(Y)

def Distance(x0,x1,y0,y1):
    dx= x1-x0
    dy= y1-y0
    return (dx*dx+dy*dy) **0.5

D=[]
for i in range(0, len(X)):
    D.append(Distance(X[i], Y[i], avx, avy))

pointIndex = D.index(min(D))
print(pointIndex)
plt.scatter(avx, avy, marker="x", c='blue')

plt.show()
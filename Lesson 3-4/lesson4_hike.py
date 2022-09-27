path = "Hike.txt"

def getDistance(x0:float, y0:float, x1:float, y1:float) -> float:
    dx = x1 - x0
    dy = y1 - y0
    return (dx**2 + dy**2)**0.5

def get3DDistance(x0:float, y0:float, z0:float, x1:float, y1:float, z1:float) -> float:
    dx = x1 - x0
    dy = y1 - y0
    dz = z1 - z0
    return (dx**2 + dy**2 + dz**2)**0.5

def getCoordingLists(path:str) -> tuple:
    X, Y, Z = [], [], []
    with open(path) as file:
        for row in file:
            sx, sy, sz = row.split(' ')
            X.append(float(sx))
            Y.append(float(sy))
            Z.append(float(sz))
    return (X, Y, Z)

def getLineStringLength2D(X: list, Y: list) ->float:
    s = 0.0
    for i in range(0, len(X)-1):
        s += getDistance(X[i], Y[i], X[i+1], Y[i+1])
    return s
def getLineStringLength3D(X: list, Y: list, Z:list) ->float:
    s = 0.0
    for i in range(0, len(X)-1):
        s += getDistance(X[i], Y[i], X[i+1], Y[i+1], Z[i], Z[i+1])
    return s

X, Y, Z = getCoordingLists(path)
print(getLineStringLength2D(X, Y))
print(getLineStringLength3D(X, Y, Z))



#read from file the 3 coordinates of each point
with open(path, 'r') as f:
    data = f.readlines()
    data = [x.strip().split(' ') for x in data]
    data = [[float(x[0]), float(x[1]), float(x[2])] for x in data]
    #calculate the distance between each point then add it to the total distance
    data = [((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)**0.5 for x,y in zip(data[1:], data[:-1])]
    print("Total Distance: ", sum(data))
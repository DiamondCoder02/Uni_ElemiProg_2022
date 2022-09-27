path = "Hike.txt"

#read from file the 3 coordinates of each point
with open(path, 'r') as f:
    data = f.readlines()
    data = [x.strip().split(' ') for x in data]
    data = [[float(x[0]), float(x[1]), float(x[2])] for x in data]
    #calculate the distance between each point then add it to the total distance
    data = [((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)**0.5 for x,y in zip(data[1:], data[:-1])]
    print("Total Distance: ", sum(data))
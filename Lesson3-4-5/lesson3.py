import matplotlib.pyplot as plt
import math


def test():
    plt.plot(math.sin(math.radians(i)) for i in range(0,360))
    plt.show()
test

"""
lst=[]
for i in range(0,360):
    #print(math.radians(i))
    lst.append(math.sin(math.radians(i)))

plt.plot(lst)
plt.show()
"""
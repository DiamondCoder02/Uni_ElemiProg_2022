import matplotlib.pyplot as plt


lst = []
print(type(lst))
print(lst)

lst.append('gay')
lst.append('horny')
lst.append(10)
lst.append(0.5)


print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print('-------------')
for value in lst:
    print(value)
print('-------------')
print(len(lst))
print('-------------')
print(lst.count(10))
print(lst.count("horny"))
print('-------------')
lst.remove(.5)
print(lst)
print('-------------')
#--------------------------------------
print('-------------')
lst22 = list()
lst2 = ['p','t','e']
print(lst2)
print(lst22)
print('-------------')
lst.extend(lst2)
print(lst)
print('-------------')


def thermoAvg(path):
    s=0.0
    flist=[]
    with open(path) as file:
        for row in file:
            v = float(row)
            flist.append(v)
            s += v
    av=s / len(flist)
    print(f"Átlag: {av}°C")

    s=0.0
    for value in flist:
        s += (value - av) ** 2
    st = (s / len(flist)) ** 0.5
    print(f'Szórás: {st}°C')

path = "thermo.txt"
thermoAvg(path)

print('-------------')
#--------------------------------------
print('-------------')
lista = [0,1,2]
print(sum(lista))
print('-------------')
#--------------------------------------
print('-------------')
plt.scatter(5,1)
plt.scatter(3,3)
print('-------------')
plt.plot([1,2,3], [3,6,4])
plt.scatter(3,5, marker='o', c="green")
print('-------------')
import math
for x in range(0,360):
    plt.scatter(x,math.sin(math.radians(x)))
plt.show()
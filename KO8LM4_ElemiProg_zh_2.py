#DiamondCoder 29.11.2022
import math
import matplotlib.pyplot as plt
import numpy as np

#exercise 1 (Done)
#convert array [0, 0, 7, 0, -1,] -> [(2, 7), (4, -1)]
print("\nExercise 1! Array convert!")
baseList = [0, 0, 7, 0, -1,]
def array_convert(array):
    newList = []
    for i in range(len(array)):
        if array[i] != 0:
            newList.append((i, array[i]))
    return newList
print(baseList)
print(array_convert(baseList))

#exercise 2 (Done)
#make a function that gets an array of numbers
print("\nExercise 2! Min-Max function!")
randomArray = [4,8,0,75,23,98,2,9,5]
def min_max(array):
    newArray = []
    mi = min(array)
    ma = max(array)
    for i in range(len(array)):
        newArray.append(float(array[i]-mi)/(ma-mi))
    return newArray
print(randomArray)
print(min_max(randomArray))

#exercise 3 (Done)
#read in file, skip first 6 line, then make it appear with matplotlib
print("\nExercise 3! File reading and matplotlib!")
fi = "slope.asc"
rowList = []
with open(fi, "r") as file:
    for i in range(6):
        next(file)
    for row in file:
        rowList.append(row.split())
    for i in range(len(rowList)):
        for j in range(len(rowList[i])):
            rowList[i][j] = float(rowList[i][j])
    plt.imshow(rowList)
    plt.show()

#exercise 4 (Done)
#from file calculate min max
print("\nExercise 4! Min-max with ASCII")
def convertDoubleListToList(doubleList):
    newList = []
    for row in doubleList:
        helpList = []
        for item in row:
            helpList.append(item)
        newList.append(helpList)
    return newList
uwu = convertDoubleListToList(rowList)
plt.imshow(uwu)
plt.show()
print(type(uwu))


#exercise 5 (Done)
#with function calculate f(x) = 1/(1+e^-10*(x-0.5)) at [0,1] with 0.001 step
print("\nExercise 5! f(x) = 1/(1+e^-10*(x-0.5))")
pltArray = []
def frick(x):
    return 1/(1+math.exp(-10*(x-0.5)))
for i in np.arange(0, 1, 0.001):
    pltArray.append(frick(i))
plt.plot(pltArray)
plt.show()

#exercise 6 
#array from exercise 4, calculate with frick function
print("\nExercise 6! WHY?")
pl=[]
for list1 in uwu:
    fer=[]
    for item in list1:
        fer.append(frick(item))
    pl.append(fer)

#plt.plot(uwu)
plt.imshow(pl)
plt.show()

print("\nDone!")
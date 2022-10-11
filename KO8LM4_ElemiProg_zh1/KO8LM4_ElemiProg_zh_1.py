#DiamondCoder 11.10.2022
import math
import matplotlib.pyplot as plt
pi=math.pi

#exercise 1 (done)
#ask for a number then calculate factorial
print("Exercise 1! Factorial")
n=int(input("Enter a number: "))
print("Factorial number is", math.factorial(n))

#exercise 2 (done)
#using matplotlib to draw a polygon from the numbers in text file
print("\n\n\nExercise 2! Making a polygon from file")
path = "sokszog.txt"
area=2116259486.700622 #area of the polygon
def polygon(path):
    with open(path, 'r') as file:
        lewd=[]
        cord=[]
        for row in file:
            x,y = row.split(',')
            x,y = float(x), float(y)
            lewd.append(x)
            cord.append(y)
            plt.plot(lewd,cord)
        #calculate perimeter of the polygon
        for i in range(0, len(lewd)-1):
            per=math.sqrt((lewd[i]-lewd[i+1])**2+(cord[i]-cord[i+1])**2)
        print("Perimeter: "+str(per)+' m')
        print("Area: "+str(area)+' m^2')
        c = ((4*pi*area) / (per**2))
        print("Compact or what: " + str(c))
    plt.show()
polygon(path)

#exercise 3 (done)
#ƒ(x) = x³ · sin x; x ∈ [-10π;  +10π]
print("\n\n\nExercise 3! Making a function")
horny=[]
meh=[]
mer=0
for i in range(-10*int(pi), 10*int(pi)):
    mer+=0.01
    l=(math.sin(i)*(i**3))+mer
    meh.append(i)
    horny.append(l)
    plt.plot(meh,horny)
plt.show()

#exercise 4(done)
#have an array of numbers and calculate those that can be divided by 3 and 2 without a remainder
print("\n\n\nExercise 4! Making an array")
arrayNumbers= [-15, 3.14, 6, 9, 73926, 396, 512, 1224, 3, 87, 102]
def divisibleBy3And2(numbers):
    newNum=[]
    for i in numbers:
        if i%3==0 and i%2==0:
            newNum.append(i)
    return newNum
print(divisibleBy3And2(arrayNumbers))

#exercise 5 (done, overcomplicated...)
print("\n\n\nExercise 5! Making a list")
path2="adatsor.txt"
def makeList(path2):
    with open(path2, 'r') as file:
        data = file.readlines()
        data = [int(x.strip()) for x in data if x.strip() != '-9999']
        print("done")
        return data
makeList(path2)
#print(makeList(path2))

#exercise 6 (done)
#make a function that reads the calculates the legth, min, max, average and standard deviation of the numbers in the file
print("\n\n\nExercise 6! Making a function")
def readNumbers(path2):
    with open(path2, 'r') as file:
        data = file.readlines()
        data = [int(x.strip()) for x in data if x.strip() != '-9999']
        return print("Length: "+str(len(data))+"\nAverage: "+str(sum(data)/len(data))+"\nMin: "+str(min(data))+"\nMax: "+str(max(data))+"\nStandard Deviation: "+str((sum([(x - sum(data)/len(data))**2 for x in data])/len(data))**0.5))
readNumbers(path2)

import matplotlib.pyplot as plt
import math

var = input("Number: ")

lst=[]
def printCollatz(x: int) -> list:
    while x!=1:
        x=x//2 if x%2==0 else 3*x+1
        lst.append(x)
        #print(x)
    return lst
#plt.plot(printCollatz(int(var)))
#plt.show()

def getLog10(lst: list) -> list:
    l1st=[]
    for x in lst:
        l1st.append(math.log10(x))
    #print(l1st)
    return l1st
#print(getLog10(lst))

def getOneCount(lst: list) -> int:
    n=0
    for i in lst:
        if str(i)[0]=='1':
            n+=1
    return n
#print(getOneCount(printCollatz(int(var))))

def getNumCount(lst: list) -> list:
    n = [0]*9
    for i in lst:
        n[int(str(i)[0])-1] +=1
    return n
#print(getNumCount(printCollatz(int(var))))

s=[]
for i in range(0,500):
    s.append(len(printCollatz(i)))
plt.plot(s)
plt.show()


"""
def printCollatz(x: int) -> None:
    while x!=1:
        x=x//2 if x%2==0 else 3*x+1
        
        print(x)

var = input("Number: ")
printCollatz(int(var))
"""
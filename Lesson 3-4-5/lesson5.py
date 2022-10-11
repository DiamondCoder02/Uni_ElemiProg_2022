#DiamondCoder 04.10.2022
import matplotlib.pyplot as plt
#xˇn+1=r*xˇn(1-xˇn)
x=0.4
temp=[]

print("Enter a number")
n=int(input("Years: "))
print("Nyulak vagy muslinca")
a=str(input("n/m? "))

if a=="n":
    r=2.85
    for i in range(n):
        x=r*x*(1-x)
        temp.append(x)
        print(i+1,"years: ",x)
        #plt.scatter(x, i)
elif a=="m":
    r=3.55
    for i in range(n):
        x=r*x*(1-x)
        temp.append(x)
        print(i+1,"years: ",x)
        #plt.scatter(x, i)

print(temp)
plt.plot(temp)
#plt.scatter(temp, i)
plt.show()


"""
TTK = "Természettudományi Kar"

print(TTK)
print(TTK[0:9])
print(TTK[0:9:2])
print(TTK[0:9])
print(TTK[::2])
print(TTK[0::2])
print(TTK[5:])
print(TTK[:6])
print("---------")
print(TTK[-1])
print(TTK[5:-1])
print(TTK[-2:5])
"""
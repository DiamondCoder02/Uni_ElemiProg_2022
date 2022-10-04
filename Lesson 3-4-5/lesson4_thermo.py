#CoderDiamond 27.09.2022
import matplotlib.pyplot as plt
path = "LongThermo.csv"

#print average, min, max, and standard deviation of the data in the file
#skip -9999 values
with open(path, 'r') as f:
    data = f.readlines()
    data = [float(x.strip()) for x in data if x.strip() != '-9999']
    print("Average: ", sum(data)/len(data))
    print("Min: ", min(data))
    print("Max: ", max(data))
    print("Standard Deviation: ", (sum([(x - sum(data)/len(data))**2 for x in data])/len(data))**0.5)
    
#plt.plot(data)
plt.show
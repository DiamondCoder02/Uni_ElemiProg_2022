#BORED

def thermoAvg(path):
    s=0.0
    n=0
    with open(path) as file:
        for row in file:
            s+=float(row)
            n+=1
    av=s/n
    print(f"Átlag: {av}°C")

    s=0.0
    with open(path) as file:
        for row in file:
            s += (float(row) - av) ** 2
    st = (s / n) ** 0.5
    print(f'Szórás: {st}°C')

path = "thermo.txt"
thermoAvg(path)
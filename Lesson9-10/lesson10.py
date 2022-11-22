#DiamondCoder 22.11.2022
import math
import matplotlib.pyplot as plt
import numpy as np

def normalizePressure(p: float, h: float) -> float:
    G=9.80665 # m/s^2
    T0=288.15 # K
    L=0.0065 # K/m
    M=0.0289644 # kg/mol
    R=8.31432 # J/(mol*K)

    C=(G*M)/(R*L)
    return p/(1.0-L*h/T0)**C

print(normalizePressure(978.1, 178.0))

def shiftList(lst: list, n: int) -> list:
    l=[None]*n
    l.extend(lst)
    return l

print(shiftList([1,3,'b'], 5))

def getArea(path: str) -> float:
    x_lst, y_lst = [], []
    with open(path) as file:
        for row in file:
            x, y, *_ = map(float, row.split(","))
            x_lst.append(x)
            y_lst.append(y)
    T=0.0
    for n in range(len(x_lst)-1):
        T+=0.5*(y_lst[n]+y_lst[n+1])*(x_lst[n+1]-x_lst[n])
    return abs(T)

print(f'T = {getArea("fish.csv") / (1000*1000)} m^2')




p=float('nan')
print(p)
print(math.isnan(p))
print(p==p)

class Point:
    @staticmethod
    def __checkFinite(v:float) -> None:
        if math.isnan(v) or math.isinf(v):
            raise ValueError(f"Value must be finite, got {v}")
    def __init__(self, x: float, y: float, z:float) -> None:
        Point.__checkFinite(x)
        Point.__checkFinite(y)
        Point.__checkFinite(z)
        
        self.X, self.Y, self.Z = x, y, z
    def __repr__(self) -> str:
        return f"Point({self.X}, {self.Y}, {self.Z})"
    
    def getDistance(self, other) -> float:
        dx, dy = self.X-other.X, self.Y-other.Y
        return (dx**2+dy**2)**0.5
    def getDistance(self, other) -> float:
        dx, dy, dz = self.X-other.X, self.Y-other.Y, self.Z-other.Z
        return (dx**2+dy**2+dz**2)**0.5

print(Point(1,2,3))
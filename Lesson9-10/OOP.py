#DiamondCoder 15.11.2022
from math import radians, tan, sin, cos
import matplotlib.pyplot as plt
import numpy as np

class GeoPoint:
    @staticmethod
    def __checkRange(val: float,
                   leftLimit: float,
                   rightLimit: float,
                   name: str) -> None:
        if not (leftLimit <= val <= rightLimit):
            raise ValueError(f"{name.capitalize()} must be in range {leftLimit} to {rightLimit}")
    def __init__(self, 
                 lon:float, #-180 to 180
                 lat:float) -> None: #-90 to 90
        self.__checkRange(lon, -180.0, 180.0, "Longitude")
        self.__checkRange(lat, -90.0, 90.0, "Latitude")
        
        self.Long = lon
        self.Lati = lat
    
    @classmethod
    def createFromString(cls, pointStr: str, sep: str=","):
        lon, lat, *_ = map(float, pointStr.split(sep))
        return cls(lon, lat)
    def asTuple(self) -> tuple:
        return (self.Long, self.Lati)
    
    def __repr__(self) -> str:
        return f"GeoPoint({self.Long}°, {self.Lati}°)"
    def __str__(self) -> str:
        return self.__repr__()
    @staticmethod
    def __checkType(__o: object) -> None:
        if not isinstance(__o, GeoPoint):
            raise TypeError(f"Expected GeoPoint object, got {type(__o)}")
    def __eq__(self, __o: object) -> bool:
        self.__checkType(__o)
        return self.Long == __o.Long and self.Lati == __o.Lati
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    def __add__(self, __o: object) -> "GeoPoint":
        self.__checkType(__o)
        return GeoPoint(self.Long + __o.Long, self.Lati + __o.Lati)
    
    @staticmethod
    def createPointList(path: str)->list:
        with open(path) as file:
            return list(map(GeoPoint.createFromString, file))

file="coordinates.csv"
#print(GeoPoint.createPointList(file))

#print(GeoPoint.createFromString("12.3, 45.6"))
"""
p = GeoPoint(33.5, 45.5)
t = GeoPoint(33.5, 45.5)
print(p)
print(str(p))
print(p==t)
"""

def centralPlainProjection(point: GeoPoint, 
                           R: float = 6371.0) -> tuple:
    lon, lat = point.asTuple()
    lon, lat = radians(lon-90.0), radians(90.0-lat)
    left = R * tan(lat)
    x = left * cos(lon)
    y = left * sin(lon)
    return (x, y)

x,y = [], []
gps = GeoPoint.createPointList(file)
for p in gps:
    x_, y_ = centralPlainProjection(p)
    x.append(x_)
    y.append(y_)

plt.plot(x, y)
plt.show()
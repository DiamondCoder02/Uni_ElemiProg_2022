#DiamondCoder 18.10.2022
import math
import matplotlib.pyplot as plt

dalia = plt.imread('dalia.jpg')
test = plt.imread('test.png')

def greyScale(rgbRaster):
    row, col, lay = rgbRaster.shape
    gray = rgbRaster.copy()
    for y in range(row):
        for x in range(col):
            pix = rgbRaster[y][x]
            gray[y][x] = (0.299*pix[0] + 0.584*pix[1] + 0.114*pix[2])
    return gray

gray = greyScale(dalia)

plt.imshow(gray)
plt.show()
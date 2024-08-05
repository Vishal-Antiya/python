import math

def circle(r):
    area = math.pi * (r ** 2)
    circumference = 2 * math.pi * r
    return area, circumference

print(circle(5))
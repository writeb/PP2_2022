from cmath import pi
import math
numberSides, lengthSide = int(input()), int(input())
a = lengthSide/(2*math.tan(math.pi/numberSides))
print(round(lengthSide*a*numberSides/2))
import math
radius = float(input())
def solve(r):
    volume = 4.0/3.0 * math.pi * (pow(r,3))
    return volume
print(solve(radius))
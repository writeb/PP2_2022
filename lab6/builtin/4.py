import time
import math
n = int(input())
mil = int(input())
d = math.sqrt(n)
time.sleep(mil/1000)
print(f'square root of {n} after {mil} milliseconds is {d}')
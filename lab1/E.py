n,f = map(int, input().split())
prime=0
from math import sqrt
for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime = 1
            break
if n<=500 and f%2==0 and prime==0:
    print("Good job!")
else: print("Try next time!")
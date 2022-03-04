a,b = int(input()), int(input())
d = (i**2 for i in range(a,b))
for i in d: print(i)
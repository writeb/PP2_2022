def rev(n):
    while n!=0:
        yield (n+1) -1
        n-=1
a = rev(int(input()))
for i in a: print(i)
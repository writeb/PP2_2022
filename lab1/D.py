n=int(input())
c=input()
if c=='b':
    print(n*1024)
elif c=='k':
    if (n/1024) is int: print(n/1024)
    else: print(round(n/1024,int(input())))
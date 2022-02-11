n = int(input())
m=n
for n1 in range(0,n):
    for m1 in range(0,m):
        if n1 == m1:
            print(n1*m1,end=" ")
        elif n1 == 0:
            print(m1,end=" ")
        elif m1==0:
            print(n1,end=" ")
        else:
            print("0",end=" ")
    print()

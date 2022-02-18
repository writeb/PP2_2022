def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

a = input().split()
for i in a :
    if prime(int(i)) :
        print(i,end = " ")
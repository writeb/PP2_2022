a=input().split()
b=[]
xor=0

for i in range(len(a)): b.append(int(a[i]))
arr=[0]*b[0]
if len(b)==2:
    for i in range(b[0]):
        arr[i]=(b[1]+2*i)
        xor^=arr[i]
else:
    x=int(input())
    for i in range(b[0]):
        arr[i]=(x+2*i)
        xor^=arr[i]

print(xor)
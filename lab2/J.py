n=int(input())
lt=[]
for i in range(n):
    s=input()
    if any(chr.isdigit() for chr in s):
        if any(chr.isupper() for chr in s):
            if any(chr.islower() for chr in s):
                lt.append(s)
    else: continue
mylist=list(dict.fromkeys(lt))
print(len(mylist))
mylist.sort()
for i in range(len(mylist)):
    s=str(mylist[i])
    print(s)

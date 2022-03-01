s=input().split()
new=[]
for i in s:
    if len(i)>=3:
        new.append(i)
print(' '.join(new))
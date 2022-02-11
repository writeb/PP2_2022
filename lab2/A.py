ls = list(map(int, input().split()))
count = 0
b = True
for ar, i in enumerate(ls):
    count = max(count - 1, i)       
    if count <= 0:
        if ar != len(ls)-1:
            b=False
        break
if b: print(1)
else: print(0)
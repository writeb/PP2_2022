ls=[]
while True:
    s = input()
    if s == "0":
        break
    ls.append(s.split())
for i in range(len(ls)):
    ls[i].reverse()
ls.sort()
for i in range(len(ls)):
    ls[i].reverse()
    p = ls[i]
    print(p[0], p[1], p[2])
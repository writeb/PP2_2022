s=input()
t=input()
if s.count(t)==1:
    print(s.index(t))
elif s.count(t)>=2:
    print(s.index(t), end=" ")
    print(s.rindex(t))
else:
    pass

    
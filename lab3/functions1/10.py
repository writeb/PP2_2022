l = list(map(int, input().split()))
def unique(l):
    newl = []
    for i in l:
        if i not in newl:
            newl.append(i)
    return newl
print(unique(l))
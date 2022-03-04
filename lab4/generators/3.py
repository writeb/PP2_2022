n = int(input())
def check():
    for i in range(n):
        if i%3==0:
            if i%4==0:
                yield i
x = check()
for i in x: print(i)
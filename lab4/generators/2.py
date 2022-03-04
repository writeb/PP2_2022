n = int(input())
def check_even():
    for i in range(n):
        if i%2==0: yield i
x = check_even()
for i in x: print(i)
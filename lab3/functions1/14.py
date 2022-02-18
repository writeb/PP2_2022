num = int(input())
if num==1:
    def converter(ounces):
        return 28.3495231 / ounces
    print(converter(int(input())))
elif num==2:
    def conventer(f):
        c = (5 / 9) * (f - 32)
        return c
    print(conventer(int(input())))
elif num==3:
    def histogram(a):
        for i in a:
            for j in range(i):
                print("*",  end = "")
            print(" ")
    l = list(map(int,input().split()))
    histogram(l)
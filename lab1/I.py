n=int(input())
for i in range(n):
    s=input()
    if "@gmail.com" in s:
        print(s.replace("@gmail.com", ""))
    else:
        pass
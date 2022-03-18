import os
def rec(name, n):
    for i in os.listdir(n):
        target = os.path.join(n,i)
        if os.path.isfile(target) and i == name:
            print(name)
            print(target)
            exit()
        elif os.path.isdir(target):
            rec(name, target)
DIR = os.getcwd()
a = input()
rec(a, DIR)
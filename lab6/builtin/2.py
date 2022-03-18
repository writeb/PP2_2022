s = input()
def solve(s):
    dt = {'upper':0, 'lower':0}
    for i in s:
        if i.isupper(): dt['upper']+=1
        elif i.islower(): dt['lower']+=1
        else: pass
    print('num of the upper case: ', dt['upper'])
    print('num of the lower case: ', dt['lower'])
solve(s)
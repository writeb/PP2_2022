lt = [str(n**2) for n in range(10)]
n = ' '.join(lt)
f = open('test.txt', 'a')
f.write('\n'+n)

with open('test.txt', 'r') as f:
    s = f.read()
print(s)
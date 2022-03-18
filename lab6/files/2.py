import os

print(os.path.exists('text.txt'))

if os.path.exists('text.txt'):
    f = open('text.txt', 'r')
    print(f.read())
    with open ('text.txt', 'a') as i:
        i.write('Hello')
with open('test.txt', 'r') as f:
    text = f.read()
wr = open('copy.json', 'w')
wr.write(text)
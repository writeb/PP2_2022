import re
text = input()
pattern = ''.join(i.capitalize() for i in text.split('_'))
print(pattern)
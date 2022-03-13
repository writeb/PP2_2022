import re
text = input()
pattern = re.sub('(\w)([A-Z])', r'\1 \2', text)
print(pattern)
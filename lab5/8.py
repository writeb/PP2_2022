import re
text = input()
pattern = re.findall('[A-Z][^A-Z]*', text)    
print(pattern)
import re
def check(text):
    pattern = '[A-Z]+[a-z]+$'
    if re.search(pattern, text): return 'match'
    else: return 'not match'
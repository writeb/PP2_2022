import re
def check(text):
    pattern = 'ab{2,3}'
    if re.search(pattern, text): return 'match'
    else: return 'not match'
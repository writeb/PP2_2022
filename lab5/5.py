import re
def check(text):
    pattern = 'a.*?b$'
    if re.search(pattern, text): return 'match'
    else: return 'not match'
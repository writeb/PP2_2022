import re
def check(text):
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern, text): return 'match'
    else: return 'not match'
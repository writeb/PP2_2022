s = input()
s1 = s[::-1]
def solve(s):
    if s1 == s: return True
    return False
print(solve(s))
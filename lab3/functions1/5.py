import itertools as it
def solve():
    s = input()
    n = list(s)
    perm = list(it.permutations(n))
    for i in perm: print("".join(i))
solve()
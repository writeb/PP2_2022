s=input()
#print(s.lower())
def toLowercase():
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z':
            s[i]=chr(ord(s[i])+32)
s=list(s)
toLowercase()
s=''.join(s)
print(s)
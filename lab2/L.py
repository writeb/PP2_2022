def check(s):
	brackets = ['()', '{}', '[]']
	while any(i in s for i in brackets):
		for br in brackets:
			s = s.replace(br, '')
	return not s

s = input()
if check(s): print("Yes")
else: print("No")
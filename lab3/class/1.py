class MyString:
    def __init__(self):
        self.str1 = ""
    def getString(self): self.str1=input()
    def printString(self): return self.str1.upper()
s1 = MyString()
s1.getString()
print(s1.printString())
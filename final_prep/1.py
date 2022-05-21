'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
* Set items are unchangeable, but you can remove and/or add items whenever you like.
Python Numbers
{   
    3 numeric types:
        int, float, complex(always with 'j')
    Random number:
        random.randrange(1,10) - means 1 - 9
}
Python Strings
{
    Check string:
        txt = "The best things in life are free!"
        print("free" in txt)    
        txt = "The best things in life are free!"
        if "expensive" in txt:      # also 'not in'
            print(' 'expensive' is present.')
    Slicing:
        a = 'hello world'
        print(a[2:5])
        print(a[:5]) - from the start
        print(a[2:]) - to the end
        print(a[::-1]) - reverse 
    Methods:
        strip() - removes whitespaces from beginning or the end
        split() - returns a list
        format() - always with {} in the string
    Escape chr:    
        txt = 'We are the so-called \'Vikings\' from the north.' - без '\' будет ошибка
}
Python Booleans
{
    False:
        bool(False)
        bool(None)
        bool(0)             # другое все True
        bool("")
        bool(())
        bool([])
        bool({})
    isinstance() - to determine if an object is of a certain data type:
}
Python Lists
{
    Functions:
        append(), insert(index, item) - for adding
        extend() 
        remove(), pop(index) - for removing
        pop(без индекса) - removes last item
        keyword - del
        clear()
        sort(), sort(reverse = True), sort(key = 'any function(def)'), sort(key = (str.lower()))
        reverse()
        copy()
}
Python Tuples
{
    Python has two built-in methods that you can use on tuples.
    
}
'''

from re import A
from urllib.parse import quote_plus


# strings is a datatype in python enclosed in quotes
a = 34
print(type(a))
b = 'shlok'
c = "shlok'"  # use this if you have single quotes in your strings
print(c)
d = '''shlok"'''  # use this if you have double quotes in a string
print(type(a), type(b), type(c))
e = c+d
print(e)  # concatinating the strings
name = "shlok"
print(len(name))
print(name[0])  # slicing
# name[4]="d"     #This is not allowed like int the arrays , this is not allowed
print(name[0:5])  # print 0,1,2 index , index is from 0 to length minus 1
# negative index can also be used..-1 index is the element at length-1
print(name[-1])
print(name[-4:-1])  # will print -4,-3,-2 indexes

dart = name[0: 5: 2]
dart = name[-5: -1: 2]
print(dart)
story = "my name is shlok agarwal and i like playing badminton"
print(len(story))
print(story.endswith("badmintn"))

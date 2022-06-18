# varaiable is the name given to a memory location in a program
# variable is container to store a value
from textwrap import indent

from sklearn.tree import plot_tree
import numpy as np

arr = np.zeros((2, 2))
print(arr)
a = 333
a *= 12
b = 44.99
print(type(b))

d = None
# print(a)
c = "shlok"
a = '''"shlok"'''  # To print doubles quotes as a string and to print multiple lines we use triple quotes
print(a)
print(type(d))
print("the value of 3+4 is ", 3+4)  # Arithmetic operators

b = (4 > 7)
print(b)

bool1 = True
bool2 = False
print("The value of bool1 is", (not bool2))
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
a2 = "4444"
print(type(a2))
a2 = int(a2)  # we can convert a string to a number if the string is a valid number
print("a2", a2+5)

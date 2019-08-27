import string
from random import randint
str1 = string.printable
for i in range(8):
    print(str1[randint(0,len(str1))],end="")

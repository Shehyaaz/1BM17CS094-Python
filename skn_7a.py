# Program 7a
'''
A prime no. is a natural no. that has exactly two distinct natural no. divisors:
1 and itself.
A happy no. is a no. that leads to 1 after a sequence of steps where in each
step the no. is replaced by sum of squares of its digits.
'''
try :
    file1 = open("prime.txt","r")
    file2 = open("happy.txt","r")
    prime_str = file1.read()
    happy_str = file2.read()
    prime = prime_str.split(", ")
    happy = happy_str.split(", ")
    lst3 = [int(val) for val in prime if val in happy] #using list comprehension
    print("Overlapping numbers :")
    print(lst3)
    file1.close()
    file2.close()
except IOError :
    print("Files not found")
#end of program

'''OUTPUT :
Overlapping numbers :
[7, 13, 19, 23, 31, 79, 97, 103, 109, 139, 167, 193, 239, 263, 293,
313, 331, 367, 379, 383, 397, 409, 487,563, 617, 653, 673, 683, 709,
739, 761, 863, 881, 907, 937]
'''

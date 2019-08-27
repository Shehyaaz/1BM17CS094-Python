def printDiv( num ):
    print(1)
    for i in range(2,int(num/2) + 1):
        if num % i == 0 : print(i)
    print(num)

printDiv(int(input("Enter the number :")))

''' A python program to print n fibonacci numbers '''
def inputNum():
    return int(input("Enter number of elements (greater than 2):"))

def fib(n):
    if n == 1:
        print(0)
    else :
        fibList = [0,1]
        for i in range(2,n):
            fibList.append(fibList[i-2]+fibList[i-1])
        print(fibList)
            
fib(inputNum())

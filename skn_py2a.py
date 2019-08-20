def search(lis, key):
    if key in lis:
        print("Present in list")
    else :
        print("Not present in list")

lis = []
while True:
    a = int(input("Enter the element : "))
    if a!= -1:
        lis.append(a)
    else :
        break
key = int(input("Enter the element to be searched : "))
search(lis,key)
                

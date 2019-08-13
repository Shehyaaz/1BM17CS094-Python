''' A python program to take a list of items and makes a new list that has only
    even elements
'''

def inputList():
    list1 = []
    while True:
        item = int(input("Enter list items (-1 to exit):"))
        if item == -1:
            break
        else :
            list1.append(item)
    return list1

def newList():
    list1  = inputList()
    list2 = [x for x in list1 if not(x & 1)]
    print(list2)

# this program prints all elements at even position in the list
def inputList():
  list1 = []
  while True :
    item = int(input("Enter element(-1 to exit):"))
    if item == -1: break
    else : list1.append(item)
  return list1
  
def newList():
  list1 = inputList()
  for x in range(len(list1)):
    if not(x+1 & 1): print(list1[x],sep = ' ')
    
 newList()

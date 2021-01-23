from typing import Any

myUniqueList = []
myLeftovers = []


def list_adder(el:Any) -> bool:
 
    if el not in myUniqueList:
        myUniqueList.append(el)
        return(True)
    else:
        myLeftovers.append(el)
        return(False)

# printing section
for el in (1, 2, '1', 2):
    print(el, list_adder(el))
    
    
print(myUniqueList)
print(myLeftovers)



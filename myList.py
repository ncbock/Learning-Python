myUniqueList = []
myLeftOvers = []

def addToList (aValue):
	if aValue not in myUniqueList:
		myUniqueList.append(aValue)
		return True
	addToLeftOvers(aValue)
	return False

def addToLeftOvers (listElem):
	myLeftOvers.append(listElem)
	return

addToList(1)
addToList(2)
addToList("neil")
addToList(3)
addToList("john")
addToList("neil")
addToList(5)
addToList(2)
addToList("john")
addToList(1)
addToList(2)
addToList(3)
addToList(5)
addToList("steve")

print(myUniqueList)
print(myLeftOvers)

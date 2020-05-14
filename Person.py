"""this is our person class"""
personArray = []
class Person:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		self.left = None
		self.right = None
		self.parent = None
		self.gen = 1

def addtoPersonArray(name, age, sex):
	personArray.append(Person(name, age, sex))

def returnPerson():
	return personArray

def findPerson(name):
    for i in personArray:
        if name == i.name:
            return i

def changeName(origname, newname):
	if findPerson(newname) == None:
		findPerson(origname).name = newname
		print(origname + "'s name has been changed to " + newname)
	else:
		print("Error: name " + newname + " already in use. Please change to another name.")

def changeAge(origname, newage):
	for i in personArray:
		if origname == i.name:
			i.age = newage
			print(origname + "'s age has been changed to " + newage)

def changeSex(origname, newsex):
	for i in personArray:
		if origname == i.name:
			if newsex.lower() == "false":
				i.sex = False
				print(origname + "'s sex has been changed to female")
			elif newsex.lower() == "true":
				i.sex = True
				print(origname + "'s sex has been changed to male")

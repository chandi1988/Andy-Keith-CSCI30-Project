"""person class and searching example"""
personArray = []
class Person:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

def addtoPersonArray(name, age, sex):
	personArray.append(Person(name, age, sex))

def returnPersonArray():
	return PersonArray


"""getting age and name, changing age and name from an array of classes in cmd"""
"""
while True:
	p = input()
	q =  p.split(" ",2)
	existence = False
	if p == "bye":
		break
	elif q[0] == "count":
		print(len(personlist))
	elif q[0] == "age":
		for person in personlist:
			if q[1] in person.name:
				print( "%s is %s years old" % (person.name, person.age))
				existence = True
		if existence == False:
			print("there aint nobody named " + q[1])
		existence = False
	elif q[0] == "sex":
		for person in personlist:
			if q[1] in person.name:
				if person.sex == True:
					print( "%s is Male" % (person.name))
				elif person.sex == False:
					print( "%s is Female" % (person.name))
				existence = True
		if existence == False:
			print("there aint nobody named " + q[1])
		existence = False
	elif q[0] == "edit-age":
		for person in personlist:
			if q[1] in person.name:
				print( "%s changed to %s" % (person.name, q[2]))
				person.name = q[2]
				existence = True
		if existence == False:
			print("there aint nobody named " + q[1])
		existence = False
	elif q[0] == "edit-age":
		for person in personlist:
			if q[1] in person.name:
				print( "%s\'s age is changed from %s to %s" % (person.name, person.age, q[2]))
				person.age = int(q[2])
				existence = True
		if existence == False:
			print("there aint nobody aged " + q[1])
		existence = False
	elif q[0] == "edit-sex":
		for person in personlist:
			if q[1] in person.name:
				print( "%s\'s sex is changed" % (person.name))
				if (q[2]) == "False":
					person.sex = False
				elif q[2] == "True":
					person.sex = True
				existence = True
		if existence == False:
			print("there aint nobody named " + q[1])
		existence = False
	elif q[0] == "enumdeets":
		for person in personlist:
			print("%s - %s" % (person.name, person.age))
"""

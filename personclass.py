#person class and searching example
class Person:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex 
		
personlist = [] 
personlist.append(Person("Carlana", 20, "true"))
personlist.append(Person("Bobby", 18, "false"))
personlist.append(Person("Sasha", 25, "false"))
personlist.append(Person("Keithy", 18, "true"))
"""
print(personlist[0].name)

look = 'false'
for person in personlist:
    if look in person.sex:
        # title() capitalizes the job's first letter
        print( "%s %s: \"%s\"" % (person.sex.title(), person.name, person.age))
		
for person in personlist:
    if 18 == person.age:
        print( "%s: \"%s\"" % (person.name, person.age))
"""
#getting age and name, changing age and name from an array of classes
while True: 
	p = input()
	q =  p.split(" ",2)
	if p == "end":
		break
	elif q[0] == "changename":
		for person in personlist:
			if q[1] in person.name:
				print( "%s changed to %s" % (person.name, q[2]))
				person.name = q[2]
			else:
				print("there aint nobody named " + q[1])
	elif q[0] == "changeage":
		for person in personlist:
			if q[1] in person.name:
				print( "%s\'s age is changed from %s to %s" % (person.name, person.age, q[2]))
				person.age = int(q[2])
			else:
				print("there aint nobody aged " + q[1])
	elif q[0] == "checkage":
		for person in personlist:
			if int(q[1]) == person.age:
				print( "%s: \"%s\"" % (person.name, person.age))
			else:
				print("there aint nobody aged " + q[1]) 
	elif q[0] == "enumnames":			
		for person in personlist:		
			print(person.name)
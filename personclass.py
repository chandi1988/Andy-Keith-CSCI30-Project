#person class and searching example
class Person:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex 
		
personlist = [] 
personlist.append(Person("Carlana", 20, "Female"))
personlist.append(Person("Bobby", 18, "Male"))
personlist.append(Person("Sasha", 25, "Female"))
personlist.append(Person("Keithy", 18, "Male"))

print(personlist[0].name)

look = 'Female'
for person in personlist:
    if look in person.sex:
        # title() capitalizes the job's first letter
        print( "%s %s: \"%s\"" % (person.sex.title(), person.name, person.age))
		
for person in personlist:
    if 18 == person.age:
        print( "%s: \"%s\"" % (person.name, person.age))
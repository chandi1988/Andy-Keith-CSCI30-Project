from Person import *
from Relations import *
from TreeFunctions import *

while True:
	ipt = input(">")
	if ipt.lower() == "bye":
		print("Goodbye!")
		break
	elif ipt.split()[0].lower() == "load":
		try:
			returnPerson().clear()
			getLinkIn().clear()
		
			FamTreeLoad(ipt.split()[1])
			makeTree()
			if len(returnPerson()) != 0:
				print(ipt.split()[1] + ".ft has been loaded!!!")
		except:
			if getError() == True:
				editError(False)
				pass
			else:
				print("Error: file does not exist")
	elif ipt.split()[0].lower() == "save":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		else:
			saveFamTree(ipt.split()[1])
			print("Family Tree has been updated!")
	elif ipt.split()[0].lower() == "count":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		else:
			print(len(returnPerson()))
	elif ipt.split()[0].lower() == "age":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		elif findPerson(ipt.split()[1]) == None:
			print("Error: no such person as " + ipt.split()[1] + " in " + getFamName() +" family")
		else:
			print(findPerson(ipt.split()[1]).age)
	elif ipt.split()[0].lower() == "sex":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		elif findPerson(ipt.split()[1]) == None:
			print("Error: no such person as " + ipt.split()[1] + " in " + getFamName() +" family")
		else:
			if findPerson(ipt.split()[1]).sex == True:
				print("Male")
			elif findPerson(ipt.split()[1]).sex == False:
				print("Female")
	elif ipt.split()[0].lower() == "ancestors":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		elif findPerson(ipt.split()[1]) == None:
			print("Error: no such person as " + ipt.split()[1] + " in " + getFamName() +" family")
		else:
			listAncestors(ipt.split()[1]) 
	elif ipt.split()[0].lower() == "descendants":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		elif findPerson(ipt.split()[1]) == None:
			print("Error: no such person as " + ipt.split()[1] + " in " + getFamName() +" family")
		else:
			returnDescendants(ipt.split()[1])
	elif ipt.split()[0].lower() == "edit-name":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		elif findPerson(ipt.split()[1]) == None:
			print("Error: no such person as " + ipt.split()[1] + " in " + getFamName() +" family")
		else:
			changeName(ipt.split()[1],ipt.split()[2])
	elif ipt.split()[0].lower() == "edit-age":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		elif findPerson(ipt.split()[1]) == None:
			print("Error: no such person as " + ipt.split()[1] + " in " + getFamName() +" family")
		else:
			changeAge(ipt.split()[1],ipt.split()[2])
	elif ipt.split()[0].lower() == "edit-sex":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		elif findPerson(ipt.split()[1]) == None:
			print("Error: no such person as " + ipt.split()[1] + " in " + getFamName() +" family")
		else:
			changeSex(ipt.split()[1],ipt.split()[2])
	elif ipt.split()[0].lower() == "relationship":
		if len(returnPerson()) == 0:
			print("Error: a family tree must be loaded in the current session first")
		else:
			try:
				if ipt.split()[1] == ipt.split()[2]:
					print("Error: inputs must be distinct")
				else: 
					print(relationship(ipt.split()[1], ipt.split()[2]))
			except:
				print("Error: input(s) are nonexistent, please fix and try again")
	else: 
		print("Error: unrecognized keyword \"" + ipt.split()[0] + "\"")
	
	
	
	
	
	
	
	
	
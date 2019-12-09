from Person import *
from Relations import *

firsterror = False
def getError():
	return firsterror
def editError(n):
	firsterror = n
	
def FamTreeLoad(familyName):
	with open(familyName+".ft", "r") as file:
		line = file.readline()
		while line:
			lineSplit = line.split()
			if lineSplit[0] == "family":
				famName(lineSplit[1])
			elif lineSplit[0] == "count":
				 (int(lineSplit[1]))
			elif lineSplit[0] == "links":
				numLinks(int(lineSplit[1]))
			elif lineSplit[0] == "name":
				try:
					name = lineSplit[1]
					age = int(file.readline().split()[1])
					n = file.readline().split()
					if n[1].lower() == "true":
						sex = True
					else:
						sex = False
					addtoPersonArray(name, age, sex)
				except:
					global firsterror
					firsterror = True
					print("Error: person details are insufficient")
			elif lineSplit[0] == "child":
				linkIn(str(line).rstrip('\n'))
			line = file.readline()
			
	returnPerson()[0].isroot = True
	
	if (len(returnPerson()) != getNumPerson()):
		returnPerson().clear()
		getLinkIn().clear()
		print("Error: declared \"count\" does NOT match number of person entries")
	elif (getNumLinks() != len(getLinkIn())):
		returnPerson().clear()
		getLinkIn().clear()
		print("Error: declared \"links\" does NOT match number of relationship entries")
	elif len(getLinkIn()) > (len(returnPerson()) - 1):
		returnPerson().clear()
		getLinkIn().clear()
		print("Error: family tree is ill-formed; check if cycles are present")
	elif len(getLinkIn()) < (len(returnPerson()) - 1):
		returnPerson().clear()
		getLinkIn().clear()
		print("Error: family tree is disconnected; check for orphans")



def makeTree():
	habalnk = len(getLinkIn())	
	while habalnk > 0:
		for i in returnPerson():
			bilang = 0
			while bilang < len(getLinkIn()):
				if (i.name == links[bilang].split()[1]):
					if i.left == None:
						leftchild = str(links[bilang].split()[2])
						if findPerson(leftchild).isroot == True:
							print("Error: Cannot set root node of a family tree as a child.")
							returnPerson().clear()
							getLinkIn().clear()
							break
						i.left = findPerson(leftchild)
						findPerson(leftchild).parent = i
						findPerson(leftchild).gen = i.gen + 1
					elif i.right == None:
						rightchild = str(links[bilang].split()[2])
						if findPerson(rightchild).isroot == True:
							print("Error: Cannot set root node of a family tree as a child.")
							returnPerson().clear()
							getLinkIn().clear()
							break
						i.right = findPerson(rightchild)
						findPerson(rightchild).parent = i
						findPerson(rightchild).gen = i.gen + 1
			
				elif findPerson(links[bilang].split()[1]) == None or findPerson(links[bilang].split()[2]) == None:
					if firsterror == True:
						firsterror == False
						pass
					else:
						print("Error: attempted to link nonexistent person(s). Load and try again.")
						returnPerson().clear()
						getLinkIn().clear()
					
				bilang += 1
		habalnk -= 1
		

def leastCommonAncestor(n1, n2):
    g1 = findPerson(n1).gen
    g2 = findPerson(n2).gen
    p1 = findPerson(n1)
    p2 = findPerson(n2)
    while True:
        if p1.parent == None:
            return p1
            break
        elif p2.parent == None:
            return p2
            break
        elif g1 == g2:
            if p1.parent == p2.parent:
                return p1.parent
                break
            else:
                p1 = p1.parent
                p2 = p2.parent
                g1 = p1.gen
                g2 = p2.gen
                while True:
                    if p1.parent == p2.parent:
                        return p1.parent
                        break
                    else:
                        p1 = p1.parent
                        p2 = p2.parent
                        g1 = p1.gen
                        g2 = p2.gen
        elif g1 > g2:
            while g1 != g2:
                p1 = p1.parent
                g1 = p1.gen
            if p1 == p2:
                return p2
            elif p1.parent == p2.parent:
                return p1.parent
                break
            else:
                p1 = p1.parent
                p2 = p2.parent
                g1 = p1.gen
                g2 = p2.gen
                while True:
                    if p1.parent == p2.parent:
                        return p1.parent
                        break
                    else:
                        p1 = p1.parent
                        p2 = p2.parent
                        g1 = p1.gen
                        g2 = p2.gen
        elif g2 > g1:
            while g2 != g1:
                p2 = p2.parent
                g2 = p2.gen
            if p2 == p1:
                return p1
            elif p1.parent == p2.parent:
                return p1.parent
                break
            else:
                p1 = p1.parent
                p2 = p2.parent
                g1 = p1.gen
                g2 = p2.gen
                while True:
                    if p1.parent == p2.parent:
                        return p1.parent
                        break
                    else:
                        p1 = p1.parent
                        p2 = p2.parent
                        g1 = p1.gen
                        g2 = p2.gen

def listAncestors(name):
	list = []
	p1 = findPerson(name)
	while p1.gen > 1:
		p1 = p1.parent
		list.append(p1.name)
	list.sort()
	for i in list:
		print(i)
	if len(list) == 0:
		print("no ancestors")
	
fDescent = []
def listDescendants(name):
	descent = []
	p = findPerson(name).left
	if p:
		descent.append(p.name)
		try:
			descent = descent + listDescendants(str(p.name))
		except:
			True
        
	q = findPerson(name).right
	if q:
		descent.append(q.name)
		try:
			descent = descent + listDescendants(str(q.name))
		except:
			True
    
	descent.sort()
	global fDescent
	fDescent = descent
	return descent

def returnDescendants(name):
	listDescendants(name)
	for i in fDescent:
		print(i)
	if len(fDescent) == 0:
		print("no descendants")


def relationship(ppp1,ppp2):
    Ordinal = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    Times = ["", "once", "twice", "thrice", "four times", "five times", "six times", "seven times", "eight times", "nine times", "ten times"]
    Great = ["", "", "great-", "great-great-", "great-great-great-","great-great-great-great-", "great-great-great-great-great-", "great-great-great-great-great-great-", "great-great-great-great-great-great-great-", "great-great-great-great-great-great-great-great-", "great-great-great-great-great-great-great-great-great-"]
    p1 = findPerson(ppp1)
    p2 = findPerson(ppp2)
    l = leastCommonAncestor(ppp1,ppp2)
    l1 = l.gen
    d1 = (p1.gen - l1)
    d2 = (p2.gen - l1)

    nearest = min(d1, d2)
    furthest = max(d1, d2)

    if nearest >= 2:
        degree = (nearest - 1)
        removal = abs(d1 -d2)
        if removal == 0:
            return str(Ordinal[degree] + " cousin")
        else:
            return str(Ordinal[degree] + " cousin, " + Times[removal] + " removed")
    elif nearest == 1:
        if furthest == 1:
            if p2.sex == True:
                return "brother"
            else:
                return "sister"
        elif furthest == 2:
            return Term("nibling", d1, d2, p2.sex)
        else:
            return str(Great[furthest - 3] + "grand" + Term("nibling", d1, d2, p2.sex))
    elif nearest == 0:
        if furthest == 1:
            return Term("child", d1, d2, p2.sex)
        else:
            return str(Great[furthest - 2] + "grand" + Term("child", d1, d2, p2.sex))


def Term(kind, d1, d2, sex):
    if d1 < d2:
        if kind == "child":
            if sex == True:
                return "son"
            else:
                return "daughter"
        else:
            if sex == True:
                return "nephew"
            else:
                return "niece"
    elif d1 > d2:
        if kind == "child":
            if sex == True:
                return "father"
            else:
                return "mother"
        else:
            if sex == True:
                return "uncle"
            else:
                return "aunt"

def saveFamTree(famname):
	file = open(famname + ".ft", "w")
	file.write("family " + str(getFamName()) + "\n")
	file.write("count " + str(getNumPerson()) + "\n")
	for i in returnPerson():
		file.write("name " + str(i.name) + "\n")
		file.write("age " + str(i.age) + "\n")
		file.write("sex " + str(i.sex).lower() + "\n")
	file.write("links " + str(getNumLinks()) + "\n")
	for i in returnPerson():
		try:
			if i.left != None:
				file.write("child " + str(i.name) + " " + str(i.left.name) + "\n")
			if i.right != None:
				file.write("child " + str(i.name) + " "  + str(i.right.name) + "\n")
		except:
			True
	file.close()
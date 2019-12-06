from personclass import *
from relationclass import *

def FamTreeLoad(familyName):
    with open(familyName+".ft", "r") as file:
        line = file.readline()
        while line:
            lineSplit = line.split()
            if lineSplit[0] == "family":
                famName(lineSplit[1])
            elif lineSplit[0] == "count":
                numPerson(int(lineSplit[1]))
            elif lineSplit[0] == "links":
                numLinks(int(lineSplit[1]))
            elif lineSplit[0] == "name":
                name = lineSplit[1]
                age = int(file.readline().split()[1])
                n = file.readline().split()
                if n[1] == "true":
                    sex = True
                else:
                    sex = False
                addtoPersonArray(name, age, sex)
            elif lineSplit[0] == "child":
                linkIn(str(line).rstrip('\n'))
            line = file.readline()

def makeTree():
    habalnk = len(getLinkIn())
    while habalnk > 0:
        #print("k")
        for i in returnPerson():
            #print(i.name)
            #print("lol")
            bilang = 0
            while bilang < len(getLinkIn()):
                #print("g")
                #print(i.name, links[bilang].split()[1])
                if i.name == links[bilang].split()[1]:
                    #print("etits")
                    if i.left == None:
                        leftchild = str(links[bilang].split()[2])
                        #print(findPerson(leftchild))
                        i.left = findPerson(leftchild)
                        #print(i.left)
                    elif i.right == None:
                        i.right = findPerson(links[bilang].split()[2])
                        print("nen")
                bilang += 1
        habalnk -= 1

fam = input()
if fam.split()[0] == "load":
    FamTreeLoad(fam.split()[1])
    makeTree()
print(returnPerson()[2].left.name)

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
                        i.left = findPerson(leftchild)
                        findPerson(leftchild).parent = i
                        findPerson(leftchild).gen = i.gen + 1
                    elif i.right == None:
                        rightchild = str(links[bilang].split()[2])
                        i.right = findPerson(rightchild)
                        findPerson(rightchild).parent = i
                        findPerson(rightchild).gen = i.gen + 1

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

fam = input()
if fam.split()[0] == "load":
    FamTreeLoad(fam.split()[1])
    makeTree()
print(leastCommonAncestor("Patricia", "Juan").name)

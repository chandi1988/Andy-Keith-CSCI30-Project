from personclass import *

familyName = ""
countPerson = 0
countLink = 0
links = []

class makeTree:
    def __init__(self, root):
        self.root = returnPerson()[0]

def findPerson(name):
    for i in returnPerson():
        if name == i.name:
            return i

def famName(n):
    global familyName
    familyName = n
def getFamName():
    return familyName

def numPerson(n):
    global countPerson
    countPerson = n
def getNumPerson():
    return countPerson

def numLinks(n):
    global countLink
    countLink = n
def getNumLinks():
    return countLink

def linkIn(n):
    global links
    links.append(n)
def getLinkIn():
    return links

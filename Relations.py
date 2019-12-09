from Person import *

"""This is Relations! This is where we store values from reading the .ft file into actual data"""

familyName = ""
countPerson = 0
countLink = 0
countNames = 0

links = []

"""this function obtains the family's name from FamTreeLoad"""
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
	

	

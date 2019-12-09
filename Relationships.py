from Person import *

familyName = ""
countPerson = 0
countLink = 0
countNames = 0
""" links stores the Child _ _ and we translate it to real relations"""
links = []

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

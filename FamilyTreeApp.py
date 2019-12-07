from personclass import *

familyName = input().split()[1]

"""establish number of people in famtree"""
numPerson = input().split()[1]
count = int(numPerson)
while count > 0:
    name = input().split()[1]
    age = int(input().split()[1])
    sex = input().split()[1]
    addtoPersonArray(name, age, sex)
    count -= 1

"""make sure correct number of links"""
linkcnt = 0
while True:
    link = input().split()[1]
    linkCount = int(link)
    if int(link) != int(numPerson) - 1:
        continue
    else:
        linkcnt = linkCount
        break

"""establish relationship (parent to child)"""

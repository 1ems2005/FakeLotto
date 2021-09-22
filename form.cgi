import random

def comparelists(comparelist1,comparelist2):
    hits=0
    for i in range(len(comparelist1)):
            if comparelist1[i] in comparelist2:
                hits=hits+1

def randlist():
    randomlist=[]
    for i in range(0,6):
        temprandom = int(random.randint(1,49))
        randomlist.append(temprandom)
    return randomlist

def inplist():
    inputlist=[]
    for i in range(len(randomlist)):
        tempinput = int(input())
        inputlist.append(tempinput)
    return inputlist

def checklist(list,):
    equal=0
    for i in range(len(list)):
        for j in range(len(list)):
            if  list[i]==list[j]:
                equal=equal+1
    equal=equal-len(list)
    if  equal>0:
        inplist()

def menu():
    randomlist=randlist()
    inputlist=inplist(randomlist)
    checklist(inputlist)
    comparelists(randomlist,inputlist)
#Gamy45 mag diesen Code
menu()
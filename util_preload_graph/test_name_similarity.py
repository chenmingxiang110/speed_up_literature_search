import difflib

def getNameSim(a, b):
    name1 = a
    name2 = b
    list1 = name1.split(" ")
    list2 = name2.split(" ")
    sm=difflib.SequenceMatcher(None,list1,list2)
    return sm.ratio()

while(True):
    a = raw_input("Name 1: ")
    if a == 'quit':
        break
    b = raw_input("Name 2: ")
    if b == 'quit':
        break
    print getNameSim(a,b)

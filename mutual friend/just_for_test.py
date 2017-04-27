import snap
import difflib
import operator

# theindex = raw_input("Enter your index: ")
# theiter = raw_input("Enter your number of iterations: ")
# therec = raw_input("Enter how many recommendation you need: ")
# print recommendation(int(theindex), g, int(theiter), int(therec))


# Graph = snap.GenRndGnm(snap.PNGraph, 1000, 10000)
# snap.SaveEdgeList(Graph, "PNGraph.edges")
Graph = snap.LoadEdgeList(snap.PNGraph, "PNGraph.edges", 0, 1, '\t')
# snap.SaveEdgeList(Graph, 'mygraph.txt')

def generateFriendTxt(Graph):
    for Node in Graph.Nodes():
        ThisLine = repr(Node.GetId())+":"
        # for i in xrange(Node.GetInDeg()):
        #     TheId = Node.GetInNId(i)
        #     ThisLine += repr(TheId)+","

        # assume the out nodes are the papers cited by this one
        for i in xrange(Node.GetOutDeg()):
            TheId = Node.GetOutNId(i)
            ThisLine += repr(TheId)+","
        ThisLine = ThisLine[:len(ThisLine)-1]
        ThisLine += "\n"
        with open("TestFile.txt", "a+") as f:
            f.write(ThisLine)

def getSim(a, b):
    sm=difflib.SequenceMatcher(None,a,b)
    return sm.ratio()

def generateFirstN(input, n):
    rank = []
    simmap = {}
    # This is the papers cited by the input paper
    myBoy = []
    with open("TestFile.txt", "r") as f:
        for line in f:
            PCited = line.split(":")
            if input == PCited[0]:
                PCited[1] = PCited[1].split("\n")[0]
                myBoy = PCited[1].split(",")
                continue
    # counting the similarity
    with open("TestFile.txt", "r") as f:
        for line in f:
            PCited = line.split(":")
            if input == PCited[0]:
                continue
            sim = getSim(PCited[1].split(","), myBoy)
            if sim>0:
                simmap[PCited[0]] = sim
    sorted_map = sorted(simmap.items(), key=operator.itemgetter(1))
    numiter = int(n)
    if int(len(simmap.keys()))<int(n):
        print "Not enough elements!"
        numiter = len(simmap.keys())
    for i in xrange(numiter):
        print sorted_map[len(simmap.keys())-1-i]


# generateFriendTxt(Graph)
theindex = raw_input("Enter your index: ")
n = raw_input("Enter number of recommendations: ")
generateFirstN(theindex, n)

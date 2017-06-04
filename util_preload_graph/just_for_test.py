import snap
import difflib
import operator

# theindex = raw_input("Enter your index: ")
# theiter = raw_input("Enter your number of iterations: ")
# therec = raw_input("Enter how many recommendation you need: ")
# print recommendation(int(theindex), g, int(theiter), int(therec))


# Graph = snap.GenRndGnm(snap.PNGraph, 1000, 10000)
# snap.SaveEdgeList(Graph, "PNGraph.edges")
# Graph = snap.LoadEdgeList(snap.PNGraph, "PNGraph.edges", 0, 1, '\t')
# snap.SaveEdgeList(Graph, 'mygraph.txt')
print "loading the graph..."
Graph = snap.LoadEdgeList(snap.PNGraph, "citation.edges", 0, 1, '\t')
print "finished loading..."

def generateFriendTxt(Graph):
    ind = 1
    for Node in Graph.Nodes():
        if ind%100000 == 0:
            print ind
        ind += 1
        ThisLine = repr(Node.GetId())+":"
        # for i in xrange(Node.GetInDeg()):
        #     TheId = Node.GetInNId(i)
        #     ThisLine += repr(TheId)+","

        # assume the out nodes are the papers cited by this one
        for i in xrange(Node.GetInDeg()):
            TheId = Node.GetInNId(i)
            ThisLine += repr(TheId)+","
        ThisLine = ThisLine[:len(ThisLine)-1]
        ThisLine += "\n"
        with open("backup/TestFile_in.txt", "a+") as f:
            f.write(ThisLine)

def getSim(a, b):
    return len(list(set(a).intersection(b)))
    """
    sm=difflib.SequenceMatcher(None,a,b)
    return sm.ratio()
    """
def generateFirstN(input, n):
    rank = []
    simmap = {}
    # This is the papers cited by the input paper
    myBoy = []
    print "searching..."
    with open("TestFile.txt", "r") as f:
        ind = 0
        per = 0
        for line in f:
            ind += 1
            if ind % 920000 == 0:
                per += 1
                if per < 50:
                    print repr(per)+"% searching finished"
            PCited = line.split(":")
            if input == PCited[0]:
                PCited[1] = PCited[1].split("\n")[0]
                myBoy = PCited[1].split(",")
                continue
    print "50% searching finished"
    if len(myBoy) == 0:
        print "The input has not been cited yet."
        return
    # counting the similarity
    with open("TestFile.txt", "r") as f:
        ind = 0
        per = 50
        for line in f:
            ind += 1
            if ind % 920000 == 0:
                per += 1
                if per<100:
                    print repr(per)+"% searching finished"

            PCited = line.split(":")
            if input == PCited[0]:
                inputflag = 1
                continue
            sim = 0
            if len(PCited)>1:
                sim = getSim(PCited[1].split(","), myBoy)
            if sim>0:
                simmap[PCited[0]] = sim
    print "Done!"
    print "Finished searching. Start sorting..."
    sorted_map = sorted(simmap.items(), key=operator.itemgetter(1))
    numiter = int(n)
    if int(len(simmap.keys()))<int(n):
        numiter = len(simmap.keys())
        print "Sorry, base on the number of citations, I can only give you "+repr(numiter)+" recommendations."

    for i in xrange(numiter):
        print sorted_map[len(simmap.keys())-1-i]


generateFriendTxt(Graph)
theindex = raw_input("Enter your index: ")
n = raw_input("Enter number of recommendations: ")
generateFirstN(theindex, n)

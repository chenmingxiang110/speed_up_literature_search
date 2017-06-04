import snap
from Utility_Lib import graphToolBox
from difflib import SequenceMatcher
import os.path
import difflib
import operator

def getSim(a, b):
    sm=difflib.SequenceMatcher(None,a,b)
    return sm.ratio()

def generateFirstN(nodeid):
    rank = []
    simmap = {}
    # This is the papers cited by the input paper
    myBoy = []
    print "searching..."
    with open("TestFile.txt", "r") as f:
        for line in f:
            PCited = line.split(":")
            if nodeid == PCited[0]:
                PCited[1] = PCited[1].split("\n")[0]
                myBoy = PCited[1].split(",")
                break
    return myBoy


nodeid = "2532434"

old_list = generateFirstN(nodeid)
print len(old_list)
graph = snap.LoadEdgeList(snap.PNGraph, "citation.edges", 0, 1, '\t')
gtb = graphToolBox()
original_list = gtb.get_inward_list(graph, int(nodeid))

print old_list
print original_list
print "--------------------"
print len(old_list)
print len(original_list)
print "--------------------"
print getSim(old_list, original_list)

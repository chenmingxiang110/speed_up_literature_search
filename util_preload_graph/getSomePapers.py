import snap
from random import randint

print "Loading the graph..."
Graph = snap.LoadEdgeList(snap.PNGraph, "citation.edges", 0, 1, '\t')
print "Finished."
print "Now searching for nodes..."
i = 0
nodeid_list = []
in_dict = {}
out_dict = {}

while(i<50):
    node = Graph.GetRndNI()
    thein = node.GetInDeg()
    out = node.GetOutDeg()
    if thein<200 and thein>50 and out>30:
        nid = node.GetId()
        nodeid_list.append(nid)
        in_dict[nid] = thein
        out_dict[nid] = out
        i += 1

print "-------------------------------------"
for nid in node_list:
    print repr(nid)+": "+"in "+repr(in_dict[nid])+", out "+repr(out_dict[nid])

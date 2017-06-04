import snap

print "Loading the graph"
Graph = snap.LoadEdgeList(snap.PNGraph, "citation.edges", 0, 1, '\t')
print "Graph loaded"
testlist = [122604366, 2527422, 95296621, 5023917, 9003370, 16797867, 10393322, 8767188, 125934459, 113660016]

dist_list = [0,0,0,0,0]

for testnode in testlist:
    print "Calculating node: "+repr(testnode)
    currnode = Graph.GetNI(testnode)
    odegree = currnode.GetOutDeg()
    idegree = currnode.GetInDeg()
    outlist = []
    inlist = []
    for i in xrange(odegree):
        ref_id = currnode.GetOutNId(i)
        outlist.append(ref_id)
    for i in xrange(idegree):
        ref_id = currnode.GetInNId(i)
        inlist.append(ref_id)

    # first delete, then add it back
    Graph.DelNode(testnode)
    print "Finished adding nodes."
    print "There are "+repr(len(outlist))+" references"
    num_ref = len(outlist)
    for outid in outlist:
        print outid
        for outjd in outlist:
            if outid == outjd:
                continue
            Length = snap.GetShortPath(Graph, outid, outjd, False)
            if Length > 5:
                Length = 5
            dist_list[Length-1] = dist_list[Length-1] + 1
    print "Finished length calculation. Now add the input node back..."
    # add it back
    Graph.AddNode(testnode)
    for nodeid in inlist:
        Graph.AddEdge(nodeid, testnode)
    for nodeid in outlist:
        Graph.AddEdge(testnode, nodeid)

for i in xrange(5):
    dist_list[i] = float(dist_list[i])/2.0

print dist_list

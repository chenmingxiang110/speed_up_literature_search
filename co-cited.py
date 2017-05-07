from snap import *
import random
def generate_graph():
    f = open('CitationMap.txt', 'r')
    nodes_num = int(f.readline()[0: -1])
    G1 = TNGraph.New()
    for i in range(nodes_num + 1):
        G1.AddNode(i)
        if(i % 100000 == 0): print "addnode:",i
    line = f.readline()
    count = 0
    while line:
        line_array = line[0: -1].split('\t')
        paper = int(line_array[0])
        ref = int(line_array[1])
        G1.AddEdge(paper, ref)
        line = f.readline()
        if(count % 100000 == 0): print count
        count = count + 1
    return G1

def sort_by_value(d): 
    items=d.items()
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort(reverse = True) 
    return [ backitems[i] for i in range(0,len(backitems))] 

def get_both_cited(paper_id, g):
    both_cited_map = {}
    paper_node = g.GetNI(paper_id)
    for i in range(paper_node.GetOutDeg()):
        out_node = g.GetNI(paper_node.GetOutNId(i))
        for j in range(out_node.GetInDeg()):
            in_node = g.GetNI(out_node.GetInNId(j))
            in_node_id = in_node.GetId()
            both_cited_map[in_node_id] = both_cited_map.setdefault(in_node_id, 0) + 1
    return sort_by_value(both_cited_map)

def get_both_cited2(paper_id, g):
    both_cited_map = {}
    paper_node = g.GetNI(paper_id)
    for i in range(paper_node.GetInDeg()):
        in_node = g.GetNI(paper_node.GetInNId(i))
        for j in range(in_node.GetOutDeg()):
            out_node = g.GetNI(in_node.GetOutNId(j))
            out_node_id = out_node.GetId()
            both_cited_map[out_node_id] = both_cited_map.setdefault(out_node_id, 0) + 1
    return sort_by_value(both_cited_map)


#g = generate_graph()
G1 = TNGraph.New()
while(1):
    paper_id = raw_input("Enter paper_id: ")
    i = raw_input("Enter 1, 2, 3; 1 for # two paper both cite; 2 for # these two paper are both cited; 3 for two input paper ")
    if(i == '1'):
	print get_both_cited(paper_id, G1)
    elif(i == '2'):
	print get_both_cited2(paper_id, G1)
    elif(i == '3'):
	des_id = raw_input("Enter second paper_id: ")
	map1 = get_both_cited(paper_id, G1)
	map2 = get_both_cited2(paper_id, G1)
	if map1.has_key(des_id): print "they both cited " + str(map1[des_id]) + "papers"
	if map2.has_key(des_id): print "they are both cited by" + str(map2[des_id]) + "papers"
	

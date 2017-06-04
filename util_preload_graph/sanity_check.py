from Utility_Lib import graphToolBox
from Utility_Lib import getRecommendation
import snap

G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(2)
G1.AddNode(3)
G1.AddNode(4)
G1.AddNode(5)

G1.AddEdge(2,1)
G1.AddEdge(3,1)
G1.AddEdge(4,1)
G1.AddEdge(1,5)

gtb = graphToolBox()
list1 = gtb.get_inward_list(G1, 1)

print len(list1)
print gtb.get_dist(G1, 2, 5)
print gtb.get_num_citation(G1, 1)

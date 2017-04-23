import snap
from snap import *
import random

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

f1 = open('PaperDOI.txt', 'r')
DOImap = {};
line1 = f1.readline()
while line1:
	line1_array = line1.strip().split('\t')
	DOI = line1_array[1]
	map_id = int(line1_array[0])
	DOImap[DOI] = map_id
	line1 = f1.readline()
f1.close()

f2 = open('MappedPapers.txt', 'r')
map_idMap = {};
line2 = f2.readline()
while line2:
	line2_array = line2.strip().split('\t')
	map_id = int(line2_array[0])
	Doc_name = line2_array[1]
	map_idMap[map_id] = Doc_name
	line2 = f2.readline()
f2.close()


def printMap(map):
	for key in map:
		print key, map[key]

#printMap(DOImap)
#printMap(map_idMap)

while 1:
	print "input two papers"
	input1 = raw_input("Enter paper1: ")
	input2 = raw_input("Enter paper2: ")
	if DOImap.has_key(input1):
		paper1 = DOImap[input1]
		paper1_name = map_idMap[paper1]
		print "paper1 is: " + paper1_name
	else: print "paper1 not found"
   	if DOImap.has_key(input2): 	
		paper2 = DOImap[input2]
		paper2_name = map_idMap[paper2]
		print "paper2 is: " + paper2_name
	else: print "paper2 not found"
	distance  = snap.GetShortPath(G1, paper1, paper2, False)
	print "distance is: " + str(distance)

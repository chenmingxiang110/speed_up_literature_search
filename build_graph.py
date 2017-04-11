from snap import *
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
while 1:
    input_index = raw_input()
    num = int(input_index)
    x = G1.GetNI(num)
    print x.GetOutDeg()


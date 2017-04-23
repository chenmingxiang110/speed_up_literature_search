f = open('Papers_sample.txt', 'r')
f_out = open('MappedPapers.txt', 'w')
f_out2 = open('PaperDOI.txt', 'w')
map = {};
line = f.readline()
map_id = 0
while line:
	lineCopy = line
	line_array = line[0: -1].split('\t')
	DOI = line_array[5]
	substr = line[line.find('\t'):]
	paper_id = int(line.split('\t')[0], 16)
	if map.has_key(paper_id): continue
	map[paper_id] = map_id
	f_out.write(str(map_id) + substr)
	f_out2.write(str(map_id) + '\t' + DOI + '\n')
	if(map_id % 100000 == 0): print map_id
	line = f.readline()
	map_id = map_id + 1
f.close()
f_out.close()
f_out2.close()

f = open('PaperReferences_sample.txt', 'r')
f_out = open('CitationMap.txt', 'w')

line = f.readline()
f_out.write(str(map_id - 1) + '\n')
count = 0
while line:
    line_array = line.strip().split('\t')
    paper = int(line_array[0], 16)
    ref = int(line_array[1], 16)
    line = f.readline()
    if not (map.has_key(paper) and map.has_key(ref)):
        continue
    f_out.write(str(map[paper]) + '\t' + str(map[ref]) + '\n')
    count = count + 1
    if count % 100000 == 0: print count
f.close()
f_out.close()

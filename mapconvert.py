f = open('Papers.txt', 'r')
f_out = open('MappedPapers.txt', 'w')
map = {};
line = f.readline()
map_id = 0
while line:
    substr = line[line.find('\t'):]
    paper_id = int(line.split('\t')[0], 16)
    if map.has_key(paper_id): continue
    map[paper_id] = map_id
    f_out.write(str(map_id) + substr)
    if(map_id % 100000 == 0): print map_id
    line = f.readline()
    map_id = map_id + 1
f.close()
f_out.close()

f = open('PaperReferences.txt', 'r')
f_out = open('CitationMap.txt', 'w')

line = f.readline()
f_out.write(str(map_id - 1) + '\n')
count = 0
while line:
    line = line[0: -2]
    line_array = line.split('\t')
    paper = int(line_array[0], 16)
    ref = int(line_array[1], 16)
    line = f.readline()
    if not (map.has_key(paper) and map.has_key(ref)):
        continue
    f_out.write(str(map[paper]) + '\t' + str(map[ref]) + '\n')
    count = count + 1
    if count % 100000 == 0: print count
f.close()

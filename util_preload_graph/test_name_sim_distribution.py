import difflib
import math

def getNameSim(a, b):
    name1 = a
    name2 = b
    list1 = name1.split(" ")
    list2 = name2.split(" ")
    sm=difflib.SequenceMatcher(None,list1,list2)
    return sm.ratio()

def idf():
    node2paper_dict = {}
    with open("idf_score_clean_1.txt", 'r') as f:
        for line in f:
            ids = (line.split("\n")[0]).split(",")
            nodeid = ids[0]
            paperid = ids[1]
            node2paper_dict[nodeid] = float(paperid)
    return node2paper_dict

def getIDFSim(a, b, idf_dict):
    word_same = []
    name1 = a.lower()
    name2 = b.lower()
    # name list for the input paper
    list1 = name1.split(" ")
    # name list for the eval paper
    list2 = name2.split(" ")
    score = 0.0
    for word in list1:
        if word in list2:
            word_same.append(word)
            currfreq = 1
            if word in idf_dict:
                currfreq = idf_dict[word]
            word_same.append(currfreq)
            maxfreq = 47256662
            idfscore = math.log(float(maxfreq)/float(currfreq))
            score += idfscore
    return score,word_same

sim_list = []
name_list = []
idf_d = idf()
for i in xrange(1,508):

    print i
    filename = "papers_new/"+repr(i)

    with open(filename, 'r') as f:
        for line in f:
            name_list.append(line)

    for i in xrange(99):
        for j in xrange(i+1,100):
            name1 = name_list[i]
            name2 = name_list[j]
            sim = getIDFSim(name1, name2, idf_d)
            sim_list.append(sim)

with open("idf_sim_list_freqonly.txt", "a+") as f:
    for sim in sim_list:
        line = repr(sim[0])+'\n'
        # line = repr(sim[0])+","+repr(sim[1])+'\n'
        f.write(line)

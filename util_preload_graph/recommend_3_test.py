import snap
from difflib import SequenceMatcher
import difflib
import operator
import os.path
import math
from heapq import nlargest

class searchByID:

    def __init__(self, paperId):
        self.pId = paperId.lower()

    def getInit(self):
        return self.pId[0:4]

    def getSim(self, str1, str2):
        return SequenceMatcher(None, str1, str2).ratio()

    def search(self):
        initials = self.getInit()
        currinfo = ""
        currentsim = 0

        if os.path.isfile("../20160205-MicrosoftAcademicGraph/IdInit/_"+initials.upper()+".txt") is False:
            return currinfo

        with open("../20160205-MicrosoftAcademicGraph/IdInit/_"+initials.upper()+".txt", 'r') as f:
            while True:
                currline = f.readline()
                title = currline.split("\t")
                if len(title) < 3:
                    break

                repid = title[0]

                similarity = self.getSim(repid.lower(), self.pId)
                if similarity == 1:
                    return currline
                elif similarity > currentsim:
                    currentsim = similarity
                    currinfo = currline
                if "\n" not in currline:
                    break
        return currinfo

    def printInfo(self):
        line = self.search().split("\n")[0].split("\r")[0]
        print "----------------------------"
        if len(line) > 0:
            infos = line.split("\t")
            infotitle = ["Paper ID","Original paper title","Normalized paper title",
                "Paper publish year","Paper publish date","Paper Document Object Identifier (DOI)",
                "Original venue name","Normalized venue name","Journal ID mapped to venue name",
                "Conference series ID mapped to venue name","Paper rank"]
            for i in xrange(11):
                print infotitle[i]+": "+infos[i]
        print "----------------------------"

class searchByID_nodeID:

    def __init__(self, paperId):
        self.pId = paperId.lower()

    def getInit(self):
        return self.pId[0:4]

    def getSim(self, str1, str2):
        return SequenceMatcher(None, str1, str2).ratio()

    def search(self):
        initials = self.getInit()
        currinfo = ""
        currentsim = 0

        if os.path.isfile("../20160205-MicrosoftAcademicGraph/nodeIdInit/_"+initials.upper()+".txt") is False:
            return currinfo

        with open("../20160205-MicrosoftAcademicGraph/nodeIdInit/_"+initials.upper()+".txt", 'r') as f:
            for line in f:
                title = line.split(":")

                repid = title[1].split('\n')[0]
                similarity = self.getSim(repid.lower(), self.pId)
                if similarity == 1:
                    return line
                elif similarity > currentsim:
                    currentsim = similarity
                    currinfo = line
        return currinfo

    def main(self):
        line = (self.search().split("\n")[0].split("\r")[0]).split(":")[0]
        return line

class searchIDbyNodeID:

    def __init__(self, paperId):
        self.pId = paperId.lower()

    def getInit(self):
        if len(self.pId)>=4:
            return self.pId[0:4]
        else:
            return "0000"

    def getSim(self, str1, str2):
        return SequenceMatcher(None, str1, str2).ratio()

    def search(self):
        initials = self.getInit()
        currinfo = ""
        currentsim = 0

        if os.path.isfile("../20160205-MicrosoftAcademicGraph/RealNodeIdInit/_"+initials.upper()+".txt") is False:
            return currinfo

        with open("../20160205-MicrosoftAcademicGraph/RealNodeIdInit/_"+initials.upper()+".txt", 'r') as f:
            for line in f:
                title = line.split(":")

                repid = title[0]
                similarity = self.getSim(repid.lower(), self.pId)
                if similarity == 1:
                    return line
                elif similarity > currentsim:
                    currentsim = similarity
                    currinfo = line
        return currinfo

    def getPaperID(self):
        line = (self.search().split("\n")[0].split("\r")[0]).split(":")[1]
        return line

class NameSimRec_test:

    def __init__(self, Graph):
        self.Graph = Graph
        self.myID = "none"
        self.id2name_dict = {}
        self.id2year_dict = {}
        self.yearAveCite = {}
        self.node2paper_dict = {}
        self.idf_dict = {}
        self.name = "none"

    def get_num_citation(self, graph, nodeId):
        node = graph.GetNI(int(nodeId))
        return node.GetInDeg()

    def get_nodeID_list(self, hop):
        NodeVec = snap.TIntV()
        List = []
        snap.GetNodesAtHop(self.Graph, int(self.myID), hop, NodeVec, False)
        for item in NodeVec:
            List.append(item)
        return List

    def node2paper(self):
        # nodeid:paperid
        node2paper_dict = {}
        with open("../20160205-MicrosoftAcademicGraph/nodeid_paperid.txt", 'r') as f:
            indica = 0
            for line in f:
                if indica%10000000 == 0:
                    print "reading "+repr(indica)+" lines"
                indica += 1
                ids = (line.split("\n")[0]).split(":")
                nodeid = ids[0]
                paperid = ids[1]
                node2paper_dict[nodeid] = paperid
        return node2paper_dict

    def id2name(self):
        node2paper_dict = {}
        with open("../20160205-MicrosoftAcademicGraph/Id2Name.txt", 'r') as f:
            indica = 0
            for line in f:
                if indica%10000000 == 0:
                    print "reading "+repr(indica)+" lines"
                indica += 1
                ids = (line.split("\n")[0]).split(":")
                nodeid = ids[0]
                paperid = ids[1]
                node2paper_dict[nodeid] = paperid
        return node2paper_dict

    def id2year(self):
        node2paper_dict = {}
        with open("../20160205-MicrosoftAcademicGraph/Id2Year.txt", 'r') as f:
            indica = 0
            for line in f:
                if indica%10000000 == 0:
                    print "reading "+repr(indica)+" lines"
                indica += 1
                ids = (line.split("\n")[0]).split(":")
                nodeid = ids[0]
                paperid = ids[1]
                node2paper_dict[nodeid] = paperid
        return node2paper_dict

    def yearavecite(self):
        node2paper_dict = {}
        with open("../20160205-MicrosoftAcademicGraph/year_cite_smooth.txt", 'r') as f:
            for line in f:
                ids = (line.split("\n")[0]).split(":")
                nodeid = ids[0]
                paperid = ids[1]
                node2paper_dict[nodeid] = paperid
        return node2paper_dict

    def idf(self):
        node2paper_dict = {}
        with open("idf_score_clean_1.txt", 'r') as f:
            for line in f:
                ids = (line.split("\n")[0]).split(",")
                nodeid = ids[0]
                paperid = ids[1]
                node2paper_dict[nodeid] = float(paperid)
        return node2paper_dict

    def getNameSim_new(self, nodeID):
        if nodeID not in self.node2paper_dict:
            return 0
        paperID = self.node2paper_dict[nodeID]
        name1 = (self.name).lower()
        name2 = (self.id2name_dict[paperID]).lower()
        # name list for the input paper
        list1 = name1.split(" ")
        # name list for the eval paper
        list2 = name2.split(" ")
        score = 0.0
        for word in list1:
            if word in list2:
                currfreq = 1
                if word in self.idf_dict:
                    currfreq = self.idf_dict[word]
                maxfreq = 47256662
                idfscore = math.log(float(maxfreq)/float(currfreq))
                score += idfscore
        return score


    def getNameSim(self, nodeID):
        return self.getNameSim_new(nodeID)
        # if nodeID not in self.node2paper_dict:
        #     return 0
        # paperID = self.node2paper_dict[nodeID]
        # name1 = self.name
        # name2 = self.id2name_dict[paperID]
        # list1 = name1.split(" ")
        # list2 = name2.split(" ")
        # sm=difflib.SequenceMatcher(None,list1,list2)
        # sim_score = sm.ratio()
        # if sim_score<0.1:
        #     sim_score = 0
        # return sim_score

    def getCiteScore(self, nodeID):
        if nodeID not in self.node2paper_dict:
            return 0
        paperID = self.node2paper_dict[nodeID]
        curryear = self.id2year_dict[paperID]
        ave = self.yearAveCite[curryear]
        paperCite = self.get_num_citation(self.Graph, nodeID)
        return float(paperCite)/float(ave)

    def buildDicts(self):
        print "Initializing id2name_dict..."
        id2name_d = self.id2name()
        print "Initializing id2year_dict..."
        id2year_d = self.id2year()
        print "Initializing yearAveCite..."
        yearAve = self.yearavecite()
        print "Initializing node2paper_dict..."
        node2paper_d = self.node2paper()
        print "Initializing idf_dict"
        idf_d = self.idf()
        return (id2name_d, id2year_d, yearAve, node2paper_d, idf_d)

    def getOverall(self, nodeID):
        cite_score = self.getCiteScore(nodeID)
        name_score = self.getNameSim(nodeID)
        return float(cite_score)*float(name_score)

    def main(self, hop, n, d1, d2, d3, d4, d5, ppid):
    # here ppid is not paper id. it is the nodeid
    # n is the number of papers to recommend.
    # The function will return a list of n elements.
        print "Start to build dictionaries..."

        self.id2name_dict = d1
        self.id2year_dict = d2
        self.yearAveCite = d3
        self.node2paper_dict = d4
        self.idf_dict = d5

        print "Finished building dictionaries."

        # The hop should be 3 for the project
        curr_node = ppid

        self.myID = curr_node
        mypaperId = self.node2paper_dict[self.myID]
        self.name = self.id2name_dict[mypaperId]

        nodeList = self.get_nodeID_list(hop)
        score_dict = {}
        total_n_num = len(nodeList)
        node_ind = 0
        for node in nodeList:
            score = self.getOverall(repr(node))
            if float(score) == 0:
                continue
            if (hop == 3) and float(score)<20:
                continue
            score_dict[repr(node)] = float(score)
            if node_ind%1000 == 0:
                print "Score for "+repr(node_ind)+"/"+repr(total_n_num)+" is: "+repr(score)
            node_ind += 1
        print "Start sorting..."
        large_score = nlargest(n, score_dict.items(), key=operator.itemgetter(1))
        result_nodeids = []
        for element in large_score:
            result_nodeids.append(int(element[0]))
        print "Sorting finished."

        # sorted_score = sorted(score_dict.items(), key=operator.itemgetter(1))
        # if len(sorted_score) <= n:
        #     n = len(sorted_score)
        # result_rec = []
        # for i in xrange(int(n)):
        #     result_rec.append(sorted_score[len(sorted_score)-1-i])
        # result_nodeids = []
        # for element in result_rec:
        #     result_nodeids.append(int(element[0]))
        return result_nodeids

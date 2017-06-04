import re
from difflib import SequenceMatcher
import os.path
import difflib
import operator
from random_walk_general import randWlk
import snap

class graphToolBox:

    def get_num_citation(self, graph, nodeId):
        node = graph.GetNI(nodeId)
        return node.GetInDeg()

    def get_dist(self, graph, nodeId1, nodeId2):
        return snap.GetShortPath(graph, nodeId1, nodeId2)

    def get_inward_list(self, graph, nodeId):
        node = graph.GetNI(nodeId)
        result = []
        for i in xrange(node.GetInDeg()):
            nextId = node.GetInNId(i)
            result.append(str(nextId))
        return result

class lookUpFile:

    def __init__(self, filename):
        self.filename = "../20160205-MicrosoftAcademicGraph/"+filename+".txt"

    def printLines(self):
        with open(self.filename,'r') as f:
            for i in xrange(5):
                print repr(f.readline())

class lookUpInfo:

    def __init__(self, filename):
        self.direc = "../20160205-MicrosoftAcademicGraph/"+filename.lower()+".txt"
        self.filename = filename.lower()
        self.items = []

    def printInfo(self):
        with open("../20160205-MicrosoftAcademicGraph/readme.txt", 'r') as readmefile:
            for i in xrange(89):
                curr = readmefile.readline().lower()
                curr = re.sub('[^a-zA-Z]+', '', curr)
                if curr == self.filename:
                    while len(curr) != 0:
                        curr = readmefile.readline().lower()
                        curr_line = curr.split("\n")[0]
                        curr = re.sub('[^a-zA-Z]+', '', curr)
                        self.items.append(curr_line)
                    break
        if len(self.items) == 0:
            print "No file info!"
            return
        for i in xrange(len(self.items)):
            print self.items[i]
        # with open(self.direc, 'r') as f:
        #     curr = f.readline()
        #     curr = re.split(r'\t+', curr)
        #     for i in xrange(len(self.items)):
        #         print len(self.items)
        #         print len(curr)
                #print self.items[i]+": "+curr[i]

class separatePapersFile:

    def __init__(self):
        self.init = "Hello"

    # def getInit(self, title):
    #     result = ""
    #
    #     return result

    def main(self):
        with open("../20160205-MicrosoftAcademicGraph/Papers.txt", 'r') as f:
            i = 0
            while(True):
                i += 1
                if i%10000 == 0:
                    print repr(i)+" out of 126,900,000"
                curr = f.readline()
                title = curr.split("\t")[2]
                initials = "_"
                words = title.split(" ")
                for j in xrange(len(words)):
                    currinit = list(words[j])[0].lower()
                    if currinit<'a' or currinit>'z':
                        continue
                    if j>2:
                        break
                    initials += currinit
                with open("../20160205-MicrosoftAcademicGraph/PaperInit/"+initials+".txt", 'a+') as fw:
                    fw.write(curr)
                if "\n" not in curr:
                    break


class separatePapersIDFile:

    def main(self):
        with open("../20160205-MicrosoftAcademicGraph/Papers.txt", 'r') as f:
            i = 0
            while(True):
                i += 1
                if i%10000 == 0:
                    print repr(i)+" out of 126,900,000"
                curr = f.readline()
                pid = curr.split("\t")[0]
                initials = "_"
                initials += pid[0:4]
                with open("../20160205-MicrosoftAcademicGraph/IdInit/"+initials+".txt", 'a+') as fw:
                    fw.write(curr)
                if "\n" not in curr:
                    break

# [5]
class separatePapersNodeIDFile:

    def main(self):
        with open("../20160205-MicrosoftAcademicGraph/map_paper_newid.txt", 'r') as f:
            i = 0
            for line in f:
                i += 1
                if i%10000 == 0:
                    print repr(i)+" out of 126,900,000"
                pid = line.split(":")[1][0:4]
                initials = "_"+pid
                with open("../20160205-MicrosoftAcademicGraph/nodeIdInit/"+initials+".txt", 'a+') as fw:
                    fw.write(line)

# [6]
class separaterealPapersNodeIDFile:

    def main(self):
        with open("../20160205-MicrosoftAcademicGraph/map_paper_newid.txt", 'r') as f:
            i = 0
            for line in f:
                i += 1
                if i%10000 == 0:
                    print repr(i)+" out of 126,900,000"
                temppid = line.split(":")[0]
                pid = "0000"
                if len(temppid)>=4:
                    pid = temppid[0:4]

                initials = "_"+pid
                with open("../20160205-MicrosoftAcademicGraph/RealNodeIdInit/"+initials+".txt", 'a+') as fw:
                    fw.write(line)


class searchByAttributes:

    def __init__(self, paperName):
        self.name = paperName.lower()

    def getInit(self):
        initials = "_"
        words = self.name.split(" ")
        for j in xrange(len(words)):
            currinit = list(words[j])[0].lower()
            if currinit<'a' or currinit>'z':
                continue
            if j>2:
                break
            initials += currinit
        return initials

    def getSim(self, str1, str2):
        return SequenceMatcher(None, str1, str2).ratio()

    def search(self, namelist):
        initials = self.getInit()
        currinfo = ""
        currentsim = 0

        if os.path.isfile("../20160205-MicrosoftAcademicGraph/PaperInit/"+initials+".txt") is False:
            return currinfo

        with open("../20160205-MicrosoftAcademicGraph/PaperInit/"+initials+".txt", 'r') as f:
            while True:
                currline = f.readline()
                title = currline.split("\t")
                if len(title) < 3:
                    break

                if title[0] in namelist:
                    continue
                title = title[2]

                similarity = self.getSim(title, self.name)
                if similarity == 1:
                    return currline
                elif similarity > currentsim:
                    currentsim = similarity
                    currinfo = currline
                if "\n" not in currline:
                    break
        return currinfo

    def printInfo(self):
        lines = []
        namelist = []
        line = self.search(namelist).split("\n")[0].split("\r")[0]
        paperid = line.split("\t")[0]
        lines.append(line)
        namelist.append(paperid)
        line = self.search(namelist).split("\n")[0].split("\r")[0]
        paperid = line.split("\t")[0]
        lines.append(line)
        namelist.append(paperid)
        line = self.search(namelist).split("\n")[0].split("\r")[0]
        paperid = line.split("\t")[0]
        lines.append(line)
        namelist.append(paperid)

        print "----------------------------"
        for line in lines:
            if len(line) > 0:
                infos = line.split("\t")
                infotitle = ["Paper ID","Original paper title","Normalized paper title",
                    "Paper publish year","Paper publish date","Paper Document Object Identifier (DOI)",
                    "Original venue name","Normalized venue name","Journal ID mapped to venue name",
                    "Conference series ID mapped to venue name","Paper rank"]
                for i in xrange(11):
                    print infotitle[i]+": "+infos[i]
                print "----------------------------"


class searchByAttributesOne:

    def __init__(self, paperName):
        self.name = paperName.lower()

    def getInit(self):
        initials = "_"
        words = self.name.split(" ")
        for j in xrange(len(words)):
            currinit = list(words[j])[0].lower()
            if currinit<'a' or currinit>'z':
                continue
            if j>2:
                break
            initials += currinit
        return initials

    def getSim(self, str1, str2):
        return SequenceMatcher(None, str1, str2).ratio()

    def search(self, namelist):
        initials = self.getInit()
        currinfo = ""
        currentsim = 0

        if os.path.isfile("../20160205-MicrosoftAcademicGraph/PaperInit/"+initials+".txt") is False:
            return currinfo

        with open("../20160205-MicrosoftAcademicGraph/PaperInit/"+initials+".txt", 'r') as f:
            while True:
                currline = f.readline()
                title = currline.split("\t")
                if len(title) < 3:
                    break

                if title[0] in namelist:
                    continue
                title = title[2]

                similarity = self.getSim(title, self.name)
                if similarity == 1:
                    return currline
                elif similarity > currentsim:
                    currentsim = similarity
                    currinfo = currline
                if "\n" not in currline:
                    break
        return currinfo

    def printInfo(self):
        lines = []
        namelist = []
        line = self.search(namelist).split("\n")[0].split("\r")[0]
        paperid = line.split("\t")[0]
        lines.append(line)
        namelist.append(paperid)

        print "----------------------------"
        for line in lines:
            if len(line) > 0:
                infos = line.split("\t")
                infotitle = ["Paper ID","Original paper title","Normalized paper title",
                    "Paper publish year","Paper publish date","Paper Document Object Identifier (DOI)",
                    "Original venue name","Normalized venue name","Journal ID mapped to venue name",
                    "Conference series ID mapped to venue name","Paper rank"]
                for i in xrange(11):
                    print infotitle[i]+": "+infos[i]
                print "----------------------------"



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

    def printInfo(self):
        line = self.search().split("\n")[0].split("\r")[0]
        print line

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

    def printInfo(self):
        line = self.search().split("\n")[0].split("\r")[0]
        print line

class getRecommendation_old:

    def transferInput(self, paperId):
        line = (searchByID_nodeID(paperId).search().split("\n")[0].split("\r")[0]).split(":")[0]
        return line

    def getSim(self, a, b, mode):
        if mode == '0':
            return len(list(set(a).intersection(b)))
        else:
            sm=difflib.SequenceMatcher(None,a,b)
            return sm.ratio()

    def generateFirstN(self, input, n, mode):
        rank = []
        simmap = {}
        # This is the papers cited by the input paper
        myBoy = []
        print "searching..."
        with open("TestFile.txt", "r") as f:
            ind = 0
            per = 0
            for line in f:
                ind += 1
                if ind % 920000 == 0:
                    per += 1
                    if per < 50:
                        print repr(per)+"% searching finished"
                PCited = line.split(":")
                if input == PCited[0]:
                    PCited[1] = PCited[1].split("\n")[0]
                    myBoy = PCited[1].split(",")
                    continue
        print "50% searching finished"
        if len(myBoy) == 0:
            print "No citation record."
            return
        # counting the similarity
        with open("TestFile.txt", "r") as f:
            ind = 0
            per = 50
            for line in f:
                ind += 1
                if ind % 920000 == 0:
                    per += 1
                    if per<100:
                        print repr(per)+"% searching finished"

                PCited = line.split(":")
                if input == PCited[0]:
                    inputflag = 1
                    continue
                sim = 0
                if len(PCited)>1:
                    sim = self.getSim(PCited[1].split(","), myBoy, mode)
                if sim>0:
                    simmap[PCited[0]] = sim
        print "Done!"
        print "Finished searching. Start sorting..."
        sorted_map = sorted(simmap.items(), key=operator.itemgetter(1))
        numiter = int(n)
        if int(len(simmap.keys()))<int(n):
            numiter = len(simmap.keys())
            print "Sorry, base on the number of citations, I can only give you "+repr(numiter)+" recommendations."
        result = []
        for i in xrange(numiter):
            result.append(sorted_map[len(simmap.keys())-1-i])
        return result

    def getPaperID(self, nodeID):
        line = (searchIDbyNodeID(nodeID).search().split("\n")[0].split("\r")[0]).split(":")[1]
        return line

    def main(self, paperID, num, mode):
        nodeID = self.transferInput(paperID)
        result = self.generateFirstN(nodeID, num, mode)
        if result is None:
            return
        id_list = []
        gtb = graphToolBox()
        print "----------------------------"
        for paper in result:
            node = paper[0]
            distance = gtb.get_dist(graph, int(nodeID), int(node))
            citation = gtb.get_num_citation(graph, int(node))
            id_list.append((paper_id, distance, citation, paper[1]))
            paper_id = self.getPaperID(node)
            # searchByID(paper_id).printInfo()
        print "----------------------------"
        print "The citation of the input paper is: "+repr(gtb.get_num_citation(graph, int(nodeID)))
        print "----------------------------"
        print "paper_id, distance, citation, score"
        for singleid in id_list:
            print singleid

# The mutual friend algorithm. This is the fast version.
# Input a nodeId, return nodeIds
class getRecommendation_test:

    def getSim(self, a, b, mode):
        if mode == '0':
            return len(list(set(a).intersection(b)))
        else:
            sm=difflib.SequenceMatcher(None,a,b)
            return sm.ratio()

    def generateFirstN(self, graph, nodeID, num, mode):
        # nodeID must be an int
        nodeID = int(nodeID)
        NodeVec1 = snap.TIntV()
        NodeVec2 = snap.TIntV()
        snap.GetNodesAtHop(graph, int(nodeID), 1, NodeVec1, False)
        snap.GetNodesAtHop(graph, int(nodeID), 2, NodeVec2, False)
        nodeList = []
        for item in NodeVec1:
            nodeList.append(item)
        for item in NodeVec2:
            nodeList.append(item)
        # if number of nodes is not enough
        print "-------------------------------"
        if len(nodeList) < num:
            print ""
            print "ATTENTION!"
            print "Base on the number of citations, I can only give you "+repr(len(nodeList))+" recommendations."
            print ""
            nodeList = [str(i) for i in nodeList]
            return nodeList
        gtb = graphToolBox()
        original_list = gtb.get_inward_list(graph, nodeID)
        simmap = {}
        for item in nodeList:
            inlist = gtb.get_inward_list(graph, item)
            score = self.getSim(inlist, original_list, mode)
            simmap[str(item)] = score
        sorted_map = sorted(simmap.items(), key=operator.itemgetter(1))
        result = []
        numiter = int(num)
        for i in xrange(numiter):
            result.append(sorted_map[len(simmap.keys())-1-i])
        return result

    def main(self, graph, nodeID, num, mode):
        gtb = graphToolBox()
        if not graph.IsNode(int(nodeID)):
            print "Cannot find the paper"
            return
        result = self.generateFirstN(graph, nodeID, num, mode)
        result_nodeIds = []
        for stuff in result:
            result_nodeIds.append(int(stuff[0]))
        return result_nodeIds

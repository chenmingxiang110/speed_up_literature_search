import snap
import random
from random import randint

class randWlk3:

    def __init__(self, graph, num_iter, stay_prop):
        self.Graph = graph
        self.num_iter = num_iter
        self.stay = stay_prop

    def retrieve_random_node(self, Graph, nodeId):
        node = Graph.GetNI(nodeId)
        degree = node.GetDeg()
        NodeN = randint(0,degree-1)
        return node.GetNbrNId(NodeN)

    def get_flag(self):
        flag = random.random()
        if flag<self.stay:
            return 0
        return 1

    def random_walk(self, Graph, start, curr):
        length = snap.GetShortPath(Graph, start, curr)
        if length >= 3:

        else:
            next_nodeID = retrieve_random_node(Graph, curr)








            

    def get_recommendation_from_dict(self, index,resultMap,num):
        result = []
        resultMap.pop(index, None)
        sorted_result = sorted(resultMap.items(), key=lambda x:x[1])
        if len(sorted_result)>= num:
            for i in xrange(num):
                result.append(sorted_result[len(sorted_result)-1-i])
        else:
            for i in len(sorted_result):
                result.append(sorted_result[len(sorted_result)-1-i])
        return result

    def recommendation(self, index, g, iter, num, f_prop, b_prop):
        resultMap = {}
        for i in xrange(iter):
            if i%100 == 0:
                print i
            r = self.random_walk(index, g, f_prop, b_prop, 0)
            if r in resultMap:
                resultMap[r] += 1
            else:
                resultMap[r] = 1
        return self.get_recommendation_from_dict(index, resultMap, num)

    def getRecommendation(self, theindex, num_recommendation):
        f = float(self.forward)
        b = float(self.backward)
        if f+b>1 or f<0 or b<0:
            print "invalid initialization"
            return
        rec_result = self.recommendation(int(theindex), self.Graph, int(self.num_iter), int(num_recommendation), f, b)
        return rec_result

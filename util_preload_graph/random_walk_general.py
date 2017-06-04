import snap
import random

class randWlk:

    def __init__(self, graph, num_iter, forward, backward):
        self.Graph = graph
        self.num_iter = num_iter
        self.forward = forward
        self.backward = backward

    def retrieve_random_from_list(self, thelist):
        a = random.randint(0,len(thelist)-1)
        return thelist[a]

    def get_flag(self, a,b):
        flag = random.random()
        if flag<a:
            return 1
        elif flag>=(1-b):
            return -1
        else:
            return 0

    def random_walk(self, index, g, f_prop, b_prop):
        g1 = g
        target = index
        truef = f_prop
        trueb = b_prop
        while True:
            x = g1.GetNI(target)
            next_step = []
            last_step = []

            f_prop = truef
            b_prop = trueb
            indegree = x.GetInDeg()*f_prop
            outdegree = x.GetOutDeg()*b_prop
            allwalk = indegree+outdegree
            wlk_prop = f_prop+b_prop
            f_prop = wlk_prop*indegree/allwalk
            b_prop = wlk_prop*outdegree/allwalk

            for Id in x.GetInEdges():
                next_step.append(Id)
            for Id in x.GetOutEdges():
                last_step.append(Id)
            if len(next_step) == 0:
                # retrieve only from the last step
                flag = self.get_flag(f_prop, f_prop+b_prop)
                if flag != 0:
                    target = self.retrieve_random_from_list(last_step)
                else:
                    break
                continue
            if len(last_step) == 0:
                # retrieve only from the last step
                flag = self.get_flag(f_prop, f_prop+b_prop)
                if flag != 0:
                    target = self.retrieve_random_from_list(next_step)
                else:
                    break
                continue

            flag = self.get_flag(f_prop, f_prop+b_prop)
            if flag  == 1:
                target = self.retrieve_random_from_list(next_step)
            elif flag == -1:
                target = self.retrieve_random_from_list(last_step)
            else:
                break
        return target

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
            r = self.random_walk(index, g, f_prop, b_prop)
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

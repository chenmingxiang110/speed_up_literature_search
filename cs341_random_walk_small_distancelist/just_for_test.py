import snap
import random

def generateGraph():
    g1 = snap.TNGraph.New()
    N1 = snap.TNEANet.New()

    g1.AddNode(1)
    g1.AddNode(2)
    g1.AddNode(3)
    g1.AddNode(4)
    g1.AddNode(5)
    g1.AddNode(6)
    g1.AddNode(7)
    g1.AddNode(8)
    g1.AddNode(9)
    g1.AddNode(0)

    g1.AddEdge(1,2)
    g1.AddEdge(1,3)
    g1.AddEdge(1,6)
    g1.AddEdge(1,0)

    g1.AddEdge(2,1)
    g1.AddEdge(2,5)
    g1.AddEdge(2,6)
    g1.AddEdge(2,7)
    g1.AddEdge(2,9)

    g1.AddEdge(3,1)
    g1.AddEdge(3,4)
    g1.AddEdge(3,7)
    g1.AddEdge(3,8)

    g1.AddEdge(4,1)
    g1.AddEdge(4,3)
    g1.AddEdge(4,5)

    g1.AddEdge(5,1)
    g1.AddEdge(5,2)
    g1.AddEdge(5,3)
    g1.AddEdge(5,0)

    g1.AddEdge(6,8)

    g1.AddEdge(7,1)
    g1.AddEdge(7,2)
    g1.AddEdge(7,5)
    g1.AddEdge(7,6)
    g1.AddEdge(7,7)
    g1.AddEdge(7,8)
    g1.AddEdge(7,0)

    g1.AddEdge(8,3)
    g1.AddEdge(8,4)
    g1.AddEdge(8,5)
    g1.AddEdge(8,7)
    g1.AddEdge(8,9)
    g1.AddEdge(8,0)

    g1.AddEdge(9,1)
    g1.AddEdge(9,5)

    g1.AddEdge(0,1)
    g1.AddEdge(0,2)
    g1.AddEdge(0,4)
    g1.AddEdge(0,6)
    g1.AddEdge(0,7)

    # NIdName = snap.TIntStrH()
    # NIdName[1] = "1"
    # NIdName[2] = "2"
    # NIdName[3] = "3"
    # NIdName[4] = "4"
    # NIdName[5] = "5"
    # NIdName[6] = "6"
    # NIdName[7] = "7"
    # NIdName[8] = "8"
    # NIdName[9] = "9"
    # NIdName[0] = "0"
    #
    # snap.DrawGViz(g1, snap.gvlDot, "g1.png", "g1", NIdName)
    return g1

def retrieve_random_from_list(thelist):
    a = random.randint(0,len(thelist)-1)
    return thelist[a]

def get_flag(a,b):
    # i.e. a = 75, b = 95
    index = random.randint(1, 100)
    if index <= a:
        return 1
    elif index <= b:
        return -1
    else:
        return 0

def random_walk(index, g, f_prop, b_prop):
    g1 = g
    target = index
    while True:
        x = g1.GetNI(target)
        next_step = []
        last_step = []

        for Id in x.GetOutEdges():
            next_step.append(Id)
        for Id in x.GetInEdges():
            last_step.append(Id)
        if len(next_step) == 0:
            # retrieve only from the last step
            flag = get_flag(f_prop, f_prop+b_prop)
            if flag != 0:
                target = retrieve_random_from_list(last_step)
            else:
                break
            continue
        if len(last_step) == 0:
            # retrieve only from the last step
            flag = get_flag(f_prop, f_prop+b_prop)
            if flag != 0:
                target = retrieve_random_from_list(next_step)
            else:
                break
            continue

        flag = get_flag(f_prop, f_prop+b_prop)
        if flag  == 1:
            target = retrieve_random_from_list(next_step)
        elif flag == -1:
            target = retrieve_random_from_list(last_step)
        else:
            break
    return target

def get_recommendation_from_dict(index,resultMap,num):
    result = []
    resultMap.pop(index, None)
    sorted_result = sorted(resultMap.items(), key=lambda x:x[1])
    if len(sorted_result)>= num:
        for i in xrange(num):
            result.append(sorted_result[i][0])
    else:
        for t in sorted_result:
            result.append(t[0])
    return result

def recommendation(index, g, iter, num, f_prop, b_prop):
    resultMap = {}
    for i in xrange(iter):
        r = random_walk(7, g, f_prop, b_prop)
        if r in resultMap:
            resultMap[r] += 1
        else:
            resultMap[r] = 1
    return get_recommendation_from_dict(index, resultMap, num)


g = generateGraph()
theindex = raw_input("Enter your index: ")
theiter = raw_input("Enter your number of iterations: ")
therec = raw_input("Enter how many recommendation you need: ")

for i in [30,40,50,60,70,80,90]:
    f_prop = (100-i)*2/3
    b_prop = (100-i)/3
    print "Now the probability of staying is: "+repr(i)+"%."
    rec_result = recommendation(int(theindex), g, int(theiter), int(therec), f_prop, b_prop)
    rec_dist = []
    for j in rec_result:
        distj = snap.GetShortPath(g, int(theindex), int(j))
        rec_dist.append(distj)
    print "Our recommendations are: "+repr(rec_result)
    print "The distance are: "+repr(rec_dist)

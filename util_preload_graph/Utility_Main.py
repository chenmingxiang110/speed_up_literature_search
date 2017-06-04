from Utility_Lib import lookUpFile
from Utility_Lib import lookUpInfo
from Utility_Lib import searchByAttributes
from Utility_Lib import searchByID
from Utility_Lib import searchByID_nodeID
from Utility_Lib import searchIDbyNodeID
from Utility_Lib import getRecommendation
from Utility_Lib import getRecommendation_old
from Utility_Lib import getRecommendation_rndwlk
from Utility_Lib import searchByFile
from Utility_Lib_Test import getRecommendation_test
from recommend_3 import NameSimRec
from recommend_3_test import NameSimRec_test
import snap


Graph = snap.GenRndGnm(snap.PNGraph, 10, 50)


def printHelp():
    print ""
    print ""
    print ""
    print ""
    print ""
    print "---------------Helping-Document---------------"
    print "[1] Look up the files."
    print "Print first five lines of the chosen file."
    print "[2] Look up information examples in a file."
    print "Input the file name, regardless of big letter or not, return the information contained in the file. For example, if you want to look up the information in Papers.txt, you just simply choose [2], and then type paper."
    print "[3] Search attributes by name."
    print "This would be the most important tool that you would be used. Type the name of the article in normalized version, and the program will return the information of that article. A normalized version of the title simply means regardless of big letters and punctuations. For example, a normalized version of MoS2-Tn2 is mos2 tn2."
    print "[4] Search attributes by Paper ID."
    print "The same as option 3. The only difference is that you can search by the paper ID."
    print "[5] Search transfered Paper ID by paper ID."
    print "Get the node ID of the paper in the snap graph."
    print "[6] Search paper ID by transfered Paper ID."
    print "Get the node ID of the paper in the snap graph."
    print "[7] Get recommendation with mutual friend only."
    print "Using the mutual friend algorithm, recommend papers based on the number of common papers."
    print "[8] Get recommendation with random walk only."
    print "Using the random walk algorithm, recommend papers based on the number of visit."
    print "-------------------The--End-------------------"

def printMenu():
    print ""
    print ""
    print ""
    print ""
    print ""
    print "############################################################"
    print ""
    print "What do you want to do?"
    print ""
    print "[-1] Load the citation graph. (Please do this before doing recommendations or tests)."
    print ""
    print "[help] Help!!!!"
    print "[0] <<<<DANGER>>>> TEST MODE <<<<DANGER>>>>"
    print "[1] Look up the files."
    print "[2] Look up information examples in a file."
    print "[3] Search attributes by name."
    print "[4] Search attributes by Paper ID."
    print "[5] Search transfered Paper ID by paper ID."
    print "[6] Search paper ID by transfered Paper ID."
    print "[7] Get recommendation with mutual friend only."
    print "[8] Get recommendation with name similarity."
    print "[9] Get comprehensive recommendation."
    print ""
    print "############################################################"

# Main function:
printMenu()
choice = (raw_input("Your choice (type the number, type \"quit\" to quit): "))

while choice != "quit":
    if choice == "help":
        printHelp()
    elif int(choice) == -1:
        print "loading the graph..."
        print "It may take a while (~20 minutes on google cloud) to load the graph."
        Graph = snap.LoadEdgeList(snap.PNGraph, "citation.edges", 0, 1, '\t')
        name_sim_rec = NameSimRec(Graph)
        dicts = name_sim_rec.buildDicts()
        print "finished loading..."

    elif int(choice) == 0:
        if (Graph.GetNodes() == 10):
            print ""
            print "Please load the graph first."
        else:
            print "PAY ATTENTION: You are now in test mode!"
            input_nodeid = raw_input("Enter the NODE ID: ")
            if input_nodeid != "quit":

                nodeid_input = int(input_nodeid)
                inputnode = Graph.GetNI(nodeid_input)

                num_out = inputnode.GetOutDeg()
                half_out = int(num_out/2.0)

                nodeids_delete = []
                for i in xrange(half_out):
                    nodeid_delete = inputnode.GetOutNId(0)
                    nodeids_delete.append(nodeid_delete)
                    Graph.DelEdge(nodeid_input, nodeid_delete)

                print "What method do you want to test?"
                print "[1] Cocitation."
                print "[2] Comprehensive Hop."
                print "[3] Comprehensive Cocitop (Cocitation + Hop3)."
                print "[Any other] Quit"
                method_choice = raw_input("Your choice: ")
                if method_choice == '1':
                    num = int(raw_input("Enter the number of recommendation: "))
                    result = getRecommendation_test().main(Graph, input_nodeid, num, '0')
                    success_predict_num = 0
                    total_num = len(nodeids_delete)
                    for node_id_d in nodeids_delete:
                        if int(node_id_d) in result:
                            success_predict_num += 1
                    print repr(success_predict_num)+"/"+repr(total_num)+" succeed."

                elif method_choice == '2':
                    n = int(raw_input("Enter number of recommendations (> 3): "))
                    n3 = n/3
                    if n3<1:
                        n3 = 1
                    n2 = n/2
                    if n2<1:
                        n3 = 1
                    n1 = n-n2-n3
                    nsc_t = NameSimRec_test(Graph)
                    result1 = nsc_t.main(1, n1, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], input_nodeid)
                    print "Finished hop-1 search."
                    result2 = nsc_t.main(2, n2, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], input_nodeid)
                    print "Finished hop-2 search."
                    result3 = nsc_t.main(3, n3, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], input_nodeid)
                    print "Finished hop-3 search."
                    overall_result = result1+result2+result3
                    success_predict_num = 0
                    total_num = len(nodeids_delete)
                    for node_id_d in nodeids_delete:
                        if int(node_id_d) in overall_result:
                            success_predict_num += 1
                    print "-----------------------------"
                    print repr(success_predict_num)+"/"+repr(total_num)+" succeed."

                elif method_choice == '3':
                    n = int(raw_input("Enter number of recommendations (> 2): "))
                    n3 = n/3
                    if n3<1:
                        n3 = 1
                    n12 = n-n3
                    result12 = getRecommendation_test().main(Graph, input_nodeid, n12, '0')
                    nsc_t = NameSimRec_test(Graph)
                    result3 = nsc_t.main(3, n3, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], input_nodeid)
                    overall_result = result12+result3
                    success_predict_num = 0
                    total_num = len(nodeids_delete)
                    for node_id_d in nodeids_delete:
                        if int(node_id_d) in overall_result:
                            success_predict_num += 1
                    print repr(success_predict_num)+"/"+repr(total_num)+" succeed."

                else:
                    print "Quit the test mode."

                for nodeid_delete in nodeids_delete:
                    Graph.AddEdge(nodeid_input, nodeid_delete)

    elif int(choice) == 1:
        filename = raw_input("Please input the filename, for example Papers: ")
        lookUpFile(filename).printLines()
    elif int(choice) == 2:
        filename = raw_input("Please input the filename, for example Papers: ")
        lookUpInfo(filename).printInfo()
    elif int(choice) == 3:
        multi = raw_input("Do you want to check the paper infos by file? [y/n]: ")
        print ""
        if multi is 'y':
            print "Please make sure that the papers' names are included in \"/home/da_package/downloads/dataset/paper_names.txt\". If not, please copy the paper names into the file, or the program might crash."
            conti = raw_input("Do you want to continue? [y/n]:")
            if conti is 'y':
                searchByFile().printInfo()
        elif multi is 'n':
            papername = raw_input("Please input the name of the paper you would like to search: ")
            searchByAttributes(papername).printInfo()
        else:
            print "Invalid input!"
    elif int(choice) == 4:
        papername = raw_input("Please input the paper ID you would like to search: ")
        searchByID(papername).printInfo()
    elif int(choice) == 5:
        papername = raw_input("Please input the paper ID you would like to search: ")
        searchByID_nodeID(papername).printInfo()
    elif int(choice) == 6:
        papername = raw_input("Please input the node ID you would like to search: ")
        searchIDbyNodeID(papername).printInfo()
    elif int(choice) == 7:
        # theindex = raw_input("Enter your paperID: ")
        # n = raw_input("Enter number of recommendations: ")
        # mode = raw_input("Please choose the search mode (0: Num of Common; 1: Similarity)")
        # getRecommendation_old().main(theindex, int(n), mode)

        if (Graph.GetNodes() == 10):
            print ""
            print "Please load the graph first."
        else:
            theindex = raw_input("Enter your paperID: ")
            n = raw_input("Enter number of recommendations: ")
            mode = raw_input("Please choose the search mode (0: Num of Common; 1: Similarity)")
            getRecommendation().main(Graph, theindex, int(n), mode)
    # elif choice == 8:
    #     if (Graph.GetNodes() == 10):
    #         print ""
    #         print "Please load the graph first."
    #     else:
    #         theindex = raw_input("Enter your paperID: ")
    #         n = raw_input("Enter number of recommendations: ")
    #         getRecommendation_rndwlk().main(Graph, theindex, n)
    elif int(choice) == 8:
        if (Graph.GetNodes() == 10):
            print ""
            print "Please load the graph first."
        else:
            theindex = raw_input("Enter your paperID: ")
            n = int(raw_input("Enter number of recommendations: "))
            hop = int(raw_input("Enter the hop: "))
            n3 = n
            name_sim_rec.main(hop, n3, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], theindex)
    elif int(choice) == 9:
        if (Graph.GetNodes() == 10):
            print ""
            print "Please load the graph first."
        else:
            print "Which mode you would like to choose?"
            print "[1] Comprehensive Hop."
            print "[2] Comprehensive Cocitop (Cocitation + Hop_3)."
            which_comp = raw_input("Your Choice: ")
            if which_comp == "1":
                theindex = raw_input("Enter your paperID: ")
                n = int(raw_input("Enter number of recommendations (> 3): "))

                n3 = n/3
                if n3<1:
                    n3 = 1
                n2 = n/2
                if n2<1:
                    n3 = 1
                n1 = n-n2-n3

                name_sim_rec.main(1, n1, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], theindex)
                name_sim_rec.main(2, n2, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], theindex)
                name_sim_rec.main(3, n3, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], theindex)
            if which_comp == "2":
                theindex = raw_input("Enter your paperID: ")
                n = int(raw_input("Enter number of recommendations (> 2): "))
                n3 = n/3
                if n3<1:
                    n3 = 1
                n12 = n-n3
                getRecommendation().main(Graph, theindex, int(n12), '0')
                print ">>>>>>>>>>>>>>>>>> Distance > 3 <<<<<<<<<<<<<<<<<<<<<<"
                print ""
                print ""
                print ""
                print ""
                print ""
                print ">>>>>>>>>>>>>>>>>> Distance > 3 <<<<<<<<<<<<<<<<<<<<<<"
                name_sim_rec.main(3, n3, dicts[0], dicts[1], dicts[2], dicts[3], dicts[4], theindex)


    else:
        print "Invalid input."
    printMenu()
    choice = (raw_input("Your choice (type the number, type \"quit\" to quit): "))
    continue

print "Bye-bye!"

from Utility_Lib import lookUpFile
from Utility_Lib import lookUpInfo
from Utility_Lib import searchByAttributes
from Utility_Lib import searchByID
from Utility_Lib import searchByID_nodeID
from Utility_Lib import searchIDbyNodeID
from Utility_Lib import getRecommendation

def printHelp():
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
    print "[7] Get recommendation."
    print "Using the mutual friend algorithm, recommend papers based on the number of common papers"
    print "-------------------The--End-------------------"

def printMenu():
    print "What do you want to do?"
    print "[0] Help!!!!"
    print "[1] Look up the files."
    print "[2] Look up information examples in a file."
    print "[3] Search attributes by name."
    print "[4] Search attributes by Paper ID."
    print "[5] Search transfered Paper ID by paper ID."
    print "[6] Search paper ID by transfered Paper ID."
    print "[7] Get recommendation."


# Main function:
printMenu()
choice = int(raw_input("Your choice (type the number, type 123 to quit): "))

while choice != 123:
    if choice == 0:
        printHelp()
    elif choice == 1:
        filename = raw_input("Please input the filename, for example Papers: ")
        lookUpFile(filename).printLines()
    elif choice == 2:
        filename = raw_input("Please input the filename, for example Papers: ")
        lookUpInfo(filename).printInfo()
    elif choice == 3:
        papername = raw_input("Please input the name of the paper you would like to search: ")
        searchByAttributes(papername).printInfo()
    elif choice == 4:
        papername = raw_input("Please input the paper ID you would like to search: ")
        searchByID(papername).printInfo()
    elif choice == 5:
        papername = raw_input("Please input the paper ID you would like to search: ")
        searchByID_nodeID(papername).printInfo()
    elif choice == 6:
        papername = raw_input("Please input the node ID you would like to search: ")
        searchIDbyNodeID(papername).printInfo()
    elif choice == 7:
        theindex = raw_input("Enter your paperID: ")
        n = raw_input("Enter number of recommendations: ")
        mode = raw_input("Please choose the search mode (0: Num of Common; 1: Similarity)")
        getRecommendation().main(theindex, n, mode)
    else:
        print "Invalid input."
    printMenu()
    choice = int(raw_input("Your choice (type the number, type 123 to quit): "))
    continue

print "Bye-bye!"

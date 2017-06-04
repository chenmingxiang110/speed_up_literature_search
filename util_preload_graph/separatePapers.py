from Utility_Lib import separatePapersFile
from Utility_Lib import separatePapersIDFile
from Utility_Lib import separatePapersNodeIDFile
from Utility_Lib import separaterealPapersNodeIDFile
from Utility_Lib import paperId2PaperName
from Utility_Lib import paperId2Year
from Utility_Lib import nodeid2year2cite

def cleanupids():
    dict_id = {}
    with open("../20160205-MicrosoftAcademicGraph/map_paper_newid.txt", 'r') as f:
        indica = 0
        for line in f:
            if indica%100000 == 0:
                print "reading "+repr(indica)+" lines (retrieving data)"
            indica += 1
            ids = (line.split("\n")[0]).split(":")
            nodeid = ids[0]
            paperid = ids[1]
            dict_id[nodeid] = paperid
    with open("../20160205-MicrosoftAcademicGraph/nodeid_paperid.txt", 'a+') as f:
        indica = 0
        for key in dict_id:
            if indica%100000 == 0:
                print "writing "+repr(indica)+" lines (retrieving data)"
            indica += 1
            line = key+":"+dict_id[key]+"\n"
            f.write(line)

def citationDistribution():
    num_dict = {}
    cit_dict = {}
    with open("../20160205-MicrosoftAcademicGraph/node2id2year2cite.txt", 'r') as f:
        indica = 0
        for line in f:
            if indica%100000 == 0:
                print "reading "+repr(indica)+" lines (retrieving data)"
            indica += 1
            stuff = (line.split("\n")[0]).split(",")
            year = stuff[3]
            cite = stuff[2]
            if year in cit_dict:
                cit_dict[year] = cit_dict[year]+int(cite)
                num_dict[year] = num_dict[year]+1
            else:
                cit_dict[year] = int(cite)
                num_dict[year] = 1
    with open("../20160205-MicrosoftAcademicGraph/year_cite_distribution.txt", 'a+') as f:
        for key in cit_dict:
            ave_cite = float(cit_dict[key])/float(num_dict[key])
            line = key+":"+repr(ave_cite)+"\n"
            f.write(line)

# separatePapersFile().main()
# separatePapersIDFile().main()
# separatePapersNodeIDFile().main()
# separaterealPapersNodeIDFile().main()
# paperId2PaperName().seperate()
# paperId2Year().seperate()
# nodeid2year2cite().main()
# cleanupids()
citationDistribution()

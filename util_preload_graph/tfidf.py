from sets import Set
import enchant

def getIDFdict():
    n_dict = {}
    with open("../20160205-MicrosoftAcademicGraph/Papers.txt", 'r') as f:
        indica = 0
        for line in f:
            if indica%100000 == 0:
                print "Parsed "+repr(indica)+" lines"
            indica += 1
            title = line.split("\t")[2]
            words = title.split(" ")
            wordset = Set([])
            for word in words:
                wordset.add(word)
            for word in wordset:
                if word in n_dict:
                    n_dict[word] = n_dict[word]+1
                else:
                    n_dict[word] = 1
    return n_dict

def cleandata():
    d = enchant.Dict("en_US")
    newlines = []
    with open("idf_score.txt", 'r') as f:
        indica = 0
        for line in f:
            if indica%100000 == 0:
                print "Cleaned "+repr(indica)+" lines"
            indica += 1
            stuff = line.split("\n")[0]
            stuff = stuff.split(",")
            if d.check(stuff[0]):
                newlines.append(line)
    return newlines

def cleandata_1():
    newlines = []
    with open("idf_score_clean.txt", 'r') as f:
        indica = 0
        for line in f:
            if indica%100000 == 0:
                print "Cleaned "+repr(indica)+" lines"
            indica += 1
            stuff = line.split("\n")[0]
            stuff = stuff.split(",")
            if int(stuff[1]) != 1:
                newlines.append(line)
    return newlines



# n_dict = getIDFdict()
# with open("idf_score.txt", 'a+') as f:
#     for key in n_dict:
#         line = key+","+repr(n_dict[key])+'\n'
#         f.write(line)

# newlines = cleandata()
# print "Writing the new file..."
# with open("idf_score_clean.txt", 'a+') as f:
#     for line in newlines:
#         f.write(line)
# print "finished"

# newlines = cleandata_1()
# print "Writing the new file..."
# with open("idf_score_clean_1.txt", 'a+') as f:
#     for line in newlines:
#         f.write(line)
# print "finished"

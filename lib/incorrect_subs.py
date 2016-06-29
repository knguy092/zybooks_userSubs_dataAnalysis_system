import csv
from collections import defaultdict
from lib import misc_funcs

def generateData(csvListPath):
    for path in csvListPath:
        splitPath = path.split('/')
        zyBookCode = splitPath[1]
        contentID = splitPath[2].split('_')[1].rstrip(".csv")
        outputCsv = open("generated_csvs/{}/incorrect_subs/{}_incorrect_subs_{}.csv".format(zyBookCode, zyBookCode, contentID),
                         "w", newline='', encoding="utf8")
        writer = csv.writer(outputCsv)
        writer.writerow(["Incorrect Submission", "Count"])
        '''
        Reason for idToIncSubs is to count only unique, incorrect submissions per user.
        Reason there is no analyzedUser set is we are interested in misconceptions.
        '''
        incSubToCount = defaultdict(int)
        idToIncSubs = defaultdict(set)
        
        with open(path, 'r', encoding="utf8") as csvFile:
            dataTable = csv.reader(csvFile)
            next(dataTable)
            for dateAndTime, userID, isCorrect, rawSub in dataTable:
                if not(int(isCorrect)):
                    idToIncSubs[userID].add(misc_funcs.stripNoiseSub(rawSub))

        for incSubs in idToIncSubs.values():
            for incSub in incSubs:
                incSubToCount[incSub] += 1

        incSubToCount.pop("", None) #removing empty submissions
        
        sortedData = sorted(incSubToCount.items(),
                            key = lambda entry : entry[1],
                            reverse=True)

        for sub, count in sortedData:
            writer.writerow([sub, count])
        outputCsv.close()

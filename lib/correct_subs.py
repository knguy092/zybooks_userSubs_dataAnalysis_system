import csv
from collections import defaultdict
from lib import misc_funcs

def generateData(csvListPaths):
    for path in csvListPaths:
        splitPath = path.split('/')
        zyBookCode = splitPath[1]
        contentID = splitPath[2].split('_')[1].rstrip(".csv")
        outputCsv = open("generated_csvs/{}/correct_subs/{}_correct_subs_{}.csv".format(zyBookCode, zyBookCode, contentID),
                         "w", newline='', encoding="utf8")
        writer = csv.writer(outputCsv)
        writer.writerow(["Correct Submission", "Count"])
        correctSubToCount = defaultdict(int)
        with open(path, 'r', encoding="utf8") as csvFile:
            dataTable = csv.reader(csvFile)
            next(dataTable)
            for dateAndTime, userID, isCorrect, rawSub in dataTable:
                if int(isCorrect):
                    correctSubToCount[misc_funcs.stripNoiseSub(rawSub)] += 1
        sortedData = sorted(correctSubToCount.items(), key = lambda entry : entry[1], reverse = True)
        for sub, count in sortedData:
            writer.writerow([sub, count])
        outputCsv.close()

import csv
from collections import defaultdict
from lib import misc_funcs
from statistics import median, mean

def generateData(csvListPaths):
    cIdToAttsData = defaultdict(dict)
    zyBookCode = csvListPaths[0].split('/')[1]
    for path in csvListPaths:
        contentID = path.split('/')[2].split('_')[1].rstrip(".csv")
        userIdToNumAtts = defaultdict(int)
        analyzedUsers = set()
        with open(path, 'r', encoding="utf8") as csvFile:
            dataTable = csv.reader(csvFile)
            next(dataTable)
            for dateAndTime, userID, isCorrect, rawSub in dataTable:
                if userID not in analyzedUsers:
                    if int(isCorrect):
                        analyzedUsers.add(userID)
                    userIdToNumAtts[userID] += 1
        numUsersParticipated = len(userIdToNumAtts)
        if numUsersParticipated != 0:
            cIdToAttsData[contentID]["medianAtts"] = median(userIdToNumAtts.values())
            cIdToAttsData[contentID]["avgAtts"] = round(mean(userIdToNumAtts.values()), 2)
            cIdToAttsData[contentID]["numUsersPart"] = numUsersParticipated
    sortedData = sorted(cIdToAttsData.items(), key=lambda entry : entry[1]["medianAtts"], reverse=True)
    outputCsv = open("generated_csvs/{}/{}_activity_difficulty.csv".format(zyBookCode, zyBookCode),
                     "w", newline='', encoding="utf8")
    writer = csv.writer(outputCsv)
    writer.writerow(["Content ID", "Median Number of Attempts", "Average Number of Attempts", "Number of Users Participated"])
    for cID, data in sortedData:
        writer.writerow([cID, data["medianAtts"], data["avgAtts"], data["numUsersPart"]])
        

import csv
from collections import defaultdict
from lib import misc_funcs
from statistics import median, mean

def generateData(csvListPaths):
    userIdToData = defaultdict(lambda : {"cIdToNumAtts" : defaultdict(int), "cIdToAtts" : defaultdict(list), "cIdsCompleted" : set()})
    zyBookCode = csvListPaths[0].split('/')[1]
    outputCsv = open("generated_csvs/{}/{}_user_data.csv".format(zyBookCode, zyBookCode),
                     'w', newline='', encoding="utf8")
    writer = csv.writer(outputCsv)
    writer.writerow(["User ID", "Median Number of Attempts", "Average Number of Attempts",
                     "Number of Activities Participated", "Number of Activities Completed",
                     "Content IDs of Unfinished Activities"])
    for path in csvListPaths:
        analyzedUsers = set()
        contentID = path.split('/')[2].split('_')[1].rstrip(".csv")
        with open(path, 'r', encoding="utf8") as csvFile:
            dataTable = csv.reader(csvFile)
            next(dataTable)
            for dateAndTime, userID, isCorrect, rawSub in dataTable:
                if userID not in analyzedUsers:
                    if int(isCorrect):
                        analyzedUsers.add(userID)
                        userIdToData[userID]["cIdsCompleted"].add(contentID)
                    userIdToData[userID]["cIdToAtts"][contentID].append(rawSub)
                    userIdToData[userID]["cIdToNumAtts"][contentID] += 1
    for userID in userIdToData:
        listNumAtts = userIdToData[userID]["cIdToNumAtts"].values()
        userIdToData[userID]["numActsPart"] = len(listNumAtts)
        userIdToData[userID]["numActsCompleted"] = len(userIdToData[userID]["cIdsCompleted"])
        setCidUnfinished = set(userIdToData[userID]["cIdToNumAtts"].keys()) - userIdToData[userID]["cIdsCompleted"]
        userIdToData[userID]["cIdsUnfinished"] = ", ".join(setCidUnfinished)
        userIdToData[userID]["avgNumAtts"] = mean(listNumAtts)
        userIdToData[userID]["medNumAtts"] = median(listNumAtts)
    sortedData = sorted(userIdToData.items(),
                        key = lambda entry : (entry[1]["medNumAtts"], entry[1]["avgNumAtts"], entry[1]["numActsPart"], -entry[1]["numActsCompleted"]),
                        reverse = True)
    for userID, data in sortedData:
        writer.writerow([userID, data["medNumAtts"], data["avgNumAtts"], data["numActsPart"],
                         data["numActsCompleted"], data["cIdsUnfinished"]])
    outputCsv.close()
    while True:
        userID = input("Enter user ID of user of interest ('q' to quit): ")
        if userID == 'q':
            break
        sortedData = sorted(userIdToData[userID]["cIdToNumAtts"].items(), key=lambda entry : entry[1], reverse=True)
        print("\nContent ID - Number of Attempts Log")
        for contentID, numAtts in sortedData:
            print("{}: {}".format(contentID, numAtts))
        contentID = input("\nEnter content ID that you would like to investigate ('q' to quit): ")
        if contentID == 'q':
            break
        print("\nSubmissions Log")
        for attemptNum, rawSub in enumerate(userIdToData[userID]["cIdToAtts"][contentID], 1):
            print("({})\n{}\n".format(attemptNum, rawSub))
        
            

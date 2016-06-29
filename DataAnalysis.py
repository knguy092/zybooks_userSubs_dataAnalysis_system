from lib import misc_funcs, incorrect_subs, csv_downloader, correct_subs, user_data, activity_difficulty
import os

#email = input("Email: ").strip()
#password = input("Password: ").strip()
#authToken = misc_funcs.getAuthToken(email, password)
authToken = input("Enter auth token: ").strip()
zyBookCode = input("zyBook code of zyBook of interest: ").strip()
activityType = input("Enter 1 for progression activities or 2 for programming activities: ").strip()

if activityType == '1':
    pass
elif activityType == '2':
    choice = input(
    '''Specification Options
    1) manual entry of content IDs
    2) rIDs text file
    3) manual entry of chapter[.lesson]s
    4) all programming activities
Input a number: ''').strip()
    if choice == '1':
        contentIDsList = input("Enter content IDs separated by spaces: ").strip().split(' ')
        print("Downloading csvs...")
        if not os.path.exists("original_csvs/{}".format(zyBookCode)):
            os.makedirs("original_csvs/{}".format(zyBookCode))
        csvListPaths = csv_downloader.byCIDs(authToken, zyBookCode, contentIDsList)
    elif choice == '2':
        rIDsTextFileName = input("Enter name of rIDs text file: ").strip()
        print("Downloading csvs...")
        if not os.path.exists("original_csvs/{}".format(zyBookCode)):
            os.makedirs("original_csvs/{}".format(zyBookCode))
        csvListPaths = csv_downloader.byCIDsTextFile(authToken, zyBookCode, rIDsTextFileName)
    elif choice == '3':
        chLessList = input("Enter chapter[.lesson]s separated by spaces: ").strip().split(' ')
        print("Downloading csvs...")
        if not os.path.exists("original_csvs/{}".format(zyBookCode)):
            os.makedirs("original_csvs/{}".format(zyBookCode))
        csvListPaths = csv_downloader.byChLess(authToken, zyBookCode, activityType, chLessList, email, password)
    elif choice == '4':
        print("Downloading csvs...")
        if not os.path.exists("original_csvs/{}".format(zyBookCode)):
            os.makedirs("original_csvs/{}".format(zyBookCode))
        csvListPaths = csv_downloader.all(authToken, zyBookCode, activityType, email, password)
    choices = input(
    '''Data Generations Available
    1) correct submissions
    2) incorrect submissions
    3) user data
    4) activity difficulty
Input numbers separated by spaces: ''').strip().split(' ')
    print("Generating data...")
    for choice in choices:
        if choice == '1':
            if not os.path.exists("generated_csvs/{}/correct_subs".format(zyBookCode)):
                os.makedirs("generated_csvs/{}/correct_subs".format(zyBookCode))
            correct_subs.generateData(csvListPaths)
        elif choice == '2':
            if not os.path.exists("generated_csvs/{}/incorrect_subs".format(zyBookCode)):
                os.makedirs("generated_csvs/{}/incorrect_subs".format(zyBookCode))
            incorrect_subs.generateData(csvListPaths)
        elif choice == '3':
            user_data.generateData(csvListPaths)
        elif choice == '4':
            activity_difficulty.generateData(csvListPaths)

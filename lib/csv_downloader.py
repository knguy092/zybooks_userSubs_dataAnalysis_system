from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import json

def byCIDs(authToken, zyBookCode, contentIDsList):
    csvListPaths = []
    for contentID in contentIDsList:
        responseURL = "https://s2.zybooks.com/v1/zybook/{}/submissions/{}?auth_token={}".format(zyBookCode, contentID, authToken)
        urlContentText = urllib.request.urlopen(responseURL)
        urlContentJsonObj = json.loads(urlContentText.read().decode("utf-8-sig"))
        csvURL = urlContentJsonObj["url"]
        csvPath = "original_csvs/{}/{}_{}.csv".format(zyBookCode, zyBookCode, contentID)
        urllib.request.urlretrieve(csvURL, filename=csvPath)
        csvListPaths.append(csvPath)
    return csvListPaths


def byCIDsTextFile(authToken, zyBookCode, rIDsTextFileName):
    csvListPaths = []
    with open("cIDs_txt_files/{}".format(rIDsTextFileName), 'r') as inputTxtFile:
        contentIDsList = [line.rstrip() for line in inputTxtFile]
    for contentID in contentIDsList:
        responseURL = "https://s2.zybooks.com/v1/zybook/{}/submissions/{}?auth_token={}".format(zyBookCode, contentID, authToken)
        urlContentText = urllib.request.urlopen(responseURL)
        urlContentJsonObj = json.loads(urlContentText.read().decode("utf-8-sig"))
        csvURL = urlContentJsonObj["url"]    
        csvPath = "original_csvs/{}/{}_{}.csv".format(zyBookCode, zyBookCode, contentID)
        urllib.request.urlretrieve(csvURL, filename=csvPath)
        csvListPaths.append(csvPath)
    return csvListPaths
    
def byChLess(authToken, zyBookCode, activityType, chLessList, email, password):
    pass

def all(authToken, zyBookCode, activityType, email, password):
    driver = webdriver.Chrome("C:/Users/hwang/AppData/Local/Programs/Python/Python35-32/Scripts/chromedriver.exe")
    driver.get("https://zybooks.zyante.com/#/signin")
    elem = driver.find_element_by_xpath("//input[@type='email']")
    elem.send_keys(email)
    elem = driver.find_element_by_id("//input[@type='password']")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

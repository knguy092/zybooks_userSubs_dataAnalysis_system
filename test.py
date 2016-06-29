from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/hwang/AppData/Local/Programs/Python/Python35-32/Scripts/chromedriver.exe")
driver.get("https://zybooks.zyante.com/#/signin")
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath("//input[@type='email']")
elem.send_keys("hwangct@uci.edu")
elem = driver.find_element_by_id("//input[@type='password']")
elem.send_keys("amoxicil1in")
elem.send_keys(Keys.RETURN)
driver.get("https://zybooks.zyante.com/#/zybook/ProgrammingInCppR25/chapter/1/section/3")
driver.implicitly_wait(10)
elems = driver.find_elements_by_xpath("//div[contains(@class, 'homeworkSystem')]")
#elems = driver.find_elements_by_xpath("//div[contains(@class, 'progressionTool')]")
#driver.close()

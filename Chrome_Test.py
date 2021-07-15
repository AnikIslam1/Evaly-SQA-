from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

driver: WebDriver = webdriver.Chrome(executable_path="D:\SQA\chromedriver_win32\chromedriver.exe")

#login: WebDriver = webdriver.Chrome(executable_path="D:\SQA\chromedriver_win32\chromedriver.exe")

#driver.get("https://evaly.com.bd/")# using login.php page
driver.get("https://evaly.com.bd/login.php")


driver.find_element_by_xpath('/html/body/reach-portal[1]/div/div/div/section/div/button').click()# remove add


phone = driver.find_element_by_xpath('//*[@id="phone"]')
phone.send_keys("01730955805")

pword = driver.find_element_by_xpath('//*[@id="password"]')
pword.send_keys("012345678@")

driver.find_element_by_xpath('//*[@id="login"]/div/div/div/form/button').click()# login

driver.get("https://evaly.com.bd/shops")

driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div/div[1]/div/div[1]/div').click()


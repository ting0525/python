from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:/Users/j0918/Desktop/chrome43/chromedriver.exe"   ##改過位置(因為改了新版本) github記得改
driver = webdriver.Chrome(PATH)

driver.get("https://ci.isu.edu.tw/prev/prev_login.asp?lang=CH&st=ISU")
search = driver.find_element_by_name("loginID")
search.send_keys("isu11003022A")
search = driver.find_element_by_name("passID")
search.send_keys("f616773488")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="img2"]').click()
driver.find_element_by_xpath('//*[@id="emp_past14_11"]').click()
driver.find_element_by_xpath(
    '/html/body/div[1]/form[2]/div[5]/div/div/div[2]/label').click()
driver.find_element_by_xpath(
    '/html/body/div[1]/form[2]/div[6]/div/div[1]/div[2]/label').click()
search = driver.find_element_by_name("emp_message")
search.send_keys("good")
driver.find_element_by_xpath('//*[@id="submit_btn"]').click()

time.sleep(1)
driver.quit()

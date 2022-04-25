from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Users/j0918/Desktop/chrome43/chromedriver.exe"   ##注意chrome更新版本 跟chrome版本需相同
driver = webdriver.Chrome(PATH)

driver.get("https://ci.isu.edu.tw/prev/prev_login.asp?lang=CH&st=ISU")

search = driver.find_element_by_name("loginID")
search.send_keys("isu11003022A")
search = driver.find_element_by_name("passID")
search.send_keys("f616773488")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="img2"]').click()
driver.find_element_by_xpath('//*[@id="emp_past14_11"]').click()
driver.find_element_by_xpath('/html/body/div[1]/form[2]/div[5]/div/div/div[2]/label').click()
driver.find_element_by_xpath('/html/body/div[1]/form[2]/div[6]/div/div[1]/div[2]/label').click()
search = driver.find_element_by_name("emp_message")
search.send_keys("good")
driver.find_element_by_xpath('//*[@id="submit_btn"]').click()

time.sleep(3)
driver.quit()





"""
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_depart2"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_past14_11"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_warship6_flag2"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_contact2"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_home_qua2"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_home_qua_ff2"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_2019nCoV2"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_warship3_flag2"]').click()
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@id="emp_warship8_name1006"]').click()
"""
##driver.find_element_by_xpath('//*[@id="submit_btn"]').click()

#link = driver.find_element_by_link_text("img2")//*[@id="img2"]
#link.click()

#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1")))

#titles = driver.find_elements_by_class_name("tgn9uw-3")
#for title in titles:
    #print(title.text)

#link = driver.find_element_by_link_text("#徵補習夥伴 高雄城市外語雅思課程請求開班支援")
#link.click()
#driver.back()
#driver.forward()

##time.sleep(5)
##driver.quit()
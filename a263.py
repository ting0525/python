from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Users/j0918/Desktop/chrome43/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://ci.isu.edu.tw/prev/prev_login.asp?lang=CH&st=ISU")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\msedgedriver.exe"


driver = webdriver.Edge(PATH)
driver.implicitly_wait(30)
driver.get("https://mt5.xm.com/")
driver.maximize_window()
accept = driver.find_element("xpath" , "/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div/button")
accept.click()
time.sleep(5)
driver.save_screenshot("C:\Program Files (x86)\Selenium\screen2.png")
time.sleep(5)
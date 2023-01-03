from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"


driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
driver.get("https://mt5.xm.com/")
driver.maximize_window()
accept = driver.find_element("xpath" , "/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div/button")
accept.click()
close = driver.find_element("name", "Close")
close.click()
cookies = driver.find_element("link text", "PLATFORMS")
cookies.click()
MT5 = driver.find_element("link text", "MT5 WebTrader")
MT5.click()
Access = driver.find_element("link text", "ACCESS MT5 WEBTRADER")
Access.click()
driver.save_screenshot("C:\Program Files (x86)\Selenium\screen.png")
time.sleep(100)


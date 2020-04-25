from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox(executable_path="C:\\Users\\sripavithra\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.implicitly_wait(100)
driver.get("https://www.distacart.com")
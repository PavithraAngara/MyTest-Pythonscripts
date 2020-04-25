from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="C:\\Users\\sripavithra\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\\sripavithra\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://browntaped.myshopify.com/admin/apps")
driver.refresh()
driver.implicitly_wait(20)
driver.find_element_by_id("account_email").send_keys("happy@distacart.com")
driver.implicitly_wait(20)
driver.find_element_by_name("commit").click()
#driver.implicitly_wait(50)
driver.find_element_by_id("account_password").send_keys("Browntaped@Dista")
#driver.implicitly_wait(100)
driver.find_element_by_name("commit").click()
driver.find_element_by_xpath("//*[@id='gid://shopify/App/462469]'/div[2]/div/div[1]/div").click()


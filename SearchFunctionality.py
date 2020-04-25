#Synopsis : To verify Smart Search Functionality
#Intent : When we enter any text in the search bar area in our application it should give automatic suggestions into the Drop-Down list
#Expection Criteria : It should give relevant suggestions based on the text we provide..

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="C:\\Users\\sripavithra\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(100)
driver.get("https://www.distacart.com")
driver.find_element_by_xpath("//*[@id='shopify-section-header']/header[2]/div[2]/div/div[1]/div/div/div[2]/li/form/input[2]").send_keys("pat")

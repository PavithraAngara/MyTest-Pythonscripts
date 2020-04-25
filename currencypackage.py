from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="C:\\Users\\sripavithra\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver.implicitly_wait(100)
driver.get("https://www.distacart.com")


driver.find_element_by_xpath("//*[@id='shopify-section-header']/header[2]/div[2]/div/div[1]/div/div/div[2]/ul[1]/li/div/div").click()
firstLevelMenu=driver.find_element_by_css_selector("#shopify-section-header > header.desktop-header > div.main_nav_wrapper > div > div.sticky-top > div > div > div.cart-user-search > ul.menu.right > li > div > div > ul > li:nth-child(2)").click()
action = ActionChains(driver)
action.move_to_element(firstLevelMenu).perform()




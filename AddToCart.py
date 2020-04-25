from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="C:\\Users\\sripavithra\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver.implicitly_wait(100)
driver.get("https://www.distacart.com")
#Navigate to Shop by Categories" :
driver.find_element_by_id("toggle-img").click()
#Health Related Coding :
firstLevelMenu = driver.find_element_by_css_selector("#menu > ul > div > div.nav > ul > div > li:nth-child(2) > a")
action = ActionChains(driver)
action.move_to_element(firstLevelMenu).perform()
#Patanjali Products coding :
secondLevelMenu = driver.find_element_by_css_selector("#menu > ul > div > div.nav > ul > div > li:nth-child(2) > ul > li:nth-child(2) > a")
secondLevelMenu.click()
#Product information for Patanjali Mukta vati Extra Power :
thirdLevelMenu =driver.find_element_by_css_selector("#shopify-section-collection-template > div > div:nth-child(4) > div.product-list.collection-matrix.clearfix.equal-columns--clear.equal-columns--outside-trim > div.one-third.column.medium-down--one-half.small-down--one-half.thumbnail.odd.quick-shop-style--popup.product-686163197997 > div > div > div.thumbnail-overlay > a")
thirdLevelMenu.click()
#To add quantity to 2
driver.find_element_by_xpath("//*[@id='product_form_686163197997']/div[3]/div[1]/span[2]").click()
#Add to Cart Button
#driver.find_element_by_xpath("//*[@id='product_form_686163197997']/div[3]/div[2]/button").click()
#Buy it Now
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div/div/div[1]/div[2]/div[4]/form/div[3]/div[2]/div/div/div/div/button[1]").click()



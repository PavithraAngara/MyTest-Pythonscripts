#Synopsis : Install app to find influencers amongst our customers.Use carro app from shopify app store
#Intent : To verify our customers and find the influencers
#Expectation Criteria : Customers should be verified with our any of the existing placed orders

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\sripavithra\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://browntaped.myshopify.com/admin/apps")
driver.refresh()
driver.implicitly_wait(20)
driver.find_element_by_id("account_email").send_keys("happy@distacart.com")
#driver.implicitly_wait(20)
driver.find_element_by_name("commit").click()
#driver.implicitly_wait(50)
driver.find_element_by_id("account_password").send_keys("Browntaped@Dista")
#driver.implicitly_wait(100)
driver.find_element_by_name("commit").click()
driver.get("https://browntaped.myshopify.com/admin/app_store/redirect?url=https://apps.shopify.com")
#for handle in driver.window_handles:
#driver.switch_to.frame()
driver.find_element_by_xpath("//*[@id='ui-app-store-hero__home-search']/label/input").send_keys("Carro")

driver.find_element_by_css_selector("#ui-app-store-hero__home-search > label > button > svg").click()
driver.find_element_by_css_selector("#SearchResultsListings > div > div > a > h4").click()
driver.find_element_by_xpath("//*[@id='Main']/section[1]/div/div/div/div[6]/form/input[2]").click()
#driver.find_elements_by_css_selector("#qa-filters-container > div.MuiButtonBase-root.MuiChip-root.MuiChip-colorSecondary.MuiChip-clickableColorSecondary.MuiChip-outlined.MuiChip-outlinedSecondary.MuiChip-sizeSmall.MuiChip-clickable > span.MuiChip-label.MuiChip-labelSmall").click()
#driver.find_element_by_xpath("/html/body/div[23]/div[3]/div/div[3]/button[2]/span[1]").click()
#driver.find_element_by_id("qa-search-main").send_keys("Customer")
#driver.find_element_by_xpath("/html/body/div[4]/main/section[1]/div/div/div/form/label/button/svg")



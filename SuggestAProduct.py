'''
synopsis : Test Suggest A product
Description : Test case to suggest a product and able to add details such as name email, productdescription and send .
Pass Criteria :  we should recieve an email from customer for the suggested product
'''
#Synopsis : To verify Suggest a Product functionality and valudation of the fields in the Email
#Intent : 1.Test case to suggest a product and able to add details such as name email, productdescription and when sending it will receive an email
#         2.Provided invalid email in the email field to test if it being submitted
#Expectation Criteria : It should send all the details to our mail "happy@distacart.com"


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="C:\\Users\\sripavithra\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(100)
driver.get("https://www.distacart.com")

driver.find_element_by_xpath("//*[@id='shopify-section-header']/header[2]/div[2]/div/div[2]/div/div/ul/li[3]/a[1]").click()

driver.find_element_by_id("contactFormName").send_keys("PavithraAngara")
driver.find_element_by_id("contactFormEmail").send_keys("abcddadaf@outlook.comm")
driver.find_element_by_id("contactFormMessage").send_keys("Require Lifebouy Hand Sanitizer \n  note : This is for Testing purpose")
#driver.find_element_by_xpath("//*[@id=''contact_form']/div/div[5]/input[1]").click()
#driver.find_elements_by_css_selector("#contact_form > div > div.clearfix.frm_bot > input.btn_c").click()
driver.find_element_by_class_name("btn_c").click()

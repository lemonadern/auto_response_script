import chromedriver_binary
# webdriver kits
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# settings
import settings
PAGE_LINK = settings.PAGE_LINK
MAIL_ADDLESS = settings.MAIL_ADDLESS
PASSWORD = settings.PASSWORD

driver = webdriver.Chrome()

driver.get(PAGE_LINK)

email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0116')))
email_field.send_keys(MAIL_ADDLESS)
driver.find_element_by_id("idSIButton9").click()

password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0118')))
password_field.send_keys(PASSWORD)
driver.find_element_by_id("idSIButton9").click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'idBtn_Back'))).click()


# driver.close()
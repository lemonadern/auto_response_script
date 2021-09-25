import chromedriver_binary
# webdriver kits
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime
import random

# settings
import settings
PAGE_LINK = settings.PAGE_LINK
MAIL_ADDRESS = settings.MAIL_ADDRESS
PASSWORD = settings.PASSWORD

import weekday
today = datetime.date.today()
is_weekend = weekday.is_weekend


# field xpaths
temperature_xpath = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input"
symptom_xpath = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input"

attend_xpath = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/label/input"
absent_xpath = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/label/input"

checkbox_xpath = "/html/body/div[1]/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/label/input"
submit_xpath = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[4]/div[1]/button/div"
# temperature
temperature = 36.0 + random.randrange(6) / 10

# weekday 
weekday = datetime.date.today().weekday()

# driver
driver = webdriver.Chrome()

driver.get(PAGE_LINK)

email_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'i0116')))
email_field.send_keys(MAIL_ADDRESS)
driver.find_element_by_id("idSIButton9").click()

password_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'i0118')))
password_field.send_keys(PASSWORD)
driver.find_element_by_id("idSIButton9").click()

WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'idBtn_Back'))).click()


# form input
temperature_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, temperature_xpath)))
temperature_field.send_keys(str(temperature))

symptom_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, symptom_xpath)))
symptom_field.click()

if(is_weekend(today=today)):
    absent_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, absent_xpath)))
    absent_field.click()
else:
    attend_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, attend_xpath)))
    attend_field.click()

mail_checkbox_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
mail_checkbox_field.click()

submit_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
submit_button.click()

driver.close()
import chromedriver_binary
from selenium import webdriver
import datetime

from driver import login, submit_form

from settings import PAGE_LINK, MAIL_ADDRESS, PASSWORD

from weekday import is_weekend
from temperature import temperature
import elements

# driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

login(driver, PAGE_LINK, MAIL_ADDRESS, PASSWORD)

submit_form(driver, temperature, is_weekend(datetime.date.today()), elements)

driver.close()
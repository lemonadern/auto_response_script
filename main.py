import chromedriver_binary
from dotenv import main
from selenium import webdriver
import datetime

from package.driver import login, submit_form

from settings import PAGE_LINK, MAIL_ADDRESSES, PASSWORDS

from package.weekday import is_weekend
from package.temperature import temperature
from package import elements

mail_addresses = MAIL_ADDRESSES.split(',')
passwords = PASSWORDS.split(',')

for i in range(len(mail_addresses)):
    # driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    login(driver, PAGE_LINK, mail_addresses[i], passwords[i])

    submit_form(driver, temperature, is_weekend(datetime.date.today()), elements)

    driver.close()
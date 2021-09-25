from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, page_link, mail_address, password):
    driver.get(page_link)

    email_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'i0116')))
    email_field.send_keys(mail_address)
    driver.find_element_by_id("idSIButton9").click()

    password_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'i0118')))
    password_field.send_keys(password)
    driver.find_element_by_id("idSIButton9").click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'idBtn_Back'))).click()

def submit_form(driver, temperature, is_weekend, elements):
    temperature_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, elements.temperature_xpath)))
    temperature_field.send_keys(str(temperature))

    symptom_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, elements.symptom_xpath)))
    symptom_field.click()

    if(is_weekend):
        absent_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, elements.absent_xpath)))
        absent_field.click()
    else:
        attend_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, elements.attend_xpath)))
        attend_field.click()

    mail_checkbox_field = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, elements.mail_checkbox_xpath)))
    mail_checkbox_field.click()

    submit_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, elements.submit_xpath)))
    submit_button.click()
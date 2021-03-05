import chromedriver_binary
from selenium import webdriver
import time
import random

# ----------------------------------------------- #
# 事前準備
# important_variables
mail = "メールアドレス"
pw = "パスワード"

# 例の報告リンク
link = '報告ページのURL'
# ----------------------------------------------- #

# 体温生成(35.5~36.5度)
temp = str(35.5 + (random.randrange(10))/10)

# 使うxpath
temp_xpath = '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input'
symptom_xpath = '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input'
go_xpath = '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/label/input'
notgo_xpath = '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/label/input'
checkmail_xpath = '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/div/label/input'
send_xpath = '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/button'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(link)
time.sleep(2)

driver.find_element_by_id("i0116").send_keys(mail)
driver.find_element_by_id("idSIButton9").click()
time.sleep(1)

driver.find_element_by_id('i0118').send_keys(pw)
driver.find_element_by_id("idSIButton9").click()
time.sleep(0.5)
driver.find_element_by_id('idSIButton9').click()

driver.find_element_by_xpath(temp_xpath).send_keys(temp)
driver.find_element_by_xpath(symptom_xpath).click()
# 登校しません
driver.find_element_by_xpath(notgo_xpath).click()

# チェックメールを送信(不要なら削除)
driver.find_element_by_xpath(checkmail_xpath).click()

driver.find_element_by_xpath(send_xpath).click()

driver.close()
driver.quit()
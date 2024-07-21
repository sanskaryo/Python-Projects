from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

username = 'sankhuzzy@gmail.com'
password = 'Mynameisdon2'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

time.sleep(2)

reject_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
reject_cookies.click()

email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(username)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)


#Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")


 
driver.quit()

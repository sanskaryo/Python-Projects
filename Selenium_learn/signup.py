from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")


first = driver.find_element(By.NAME, "fName")
last = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first.send_keys("John")
last.send_keys("cena")
email.send_keys("John.cena.ambaniWedding@jio.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

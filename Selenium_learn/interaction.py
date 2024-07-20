from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

event1 = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

print(event1.text)

driver.quit()
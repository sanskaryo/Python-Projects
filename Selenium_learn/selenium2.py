from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/instant_pot/")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CSS_SELECTOR, value=".a-price-fraction")
print(f"{price_dollar.text}.{price_cents.text}")

driver.quit()

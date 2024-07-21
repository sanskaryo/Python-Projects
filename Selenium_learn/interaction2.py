from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Uncomment these lines if you want to click on the article count
# event1 = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# event1.click()
# print(event1.text)

all_portal = driver.find_element(By.LINK_TEXT, "Content portals")


search = driver.find_element(By.CSS_SELECTOR, "#searchInput")

search.send_keys("Python")
search.send_keys(Keys.ENTER)


try:
  
    pass
finally:
    driver.quit()
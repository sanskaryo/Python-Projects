from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for n in range(len(event_names)):
    print(f"{n+1}. {event_names[n].text}")
    
events = {}

for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
    print()
print(events)
driver.quit()





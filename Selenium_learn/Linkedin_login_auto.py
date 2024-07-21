from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your LinkedIn credentials



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    # Wait for the page to load
    time.sleep(2)

    # Find and fill the username field
    email_field = driver.find_element(By.ID, 'username')
    email_field.send_keys(username)

    # Find and fill the password field
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to ensure login is successful
    time.sleep(5)
    
    # You can add more actions here after login

finally:
    # Close the WebDriver
    driver.quit()

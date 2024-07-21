from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script finishes
chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL certificate errors
chrome_options.add_argument('--ignore-ssl-errors')  # Ignore SSL/TLS errors

# Initialize the WebDriver with Chrome options
driver = webdriver.Chrome(service=Service('C:/WebDriver/chromedriver.exe'), options=chrome_options)

# Open a website
driver.get("https://www.amazon.in")

# Your code to interact with the website

# Quit the driver
driver.quit()

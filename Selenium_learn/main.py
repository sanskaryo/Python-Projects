from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Amazon India
driver.get("https://www.amazon.in/")

# Wait for the price elements to be present
try:
    # Wait for some other element on the page to ensure it's loaded
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
    )

    price_dollar = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
    )
    price_cents = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction"))
    )
    print(f"{price_dollar.text}.{price_cents.text}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

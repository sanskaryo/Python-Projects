from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Define promised speeds
promised_down = 60
promised_up = 45

# Twitter credentials (update these with your actual credentials)
twitter_username = ""
twitter_password = ""

class InternetSpeedBot:
    def __init__(self):
        self.driver = driver
        self.up = 0
        self.down = 0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".start-text"))
        )
        
        try:
            # Wait for and close the cookie consent popup if it appears
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            ).click()
        except:
            pass

        go_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-text")
        go_button.click()
        time.sleep(60)
        
        download_speed = self.driver.find_element(by=By.CSS_SELECTOR, value=".download-speed")
        upload_speed = self.driver.find_element(by=By.CSS_SELECTOR, value=".upload-speed")
        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)
        print(f"Download: {self.down} Mbps, Upload: {self.up} Mbps")
        
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        username_field = self.driver.find_element(by=By.CSS_SELECTOR, value="input[name='text']")
        username_field.send_keys(twitter_username)
        
        # Use provided XPath for the "Next" button
        next_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div/button[2]/div/span/span')
        next_button.click()
        time.sleep(2)
        
        password_field = self.driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
        password_field.send_keys(twitter_password, Keys.ENTER)
        time.sleep(5)
        
        tweet_box = self.driver.find_element(by=By.CSS_SELECTOR, value="div[aria-label='Tweet text']")
        complaint = f"Hey @YourISP, my internet speed is {self.down} Mbps download and {self.up} Mbps upload. Promised speeds are {promised_down} Mbps down and {promised_up} Mbps up. Please resolve this issue."
        tweet_box.send_keys(complaint)
        tweet_button = self.driver.find_element(by=By.CSS_SELECTOR, value="div[data-testid='tweetButtonInline']")
        tweet_button.click()


if __name__ == "__main__":
    bot = InternetSpeedBot()
    bot.get_internet_speed()
    if bot.down < promised_down or bot.up < promised_up:
        bot.tweet_at_provider()

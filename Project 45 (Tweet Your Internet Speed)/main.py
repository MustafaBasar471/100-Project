from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


DOWNLOAD = 50
UPLOAD = 10
driver_path = "path here"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.dowm = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(5)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

    def tweet_at(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        mail_input = self.driver.find_element_by_name("text")
        mail_input.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(3)
        
        password_input = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span')
        login_button.click()
        time.sleep(3)

        tweet_area = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/span/span')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {DOWNLOAD}down/{UPLOAD}up?"
        tweet_area.send_keys(tweet)
        time.sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div')
        tweet_button.click()
        time.sleep(2)


        self.driver.quit()
bot = InternetSpeedTwitterBot(driver_path)
bot.get_internet_speed()
bot.tweet_at()



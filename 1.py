from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path to chromedriver in your computer
driver = webdriver.Chrome('/chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = "friends_name"

# Replace the below string with your own message
string = "How you doin'..??;)"

y_arg = '//*[@id="side"]/div[2]/div/label/input'
input_y = wait.until(EC.presence_of_element_located((By.XPATH, y_arg)))
input_y.send_keys(target + Keys.ENTER)
inp_xpath = '//*[@id="main"]//footer//div[contains(@class, "input")]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
for i in range(10):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
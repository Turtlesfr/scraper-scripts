from selenium import webdriver
import urllib.request
import os
import time
from time import sleep 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions    import StaleElementReferenceException
from selenium.common.exceptions    import WebDriverException
from selenium.common.exceptions    import TimeoutException as SeleniumTimeoutException
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
#driver = webdriver.PhantomJS(executable_path=r'C:\Users\Alexandre\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe')
driver.set_window_size(800, 550)

driver.get("https://;")
time.sleep(2) # seconds
username_input = driver.find_element_by_name('login_username')
username_input.send_keys('')
password_input = driver.find_element_by_name('login_password')
password_input.send_keys('')
password_input.send_keys(Keys.ENTER)
#driver.find_element_by_xpath(".//*/a[[contains(text()='Me connecter')]").click()

time.sleep(8) # seconds

with open("i-user-message.txt") as in_file:
    for url in in_file:
        driver.implicitly_wait(3) # seconds
        driver.get(url.strip())
        print(url.strip())
        time.sleep(2) # seconds

        subject_input = driver.find_element_by_name('msg_subject')
        subject_input.send_keys('Hey')
        time.sleep(2) # seconds        driver.switch_to_frame(0)
        
        driver.switch_to_frame(0)
        driver.switch_to_frame(0)
        message_input = driver.find_element_by_id('editable_content')
        message_input.click()
        message_input.send_keys("Hi")
        time.sleep(1)
        message_input.send_keys(Keys.SHIFT, Keys.ENTER)
        message_input.send_keys(Keys.SHIFT, Keys.ENTER)
        message_input.send_keys("Ca boom ? ");
        message_input.send_keys(Keys.SHIFT, Keys.ENTER)
        time.sleep(1)
        message_input.send_keys(Keys.SHIFT, Keys.ENTER)
        message_input.send_keys("Regards")

        driver.switch_to_default_content()
        time.sleep(1)

        driver.find_element_by_id("sentButton").click()
        
        time.sleep(3) # seconds
        driver.switch_to_default_content()
        
        

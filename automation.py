from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option('detach', True)

service = Service(executable_path='./chromedriver')

chrome_browser = webdriver.Chrome(options=options, service=service)

chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('Awesome!')

show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')

assert 'Awesome!' in output_message.text

chrome_browser.quit()

#test commit please!!!
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import user_name, phone
from random import randrange

import selenium.common.exceptions
import telebot
import time
import datetime
import config



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
chrome_options.headless = False
browser = webdriver.Chrome(r'chromedriver.exe', options=chrome_options)
wait = WebDriverWait(browser, 10)

tb = telebot.TeleBot(config.TOKEN)  # инициализация теле_бота


browser.get('https://sovajewels.com/catalog/braslety/bracelet-united24-azovsteel.html') #искомое
# browser.get('https://sovajewels.com/ua/catalog/braslety/braslet-iz-belogo-zolota-story-artikul-400935710201.html') #тест урл
count = 0
print('start...')
def foo():
    name_input = browser.find_element(By.CLASS_NAME, 'def-input__input')
    name_input.clear()
    name_input.send_keys(f'{user_name}')
    phone_num_input = browser.find_element(By.CLASS_NAME, 'def-phone__input')
    phone_num_input.clear()
    phone_num_input.send_keys(f'{phone}')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, 'form[class="def-buy-one-click-form"]>button[class = def-button-primary]').click()
while True:
    try:
        elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'def-button-secondary.def-buy-one-click')))
        if elem:
            elem.click()
            print('TRUE')
            foo()
            browser.quit()
            for r in range(100):
                tb.send_message(config.chat_id, 'KURWA BEGI EBANII VROT!!!!\n https://sovajewels.com/catalog/braslety/bracelet-united24-azovsteel.html')  # Бот отправляет сообщения в телеграм
                time.sleep(10)
            quit()
    except selenium.common.exceptions.TimeoutException as EX:
        print(f'Product not found:\n Count: {count}\n time: {datetime.datetime.today().strftime("%H:%M:%S")}')
        browser.refresh()
        time.sleep(randrange(4, 10))
        count = count + 1
        continue



"""
Lesson 24 step 8, Example

Ждем нужный текст на странице

wait.until(EC.text_to_be_present_in_element(
    (By.ID, "price"), "$100"))              # (By.ID, "price") это кортеж!
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os, time
import math, numpy

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
wait = WebDriverWait(browser, 12)

wait.until(EC.text_to_be_present_in_element(
    (By.ID, "price"), "$100"))

try:
    button = browser.find_element_by_tag_name("button")
    button.click()

    x_element = browser.find_element_by_css_selector('#input_value')
    x = int(x_element.text)
    text = str(math.log(abs(12*numpy.sin(x))))

    # заполняем форму
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(text)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

    #Check, we passed registration
    #Wait page loading
    time.sleep(1)

finally:

    # Wait for visiable check succes of the script
    time.sleep(15)
    # Terminate browser
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)

    value = browser.find_element(By.ID, "answer")
    value.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()

    radiobaton = browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    

    

    

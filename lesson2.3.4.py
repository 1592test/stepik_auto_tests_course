from selenium import webdriver
from selenium.webdriver.common.by import By
import math



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
button1.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element(By.ID,'input_value')
x = x_element.text

answer = browser.find_element(By.ID,'answer')
answer.send_keys(calc(int(x)))


button2 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
button2.click()       

print(browser.switch_to.alert.text)

                                                         


import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

element1 = browser.find_element(By.CSS_SELECTOR,"[name='firstname']")
element1.send_keys('AAA')
element2 = browser.find_element(By.CSS_SELECTOR,"[name='lastname']")
element2.send_keys('Aaaa')
element3 = browser.find_element(By.CSS_SELECTOR,"[name='email']")
element3.send_keys('e@mai.l')
element4 = browser.find_element(By.ID,"file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element4.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
button.click()

browser.close()
                      


                                                         


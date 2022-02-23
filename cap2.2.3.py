from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

	btn = browser.find_element_by_id("book").click()
	
	inp = browser.find_element_by_id("answer")
	xx = browser.find_element_by_id("input_value")	
	xxtext = xx.text
	inp.send_keys(calc(xxtext))
	browser.find_element_by_css_selector("[type='submit']").click()
finally:
   time.sleep(2)
   browser.quit()

# Работа с открытие нового окна.

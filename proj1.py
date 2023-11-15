from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start the browser
service_obj = Service(
    "/Users/jonathantsai/Selenium/Project1/geckodriver")  # web driver path
driver = webdriver.Firefox(service=service_obj)
# driver = webdriver.Firefox() or driver = webdriver.Safari() - need to set "allow remote automation"
url = "https://duckduckgo.com/"
driver.get(url)
driver.maximize_window()
# time.sleep(3)
# driver.close()
# By.TAG_NAME, By.CLASS_NAME, By.NAME, BY.LINK_TEXT, By.PARTIAL_LINK_TEXT, and By.XPATH
# e.g. search = driver.find.element(by=By.XPATH, value="//input[@]")
search = driver.find_element(
    by=By.XPATH, value="//input[@id='searchbox_input']")
time.sleep(2)  # must allow template engine to work
search.send_keys('erb')
search.send_keys(Keys.ENTER)
# toggle = driver.find_element(
#     by=By.XPATH, value="//span[@class='switch__knob']")
# toggle.click()
search.clear()  # clear the input
search.click()
driver.back()  # nav back
driver.refresh()
driver.forward()
time.sleep(100)
driver.close()

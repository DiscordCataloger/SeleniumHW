from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

service_obj = Service(
    "/Users/jonathantsai/Selenium/Project1/geckodriver")
driver = webdriver.Firefox(service=service_obj)
url = "https://hk.yahoo.com/"
driver.get(url)
driver.maximize_window()
login = driver.find_element(
    by=By.XPATH, value="//a[@id='header-signin-link']")
time.sleep(3)
login.click()
register = driver.find_element(by=By.XPATH, value="//a[@id='createacc']")
time.sleep(3)
register.click()
firstname = driver.find_element(
    by=By.XPATH, value="//input[@id='usernamereg-firstName']")
firstname.send_keys('erb')
lastname = driver.find_element(by=By.ID, value="usernamereg-lastName")
lastname.send_keys(100)
email = driver.find_element(
    by=By.XPATH, value="//input[@id='usernamereg-userId']")
email.send_keys("erbhello100")
password = driver.find_element(by=By.ID, value="usernamereg-password")
password.send_keys("EraHello-100")
bdaymonth = Select(driver.find_element(
    by=By.ID, value="usernamereg-month"))
bdaymonth.select_by_value("12")
bday = driver.find_element(by=By.ID, value="usernamereg-day")
bday.send_keys('23')
bdayyear = driver.find_element(by=By.ID, value="usernamereg-year")
bdayyear.send_keys('1967')
time.sleep(2)
submit = driver.find_element(by=By.ID, value="reg-submit-button")
submit.click()
phone = driver.find_element(by=By.ID, value="usernamereg-phone")
time.sleep(2)
phone.send_keys(65726986)
time.sleep(2)
submit2 = driver.find_element(by=By.ID, value="reg-submit-button")
submit2.click()
time.sleep(2)
driver.close()

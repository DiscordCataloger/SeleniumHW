import os
import subprocess
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display
from PIL import Image
from selenium.webdriver.common.keys import Keys
import imageio
import time
import io

# Set up a virtual display and start the browser
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Navigate to the website
driver.get("https://deepstatemap.live/en")
driver.maximize_window()

# Close all pop-ups
time.sleep(8)
popup1 = driver.find_element(
    By.XPATH, "//div[@class='cl-dialog-close-icon']//*[name()='svg']")
popup1.click()

popup2 = driver.find_element(By.XPATH, "//button[@class='agree']")
popup2.click()

# Zoom
map_element = driver.find_element("css selector", "#map")
actions = ActionChains(driver)
# Drag the map to a specific spot
actions.click_and_hold(
    map_element).move_by_offset(-200, -250).release().perform()
# Click and drag the map
for _ in range(2):
    actions.click_and_hold().move_by_offset(0, 0).release().perform()
    time.sleep(0.2)  # pause between each scroll action to simulate slower zoom


history = driver.find_element(By.XPATH, "//img[@title='History Calendar']")
history.click()

# Initialize a list to store the screenshots
screenshots = []

# Find the date input field
date_input = driver.find_element(By.CSS_SELECTOR, "#history-calendar")

# Clear the input field
date_input.clear()

# Input a date
date_input.send_keys("2023-10-15")

# Wait for up to 1 second for the button to appear
time.sleep(1)
close = driver.find_element(By.XPATH, "//div[@class='history__datetime']")
close.click()

# # Rewind time
# stop_time = time.time() + 20
# while time.time() < stop_time:
#     history_button = driver.find_element(
#         By.XPATH, "//img[@src='/images/arrow-prev.png']")
#     history_button.click()

# Start speeding up map transitioning to 3x
speed_up = driver.find_element(
    By.XPATH, "//button[@class='history-nav speed']")
speed_up.click()

# Capture screenshots of the map every minute for a day
end_time = time.time() + 30
while time.time() < end_time:
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(screenshot))
    screenshots.append(image)

# Save the screenshots as a GIF
imageio.mimsave('map_transitions.gif', screenshots, duration=1)

# Zoom out before closing
zoom_out = driver.find_element(By.XPATH, "//a[@title='Zoom out']")
zoom_out.click()
time.sleep(0.5)
# Close the browser
driver.quit()

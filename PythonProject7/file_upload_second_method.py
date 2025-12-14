import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()

time.sleep(2)  # Wait for page to load

# Click file input to open OS file dialog
file_input = driver.find_element(By.ID, "file-upload")
driver.execute_script("arguments[0].click();", file_input)  # JS click works in Firefox

time.sleep(2)  # Wait for dialog to open

# Use PyAutoGUI to type file path and press Enter
file_path = r"C:\Users\Noor Ul Ain\Desktop\application.docx"
pyautogui.write(file_path)
time.sleep(0.5)
pyautogui.press('enter')

time.sleep(2)  # Wait for file selection to register

# Click Upload button
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

time.sleep(3)
driver.quit()

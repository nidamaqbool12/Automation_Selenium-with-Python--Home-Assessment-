from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()


file_input = driver.find_element(By.ID, "file-upload")

file_input.send_keys(r"C:\Users\Noor Ul Ain\Desktop\application.docx")  # Example: Windows path
time.sleep(2)
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

# Wait to see result
time.sleep(3)

driver.quit()


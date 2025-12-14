from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# CSV se user data load karo
with open("form-data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    users = list(reader)

for user in users:
    driver = webdriver.Chrome()
    driver.get("https://services.itspk.com/createservice")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 10)

    try:
        # Service dropdown
        service_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "serviceSelect"))))
        service_dropdown.select_by_visible_text(user["Service"])

        # Attachment (file upload)
        attachment_input = driver.find_element(By.ID, "attachment")
        time.sleep(3)
        attachment_input.send_keys(user["AttachmentPath"])
        time.sleep(3)

        # Suffix dropdown
        suffix_dropdown = Select(driver.find_element(By.ID, "suffixSelect"))
        suffix_dropdown.select_by_visible_text(user["Suffix"])

        # First Name
        driver.find_element(By.ID, "firstName").send_keys(user["FirstName"])

        # Last Name
        driver.find_element(By.ID, "lastName").send_keys(user["LastName"])

        # Email
        driver.find_element(By.ID, "email").send_keys(user["Email"])

        # Password
        driver.find_element(By.ID, "password").send_keys(user["Password"])

        # Country dropdown
        country_dropdown = Select(driver.find_element(By.ID, "countrySelect"))
        country_dropdown.select_by_visible_text(user["Country"])  # Example: "Pakistan"

        # Description
        driver.find_element(By.ID, "description").send_keys(user["Description"])
        time.sleep(5)  # Just to visually verify before closing

        submit_button = driver.find_element(By.CSS_SELECTOR, "button.custom-submit-btn")
        submit_button.click()

    finally:
        driver.quit()

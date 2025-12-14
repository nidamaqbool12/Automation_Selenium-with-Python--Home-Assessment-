import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

CSV_PATH = "created_users.csv"
URL = "https://services.itspk.com"

# Skipping 11th row (1-based index)
SKIP_ROW_NUM = 4

driver = webdriver.Firefox()
driver.maximize_window()


def login_and_logout(email, password):
    driver.get(URL)

    # Login process
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-secondary").click()

    time.sleep(3)  # Wait 3 seconds after login

    # Click on settings and logout
    driver.find_element(By.XPATH, "(//i[@class='ti ti-settings fs-10'])[1]").click()
    driver.find_element(By.XPATH, "(//a[contains(@onclick, 'logout-form')])[1]").click()
    time.sleep(2)  # Optional wait for logout to complete


with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row_num, row in enumerate(reader, start=1):
        if row_num == SKIP_ROW_NUM:
            print(f"Skipping row {row_num}")
            continue

        email = row.get("Email")  # Changed to match the header in your CSV
        password = row.get("Password")  # Changed to match the header in your CSV

        if not email or not password:
            print(f"Row {row_num} missing email/password — skipping")
            continue

        try:
            login_and_logout(email, password)
            print(f"[Row {row_num}] Successfully logged out user: {email}")
        except Exception as e:
            print(f"[Row {row_num}] Error: {e}")

driver.quit()

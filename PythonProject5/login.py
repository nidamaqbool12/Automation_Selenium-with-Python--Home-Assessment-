import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Reading user data from CSV file
with open("user-login.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    users = list(reader)

for user in users:
    driver = webdriver.Firefox()
    driver.get("https://services.itspk.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:

        username = wait.until(EC.presence_of_element_located((By.ID, "email")))
        username.send_keys(user["email"])
        print("--------------------PASSED#01-----------------------")
        print(f"Successfully typed the username: {user['email']}")
        print("                                            ")
        time.sleep(1)


        password = driver.find_element(By.ID, "password")
        password.send_keys(user["password"])
        print("--------------------PASSED#02-----------------------")
        print(f"Successfully typed the password for: {user['email']}")
        print("                                            ")
        time.sleep(1)


        signIn = driver.find_element(By.XPATH, "//button[@class='btn btn-secondary']")
        signIn.click()
        print("--------------------PASSED#03--------------------------")
        print(f"Successfully clicked Sign In for: {user['email']}")
        time.sleep(3)

    except Exception as e:
        print(f"[ERROR] Failed for user {user['email']}: {e}")

    driver.quit()






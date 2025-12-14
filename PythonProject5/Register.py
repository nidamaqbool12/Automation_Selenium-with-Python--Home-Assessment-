import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read CSV file
with open("Valid_Register_data.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    users = list(reader)

for user in users:
    driver = webdriver.Chrome()
    driver.get("https://conference.itspk.com/register/1/0")
    driver.set_window_size(1920, 1080)

    wait = WebDriverWait(driver, 10)

    # FIELD ASSERTIONS
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='auth-left']/div[1]/form/div[1]/div/input"))), "Email field not found"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='auth-left']/div[1]/form/div[2]/div/input"))), "First name field not found"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='auth-left']/div[1]/form/div[3]/div/input"))), "Last name field not found"
    # Fill basic fields
    driver.find_element(By.XPATH, "//*[@id='auth-left']/div[1]/form/div[1]/div/input").send_keys(user["email"])
    driver.find_element(By.XPATH, "//*[@id='auth-left']/div[1]/form/div[2]/div/input").send_keys(user["first_name"])
    driver.find_element(By.XPATH, "//*[@id='auth-left']/div[1]/form/div[3]/div/input").send_keys(user["last_name"])
    driver.find_element(By.XPATH, "//input[@placeholder='Company/Instititution Name *']").send_keys(user["company"])
    driver.find_element(By.XPATH, "//input[@placeholder='Home Phone ']").send_keys(user["home_phone"])
    driver.find_element(By.XPATH, "(//input[@placeholder='Cell Phone *'])[1]").send_keys(user["cell_phone"])


    time.sleep(4)


    # Select Registration Type
    role_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "roleSelect")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", role_dropdown)
    if user.get("registration_type"):
        Select(role_dropdown).select_by_visible_text(user["registration_type"])

    time.sleep(1)

    #Select Country
    country_dropdown = wait.until(EC.element_to_be_clickable((By.NAME, "country")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", country_dropdown)
    if user.get("country"):
        Select(country_dropdown).select_by_visible_text(user["country"])

    #City & Province
    driver.find_element(By.XPATH, "//*[@id='auth-left']/div[1]/form/div[9]/div/input").send_keys(user["city"])
    driver.find_element(By.XPATH, "//*[@id='auth-left']/div[1]/form/div[10]/div/input").send_keys(user["province"])

    #Password fields
    driver.find_element(By.XPATH,
                        "//*[@id='password']").send_keys(user["password"])
    driver.find_element(By.XPATH, "//*[@id='confirm_password']").send_keys(user["confirm_password"])


    toggle_button = wait.until(EC.element_to_be_clickable((By.ID, "toggleFields")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle_button)
    driver.execute_script("arguments[0].click();", toggle_button)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='fieldContainer']/div/div/div[1]/div/input").send_keys(user["extra1"])
    driver.find_element(By.XPATH, "//*[@id='fieldContainer']/div/div/div[2]/div/input").send_keys(user["extra2"])
    driver.find_element(By.XPATH, "//*[@id='fieldContainer']/div/div/div[3]/div/input").send_keys(user["extra3"])

    #Submit
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Sign Up']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(2)
    error_messages = driver.find_elements(By.XPATH, "//*[contains(text(),'Please select') or contains(text(),'taken') or contains(@class, 'alert-danger')]")

    if error_messages:
        for err in error_messages:
            print(f"[ERROR] {user['email']} → {err.text}")
    else:
        print(f"[SUCCESS] Registration submitted for {user['email']}.")

    time.sleep(3)
    driver.quit()

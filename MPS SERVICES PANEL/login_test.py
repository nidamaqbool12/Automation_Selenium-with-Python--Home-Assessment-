import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

with open("data_test_login.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    users = list(reader)


for user in users:
    driver = webdriver.Chrome()
    driver.get("https://conference.itspk.com/")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 10)


    # Login
    try:
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
        login_link.click()
    except:
        pass

    wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(user["email"])
    driver.find_element(By.NAME, "password").send_keys(user["password"])
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()

    try:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='https://conference.itspk.com/abstract-submission-form']")
        ))
        print(f"[SUCCESS] {user['email']} logged in successfully.")
    except:
        print(f"[ERROR] {user['email']} failed to log in.")
        driver.quit()
        continue

    # Open submission form
    driver.find_element(By.XPATH, "//a[@href='https://conference.itspk.com/abstract-submission-form']").click()

    # Main track
    try:
        main_track_select = Select(wait.until(
            EC.visibility_of_element_located((By.ID, "mainTrackSelect"))
        ))
        main_track_select.select_by_visible_text(user["main_track"])
    except Exception as e:
        print(f"[WARN] Could not select Main Track for {user['email']}: {e}")

    # Sub track
    try:
        sub_track_select = Select(wait.until(
            EC.visibility_of_element_located((By.ID, "childTrackSelect"))
        ))
        sub_track_select.select_by_visible_text(user["sub_track"])
    except Exception as e:
        print(f"[WARN] Could not select Sub Track for {user['email']}: {e}")

    # Fill form
    wait.until(EC.visibility_of_element_located((By.NAME, "title"))).send_keys(user["title"])
    driver.find_element(By.NAME, "abstract").send_keys(user["abstract"])

    # Keywords
    try:
        keywords_input = driver.find_element(
            By.XPATH, "//div[@class='bootstrap-tagsinput col-md-12']//input[@placeholder='Press enter to insert']"
        )
        for keyword in user["keywords"].split(","):
            keywords_input.send_keys(keyword.strip())
            keywords_input.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"[WARN] Could not fill keywords for {user['email']}: {e}")

    # Reference code
    try:
        driver.find_element(By.ID, "reference_number").send_keys(user["manuscript_ref_code"])
    except Exception as e:
        print(f"[WARN] Could not fill manuscript ref code for {user['email']}: {e}")
        time.sleep(3)

    # ===== VALIDATION before submit =====
    title_text = user["title"]
    abstract_text = user["abstract"]
    keywords_list = [k.strip() for k in user["keywords"].split(",") if k.strip()]

    title_len = len(title_text)
    abstract_word_count = len(abstract_text.split())
    keywords_count = len(keywords_list)

    if title_len != 50:
        print(f"[VALIDATION ERROR] {user['email']}: Title must be exactly 50 characters (got {title_len}).")
        driver.quit()
        continue

    if abstract_word_count != 200:
        print(f"[VALIDATION ERROR] {user['email']}: Abstract must be exactly 200 words (got {abstract_word_count}).")
        driver.quit()
        continue

    if keywords_count != 7:
        print(f"[VALIDATION ERROR] {user['email']}: Keywords must have exactly 7 items (got {keywords_count}).")
        driver.quit()
        continue

    #Submit only if all checks pass
    try:
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", submit_btn)
        print(f"[INFO] Submission completed for {user['email']}.")
    except Exception as e:
        print(f"[ERROR] Could not submit form for {user['email']}: {e}")

    time.sleep(3)
    driver.quit()

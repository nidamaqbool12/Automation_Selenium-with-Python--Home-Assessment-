import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# -------------------- HTML LOGGING & REPORT ---------------------
html_logs = []

def log(message):
    """Logs messages to console and HTML report."""
    print(message)
    html_message = message
    if "Passed" in message or "PASS" in message:
        html_message = f'<span style="color: green; font-weight: bold;">{message}</span>'
    elif "Failed" in message or "FAIL" in message or "Unexpected" in message:
        html_message = f'<span style="color: red; font-weight: bold;">{message}</span>'
    elif message.startswith("-"*50):
        html_message = message.replace("-", '<hr style="border: 1px dashed #bbb;">')
    html_logs.append(html_message)

def generate_html_report():
    report_path = "Automation_Report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Automation Report</title>")
        f.write("<style>")
        f.write("body { font-family: 'Consolas', 'Courier New', monospace; background-color: #f4f4f4; padding: 20px; }")
        f.write(".container { background-color: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }")
        f.write("h2 { color: #333; border-bottom: 2px solid #ccc; padding-bottom: 10px; }")
        f.write("</style>")
        f.write("</head><body><div class='container'>")
        f.write("<h2>Automation Execution Report</h2>")
        f.write(f"<p><strong>Generated on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        f.write("<pre style='background-color:#fff;padding:15px;border:1px solid #ccc; white-space: pre-wrap; word-wrap: break-word;'>")
        for line in html_logs:
            f.write(line + "\n")
        f.write("</pre></div></body></html>")
    log(f"[✓] HTML report saved at: {os.path.abspath(report_path)}")

# -------------------- SELENIUM DRIVER ---------------------
driver = webdriver.Firefox()

def open_login_page():
    driver.get("https://test-jms.eurekaselect.com/Login/show_login")
    time.sleep(2)

def perform_login(user_email, user_password):
    email_field = driver.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys(user_email)
    password_field = driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys(user_password)
    login_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
    login_btn.click()
    time.sleep(2)

#----------------------POSITIVE TEST CASES------------------------
#----------------------POSITIVE TC_01-----------------------------
log("                      Positive Test Cases for Author Login                                               ")
log("")
log("---------------------------------------POSITIVE TC_01----------------------------------------------------")
log("Login with valid email and password after login it should redirect to the Dashboard Page.")

open_login_page()
perform_login("Jennifer@testingxolva.com","1#25QL&Hda")

if "dashboard" in driver.current_url.lower():
    log("Passed TestCase:Positive TC_01 - Valid email and valid password: Login successful")
    try:
        logout = driver.find_element(By.XPATH, "//a[@class='waves-effect waves-light']//i[@class='md md-settings-power']")
        logout.click()
        log("Logged out successfully.")
    except Exception:
        log("Logout button not found or an error occurred during logout.")
else:
    log("Failed TestCase:Positive TC_01 - Login with valid credentials: but it doesn't redirect to the Dashboard Page: Login failed")
    log("Your session has expired. please sign-in again")
time.sleep(2)

#----------------------POSITIVE TC_02-----------------------------
log(" ")
log("---------------------------------------POSITIVE TC_02----------------------------------------------------")
log("Refreshing the page before login")

open_login_page()
driver.refresh()
perform_login("Jennifer@testingxolva.com","1#25QL&Hda")

if "dashboard" in driver.current_url.lower():
    log("Passed TestCase:Positive TC_02 - Valid email and valid password: Login successful")
    try:
        logout = driver.find_element(By.XPATH, "//a[@class='waves-effect waves-light']//i[@class='md md-settings-power']")
        logout.click()
        log("Logged out successfully.")
    except Exception:
        log("Logout button not found or an error occurred during logout.")
else:
    log("Failed TestCase:Positive TC_02 - Login with valid credentials: but it doesn't redirect to the Dashboard Page: Login failed")
    log("Your session has expired. please sign-in again")
time.sleep(2)

#----------------------NEGATIVE TEST CASES------------------------
log("                                Negative Test Cases for Author Login                                               ")
log("")

#----------------------NEGATIVE TC_01-----------------------------
log("---------------------------------------NEGATIVE TC_01----------------------------------------------------")
log("Leave both email and password fields empty and click the login button.")
open_login_page()
perform_login(" ", " ")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase: NEGATIVE TC_01 - Empty fields,Login Blocked!")
else:
    log("Failed TestCase:NEGATIVE TC_01 - Empty fields: Unexpected behavior!")
time.sleep(2)

#----------------------NEGATIVE TC_02-----------------------------
log("---------------------------------------NEGATIVE TC_02----------------------------------------------------")
log("Enter an email with numbers (e.g.Jennifer@23testingxolva.com) and a valid password, then click the Sign In button.")
open_login_page()
perform_login("Jennifer@23testingxolva.com", "1#25QL&Hda")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase: NEGATIVE TC_02 - Email with numbers format: Login blocked !")
else:
    log("Failed TestCase:NEGATIVE TC_02 - Email with numbers format: Unexpected behavior ")
time.sleep(2)

#----------------------NEGATIVE TC_03-----------------------------
log("---------------------------------------NEGATIVE TC_03----------------------------------------------------")
log("Login using the Enter key")
open_login_page()
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("Jennifer@testingxolva.com")
password_field = driver.find_element(By.ID, "password")
password_field.clear()
password_field.send_keys("1#25QL&Hda")
time.sleep(1)
password_field.send_keys(Keys.ENTER)
time.sleep(3)
if "Dashboard" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_03 - Valid email and valid password: Login successful")
    try:
        logout = driver.find_element(By.XPATH, "//a[@class='waves-effect waves-light']//i[@class='md md-settings-power']")
        logout.click()
        log("Logged out successfully.")
    except Exception:
        log("Logout button not found or an error occurred during logout.")
else:
    log("Failed TestCase:Negative TC_03 - Login with valid credentials: but it doesn't redirect to the Dashboard Page: Login failed")
    log("Your session has expired. please sign-in again")
time.sleep(2)

#----------------------NEGATIVE TC_04-----------------------------
log("---------------------------------------NEGATIVE TC_04----------------------------------------------------")
log("Enter an email with invalid format (e.g., Jennifer@@testingxolva.com) and a valid password, then click Sign In..")
open_login_page()
perform_login("Jennifer@@testingxolva.com", "1#25QL&Hda")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_04 - Invalid email format: Login blocked")
else:
    log("Failed TestCase:Negative TC_04 -Invalid email format: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_05-----------------------------
log("---------------------------------------NEGATIVE TC_05----------------------------------------------------")
log("Enter the valid email and invalid password click the Sign In button.")
open_login_page()
perform_login("Jennifer@testingxolva.com", "1csdsdcscsda")
if "Login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_05 - Invalid password: Login blocked")
else:
    log("Failed TestCase:Negative TC_05 -Invalid password: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_06-----------------------------
log("---------------------------------------NEGATIVE TC_06----------------------------------------------------")
log("Enter the invalid email and invalid password click the Sign In button.")
open_login_page()
perform_login("Jennifer@@testingxolva.com", "sdsddsd&Hda")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_06 - Invalid email and password: Login blocked")
else:
    log("Failed TestCase:Negative TC_06 -Invalid email and password: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_07-----------------------------
log("---------------------------------------NEGATIVE TC_07----------------------------------------------------")
log("Enter a common SQL injection string in the email field (e.g., ' OR '1'='1) and a valid password, then click Sign In..")
open_login_page()
perform_login("' OR '1'='1' --", "sdsddsd&Hda")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_07 - SQL injection string in the email field: Login blocked")
else:
    log("Failed TestCase:Negative TC_07 -SQL injection string in the email field: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_08-----------------------------
log("---------------------------------------NEGATIVE TC_08----------------------------------------------------")
log("Enter a valid email and password with leading or trailing whitespaces and click Sign In.")
open_login_page()
perform_login("Jennifer@testingxolva.com", "   1#25QL&Hda")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_08 - Invalid email and password: Login blocked")
else:
    log("Failed TestCase:Negative TC_08 -Invalid email and password: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_09-----------------------------
log("---------------------------------------NEGATIVE TC_09----------------------------------------------------")
log("Enter an unregistered email address with a valid password and click Sign In.")
open_login_page()
perform_login("muhammadanas123@testingxolva.com", "1#25QL&Hda")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_09 - Invalid email and password: Login blocked")
else:
    log("Failed TestCase:Negative TC_09 -Invalid email and password: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_10-----------------------------
log("---------------------------------------NEGATIVE TC_10----------------------------------------------------")
log("Enter a valid email with a password shorter than the required minimum and click Sign In.")
open_login_page()
perform_login("Jennifer@testingxolva.com", "1#25QL")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_10 - Invalid email and password: Login blocked")
else:
    log("Failed TestCase:Negative TC_10 -Invalid email and password: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_11-----------------------------
log("---------------------------------------NEGATIVE TC_11----------------------------------------------------")
log("Enter HTML or JavaScript code (e.g., <script>alert(1)</script>) in password field and click Sign In..")
open_login_page()
perform_login("Jennifer@testingxolva.com", "<script>alert(1)</script>")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_11 - HTML/JS code (XSS) attempt: Blocked successfully")
else:
    log("Failed TestCase:Negative TC_11 -HTML/JS code (XSS) attempt: Blocked successfully: Unexpected behavior")
time.sleep(2)

#----------------------NEGATIVE TC_12-----------------------------
log("---------------------------------------NEGATIVE TC_12----------------------------------------------------")
log("Enter the email in uppercase (e.g., JENNIFER@TESTINGXOLVA.COM) if the system is case-sensitive and click Sign In.")
open_login_page()
perform_login("JENNIFER@TESTINGXOLVA.COM", "1#25QL&Hda")
if "show_login" in driver.current_url.lower():
    log("Passed TestCase:Negative TC_12 - Email case sensitivity handled correctly")
else:
    log("Failed TestCase:Negative TC_12 -Email case sensitivity: Unexpected behavior")
time.sleep(2)

# -------------------- CLOSE BROWSER ---------------------
driver.quit()
log("All tests completed. Browser closed.")

# -------------------- GENERATE HTML REPORT ---------------------
generate_html_report()

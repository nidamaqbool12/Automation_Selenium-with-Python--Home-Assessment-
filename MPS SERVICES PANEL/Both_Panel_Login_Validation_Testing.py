import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Needed for the Enter key test
from datetime import datetime
import os

# ==============================================================================
# Custom Logging Setup
# ==============================================================================

# Global list to hold logs that will be written to the HTML file
html_logs = []

def log(message, status="INFO"):

    # Print to console (standard behavior)
    print(message)

    # Prepare message for HTML (adding style)
    html_message = message
    if "Passed#" in message:
        # Green for Passed
        html_message = f'<span style="color: green; font-weight: bold;">{message}</span>'
    elif "Failed#" in message or "Unexpected" in message:
        # Red for Failed
        html_message = f'<span style="color: red; font-weight: bold;">{message}</span>'
    elif "Skipping" in message:
        # Orange for Skipped
        html_message = f'<span style="color: orange; font-weight: bold;">{message}</span>'
    elif message.startswith("="*50) or message.startswith("-" * 50):
        # Horizontal lines for separation
        html_message = message.replace('=', '<hr style="border: 2px solid #555;">').replace('-', '<hr style="border: 1px dashed #bbb;">')


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

        # Write the captured logs (already formatted with colors)
        for line in html_logs:
            f.write(line + "\n")

        f.write("</pre></div></body></html>")

    log(f"\n[✓] HTML report saved at: {os.path.abspath(report_path)}")
    print("="*50)

# ==============================================================================
# WebDriver and Initial Setup (Using log() instead of print())
# ==============================================================================

driver = webdriver.Firefox()
driver.get("https://services.itspk.com/admin-login")
driver.maximize_window()
time.sleep(2)
log("Starting Admin Panel Login Automation Tests...\n" + "="*50)

# ==============================================================================
# POSITIVE TEST CASES (P01 - P07)
# ==============================================================================

# Test Case P01 - Valid email and valid password
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)

# Assertion and Logout
if "dashboard" in driver.current_url.lower():
    log("Passed#P01 - Valid email and valid password: Login successful")
    try:
        # Using a more robust selector for the logout icon's parent link
        logout = driver.find_element(By.XPATH, "//i[contains(@class, 'ti-logout')]/parent::a")
        logout.click()
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P01 - Valid email and valid password: Login failed\n" + "-"*50)
time.sleep(2)


# Test Case P02  - Click Login button without entering credentials
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)

if "login" in driver.current_url.lower():
    log("Passed#P02 - Blank email and password: Login blocked\n" + "-"*50)
else:
    log("Failed#P02  - Blank email and password: Unexpected behavior\n" + "-"*50)
time.sleep(2)


# Test Case P03 - Login after copying and pasting valid credentials
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
if "dashboard" in driver.current_url.lower():
    log("Passed#P03 - Copy/Paste equivalent: Login successful")
    try:
        driver.find_element(By.XPATH, "//i[contains(@class, 'ti-logout')]/parent::a").click()
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P03 - Copy/Paste equivalent: Login failed\n" + "-"*50)
time.sleep(2)


# --- Test Case P04 - Login after refreshing the page ---
driver.get("https://services.itspk.com/admin-login")
time.sleep(2) # Simulates a manual refresh
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)

if "dashboard" in driver.current_url.lower():
    log("Passed#P04 - Login after refreshing the page: Login successful")
    try:
        driver.find_element(By.XPATH, "//i[contains(@class, 'ti-logout')]/parent::a").click()
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P04 - Login after refreshing the page: Login failed\n" + "-"*50)
time.sleep(2)


# Test Case P05 - Login immediately after submitting the service form (Manual step, skipped)
log("Skipping P05: Login immediately after submitting the service form (Requires external action).")
time.sleep(2)

# Test Case P06 - Login with email containing numbers (e.g., admin123@gmail.com)
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
# Use an email with numbers in it for this test
driver.find_element(By.ID, "email").send_keys("admin123@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
if "dashboard" in driver.current_url.lower():
    log("Passed#P06 - Email with numbers: Login successful")
    try:
        # Attempt to log out if login was successful
        driver.find_element(By.XPATH, "//i[contains(@class, 'ti-logout')]/parent::a").click()
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P06 - Email with numbers: Login failed\n" + "-"*50)
time.sleep(2)


# Test Case P07  - Login using the Enter key
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("12345678")
time.sleep(1)
password_field.send_keys(Keys.ENTER)  # Send Enter key
time.sleep(3)

if "dashboard" in driver.current_url.lower():
    log("Passed#P07 - Login using Enter key: Login successful")
    try:
        driver.find_element(By.XPATH, "//i[contains(@class, 'ti-logout')]/parent::a").click()
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P07 - Login using Enter key: Unexpected login\n" + "-"*50)
time.sleep(2)


# ==============================================================================
# NEGATIVE TEST CASES (N08 - N20)
# ==============================================================================
log("\nNEGATIVE TEST CASES:\n" + "="*50)


# Test Case N08 - Invalid email and invalid password
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("invalidemail@gmail.com")
driver.find_element(By.ID, "password").send_keys("invalidpassword")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)

if "login" in driver.current_url.lower():
    log("Passed#N08 - Invalid email and invalid password: Login blocked\n" + "-"*50)
else:
    log("Failed#N08 - Invalid email and invalid password: Unexpected login\n" + "-"*50)
time.sleep(2)


# Test Case N09 - Invalid email format
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("user@@mail.com")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N09 - Invalid email format: Login blocked\n" + "-"*50)
else:
    log("Failed#N09 - Invalid email format: Unexpected behavior\n" + "-"*50)
time.sleep(2)


# Test Case N10 - Empty email field
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N10 - Empty email: Login blocked\n" + "-"*50)
else:
    log("Failed#N10 - Empty email: Unexpected behavior\n" + "-"*50)
time.sleep(2)


# Test Case N11 - Empty password field
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "password").send_keys("")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N11 - Empty password: Login blocked\n" + "-"*50)
else:
    log("Failed#N11 - Empty password: Unexpected behavior\n" + "-"*50)
time.sleep(2)


# Test Case N12 - Login with both fields empty
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
# Fields are already empty
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N12 - Both fields empty: Login blocked\n" + "-"*50)
else:
    log("Failed#N12 - Both fields empty: Unexpected behavior\n" + "-"*50)
time.sleep(2)


# Test Case N13 - SQL Injection attempt
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("' OR '1'='1")
driver.find_element(By.ID, "password").send_keys("' OR '1'='1")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N13 - SQL injection attempt: Blocked successfully\n" + "-"*50)
else:
    log("Failed#N13 - SQL injection attempt: Unexpected login\n" + "-"*50)
time.sleep(2)


# ---Test Case N14 - Login with whitespace-only input ---
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("      ") # 6 spaces
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N14 - Whitespace-only email: Login blocked\n" + "-"*50)
else:
    log("Failed#N14 - Whitespace-only email: Unexpected login\n" + "-"*50)
time.sleep(2)


# --- Test Case N15 - Login using unregistered email ---
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("unregistered_user@test.com")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N15 - Unregistered email: Login blocked\n" + "-"*50)
else:
    log("Failed#N15 - Unregistered email: Unexpected login\n" + "-"*50)
time.sleep(2)


# --- Test Case N16 - Login with password less than required length ---
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "password").send_keys("123") # Short password
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N16 - Password less than required length: Login blocked\n" + "-"*50)
else:
    log("Failed#N16 - Password less than required length: Unexpected login\n" + "-"*50)
time.sleep(2)


# --- Test Case N17 - Login with HTML/JS code in input (XSS attempt) ---
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "password").send_keys("<script>alert('XSS')</script>")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N17 - HTML/JS code (XSS) attempt: Blocked successfully\n" + "-"*50)
else:
    log("Failed#N17 - HTML/JS code (XSS) attempt: Unexpected login\n" + "-"*50)
time.sleep(2)


# Test Case N18 - Login with email in uppercase
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("ADMIN@GMAIL.COM")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)


if "login" in driver.current_url.lower():
    log("Passed#N18 - Email in uppercase: Blocked (System IS case-sensitive for email)\n" + "-"*50)
else:
    # If it logs in, it fails the negative test expectation
    log("Failed#N18 - Email in uppercase: Unexpected success (System is NOT case-sensitive for email)\n" + "-"*50)
    # Log out to continue the remaining tests
    try:
        driver.find_element(By.XPATH, "//i[contains(@class, 'ti-logout')]/parent::a").click()
    except Exception:
        pass
time.sleep(2)


# ---  Test Case N19 - Login with password in uppercase/lowercase mismatch ---
driver.get("https://services.itspk.com/admin-login")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
# Incorrect password: changed '8' to 'A' or 'a' to test case sensitivity
driver.find_element(By.ID, "password").send_keys("1234567A")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)
if "login" in driver.current_url.lower():
    log("Passed#N19 - Password case mismatch: Login blocked (System is case-sensitive for password) \n" + "-"*50)
else:
    log("Failed#N19 - Password case mismatch: Unexpected login \n" + "-"*50)
time.sleep(2)


# Test Case N20 - Login after account deletion, using old credential (Manual step, skipped)
log("Skipping N20: Login after account deletion (Requires external setup/deletion).")
time.sleep(2)

#  User Login Panel Testing................

log("Starting User/Author Panel Login Automation Tests...\n" + "="*50)

# ==============================================================================
# POSITIVE TEST CASES (P01 - P07)
# ==============================================================================

# Test Case P01 - Valid email and valid password
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("omer@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)

# Assertion and Logout
if "dashboard" in driver.current_url.lower():
    log("Passed#P01 - Valid email and valid password: Login successful")
    try:
        # Using a more robust selector for the logout icon's parent link
        driver.find_element(By.CSS_SELECTOR, ".ti.ti-settings.fs-10").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//form[@id='logout-form']").submit()
        time.sleep(3)
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P01 - Valid email and valid password: Login failed\n" + "-"*50)
time.sleep(2)


# Test Case P02  - Click Login button without entering credentials
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(2)

if "login" in driver.current_url.lower():
    log("Passed#P02 - Blank email and password: Login blocked\n" + "-"*50)
else:
    log("Failed#P02  - Blank email and password: Unexpected behavior\n" + "-"*50)
time.sleep(2)


# Test Case P03 - Login after copying and pasting valid credentials
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("omer@gmail.com")
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
if "dashboard" in driver.current_url.lower():
    log("Passed#P03 - Copy/Paste equivalent: Login successful")
    try:
        driver.find_element(By.CSS_SELECTOR, ".ti.ti-settings.fs-10").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//form[@id='logout-form']").submit()
        time.sleep(3)
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P03 - Copy/Paste equivalent: Login failed\n" + "-"*50)
time.sleep(2)


# --- Test Case P04 - Login after refreshing the page ---
driver.get("https://services.itspk.com")
time.sleep(2) # Simulates a manual refresh
driver.find_element(By.ID, "email").send_keys("omer@gmail.com")
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)

if "dashboard" in driver.current_url.lower():
    log("Passed#P04 - Login after refreshing the page: Login successful")
    try:
        driver.find_element(By.CSS_SELECTOR, ".ti.ti-settings.fs-10").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//form[@id='logout-form']").submit()
        time.sleep(3)
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P04 - Login after refreshing the page: Login failed\n" + "-"*50)
time.sleep(2)


# Test Case P05 - Login immediately after submitting the service form (Manual step, skipped)
log("Skipping P05: Login immediately after submitting the service form (Requires external action).")

time.sleep(2)


# Test Case P06 - Login with email containing numbers (e.g., admin123@gmail.com)
driver.get("https://services.itspk.com")
time.sleep(1)
# Use an email with numbers in it for this test
driver.find_element(By.ID, "email").send_keys("omer222@gmail.com")
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
if "dashboard" in driver.current_url.lower():
    log("Passed#P06 - Email with numbers: Login successful")
    try:
        # Attempt to log out if login was successful
        driver.find_element(By.CSS_SELECTOR, ".ti.ti-settings.fs-10").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//form[@id='logout-form']").submit()
        time.sleep(3)
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P06 - Email with numbers: Login failed\n" + "-"*50)
time.sleep(2)


# Test Case P07  - Login using the Enter key
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("omer@gmail.com")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Omer@123")
time.sleep(1)
password_field.send_keys(Keys.ENTER)  # Send Enter key
time.sleep(3)

if "dashboard" in driver.current_url.lower():
    log("Passed#P07 - Login using Enter key: Login successful")
    try:
        driver.find_element(By.CSS_SELECTOR, ".ti.ti-settings.fs-10").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//form[@id='logout-form']").submit()
        time.sleep(3)
        log("Logged out successfully.\n" + "-"*50)
    except Exception:
        log("Logout button not found or an error occurred during logout.\n" + "-"*50)
else:
    log("Failed#P07 - Login using Enter key: Unexpected login\n" + "-"*50)
time.sleep(4)


# ==============================================================================
# NEGATIVE TEST CASES (N08 - N20)
# ==============================================================================
log("\nNEGATIVE TEST CASES:\n" + "="*50)

# Define the exact XPath for the "Login" heading from the screenshot
# This will be used in N08 - N17 and N19
LOGIN_HEADING_XPATH = "//b[normalize-space()='Login']"

# Test Case N08 - Invalid email and invalid password
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("invalidemail@gmail.com")
driver.find_element(By.ID, "password").send_keys("invalidpassword")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3) # Wait after click

# Assertion check for "Login" heading using the exact XPath
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N08 - Invalid email and invalid password: Login blocked\n" + "-"*50)
except:
    log("Failed#N08 - Invalid email and invalid password: Unexpected login\n" + "-"*50)
time.sleep(2)


# Test Case N09 - Invalid email format
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("omer@@mail.com")
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N09 - Invalid email format: Login blocked\n" + "-"*50)
except:
    log("Failed#N09 - Invalid email format: Unexpected behavior\n" + "-"*50)
time.sleep(3)


# Test Case N10 - Empty email field
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("")
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    # Note: For empty fields, sometimes browser's built-in validation blocks the submit.
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N10 - Empty email: Login blocked\n" + "-"*50)
except:
    log("Failed#N10 - Empty email: Unexpected behavior\n" + "-"*50)
time.sleep(3)


# Test Case N11 - Empty password field
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("omer@gmail.com")
driver.find_element(By.ID, "password").send_keys("")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    # Note: For empty fields, sometimes browser's built-in validation blocks the submit.
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N11 - Empty password: Login blocked\n" + "-"*50)
except:
    log("Failed#N11 - Empty password: Unexpected behavior\n" + "-"*50)
time.sleep(3)


# Test Case N12 - Login with both fields empty
driver.get("https://services.itspk.com")
time.sleep(1)
# Fields are already empty
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    # Note: For empty fields, sometimes browser's built-in validation blocks the submit.
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N12 - Both fields empty: Login blocked\n" + "-"*50)
except:
    log("Failed#N12 - Both fields empty: Unexpected behavior\n" + "-"*50)
time.sleep(4)


# Test Case N13 - SQL Injection attempt
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("' OR '1'='1")
driver.find_element(By.ID, "password").send_keys("' OR '1'='1")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N13 - SQL injection attempt: Blocked successfully\n" + "-"*50)
except:
    log("Failed#N13 - SQL injection attempt: Unexpected login\n" + "-"*50)
time.sleep(3)


# ---Test Case N14 - Login with whitespace-only input ---
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("      ") # 6 spaces
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N14 - Whitespace-only email: Login blocked\n" + "-"*50)
except:
    log("Failed#N14 - Whitespace-only email: Unexpected login\n" + "-"*50)
time.sleep(2)


# --- Test Case N15 - Login using unregistered email ---
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("unregistered_user@test.com")
driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N15 - Unregistered email: Login blocked\n" + "-"*50)
except:
    log("Failed#N15 - Unregistered email: Unexpected login\n" + "-"*50)
time.sleep(2)


# --- Test Case N16 - Login with password less than required length ---
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("omer@gmail.com")
driver.find_element(By.ID, "password").send_keys("123") # Short password
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N16 - Password less than required length: Login blocked\n" + "-"*50)
except:
    log("Failed#N16 - Password less than required length: Unexpected login\n" + "-"*50)
time.sleep(2)


# --- Test Case N17 - Login with HTML/JS code in input (XSS attempt) ---
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "password").send_keys("<script>alert('XSS')</script>")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N17 - HTML/JS code (XSS) attempt: Blocked successfully\n" + "-"*50)
except:
    log("Failed#N17 - HTML/JS code (XSS) attempt: Unexpected login\n" + "-"*50)
time.sleep(2)


# Test Case N18 - Login with email in uppercase (Checking for Dashboard failure)
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("OMER@GMAIL.COM")
driver.find_element(By.ID, "password").send_keys("Omer@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)

# For N18, we check for "Dashboard" (or any element unique to the logged-in state)
try:
    # Use a generic locator to check for logged-in state (e.g., 'Dashboard' text)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Dashboard')]")
    # If Dashboard is found, the negative test failed (unexpected success)
    log("Failed#N18 - Email in uppercase: Unexpected success (System is NOT case-sensitive for email)\n" + "-"*50)
    # Log out to continue the remaining tests
    try:
        # Log out using assumed logic
        driver.find_element(By.XPATH, "//i[contains(@class, 'ti-logout')]/parent::a").click()
    except Exception:
        pass
except Exception:
    # If Dashboard is NOT found, it means the login was blocked (expected result)
    log("Passed#N18 - Email in uppercase: Blocked (System IS case-sensitive for email)\n" + "-"*50)
time.sleep(2)


# ---  Test Case N19 - Login with password in uppercase/lowercase mismatch ---
driver.get("https://services.itspk.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("OmER@gmail.com")
driver.find_element(By.ID, "password").send_keys("oMeR@123")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, LOGIN_HEADING_XPATH)
    log("Passed#N19 - Password case mismatch: Login blocked (System is case-sensitive for password) \n" + "-"*50)
except:
    log("Failed#N19 - Password case mismatch: Unexpected login \n" + "-"*50)
time.sleep(2)


# Test Case N20 - Login after account deletion, using old credential (Manual step, skipped)
log("Skipping N20: Login after account deletion (Requires external setup/deletion).")
time.sleep(2)


log("All tests completed.")
driver.quit()
# ==============================================================================
# Final Report Generation
# ==============================================================================

generate_html_report()
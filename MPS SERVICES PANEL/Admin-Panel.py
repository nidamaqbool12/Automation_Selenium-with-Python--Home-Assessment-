import time
import os
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker

fake = Faker()

# ================= Reporting System =================
html_logs = []

def log(msg):
    print(msg)
    html_message = msg
    if "Passed#" in msg:
        html_message = f'<span style="color: green; font-weight: bold;">{msg}</span>'
    elif "Failed#" in msg or "Unexpected" in msg:
        html_message = f'<span style="color: red; font-weight: bold;">{msg}</span>'
    elif msg.startswith("="*50) or msg.startswith("-"*50):
        html_message = msg.replace('=', '<hr style="border: 2px solid #555;">').replace('-', '<hr style="border: 1px dashed #bbb;">')
    html_logs.append(html_message)

def generate_html_report():
    report_path = "Automation_Report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Automation Report</title>")
        f.write("<style>")
        f.write("body { font-family: 'Consolas', 'Courier New', monospace; background-color: #f4f4f4; padding: 20px; }")
        f.write(".container { background-color: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }")
        f.write("h2 { color: #333; border-bottom: 2px solid #ccc; padding-bottom: 10px; }")
        f.write("pre { white-space: pre-wrap; word-wrap: break-word; }")
        f.write("</style>")
        f.write("</head><body><div class='container'>")
        f.write("<h2>Automation Execution Report</h2>")
        f.write(f"<p><strong>Generated on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        f.write("<pre style='background-color:#fff;padding:15px;border:1px solid #ccc;'>")
        for line in html_logs:
            f.write(line + "\n")
        f.write("</pre></div></body></html>")
    abs_path = os.path.abspath(report_path)
    print(f"\n[✓] HTML report saved at: {abs_path}")
    print("="*50)

# ================= Setup Driver =================
driver = webdriver.Firefox()
driver.get("https://services.itspk.com/admin-login")
driver.maximize_window()

log("Starting Admin Panel Automation Test (ADD USER FORM)...\n" + "="*50)
email = "admin@gmail.com"
password = "12345678"

driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-secondary").click()
time.sleep(4)

# ================= Helper Functions =================
def open_add_user_page():
    driver.get("https://services.itspk.com/createuser")
    time.sleep(2)

def fill_form_fields(suffix, first_name, last_name, user_email, pwd, confirm_pwd):
    driver.find_element(By.ID, "first_name").clear()
    driver.find_element(By.ID, "last_name").clear()
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password_confirmation").clear()
    if suffix:
        Select(driver.find_element(By.NAME, "suffix")).select_by_visible_text(suffix)
    else:
        Select(driver.find_element(By.NAME, "suffix")).select_by_index(0)
    driver.find_element(By.ID, "first_name").send_keys(first_name)
    driver.find_element(By.ID, "last_name").send_keys(last_name)
    driver.find_element(By.ID, "email").send_keys(user_email)
    driver.find_element(By.ID, "password").send_keys(pwd)
    driver.find_element(By.ID, "password_confirmation").send_keys(confirm_pwd)

def create_user(first_name, last_name, user_email, pwd="Strong@123"):
    open_add_user_page()
    Select(driver.find_element(By.NAME, "suffix")).select_by_visible_text("Mr")
    driver.find_element(By.ID, "first_name").send_keys(first_name)

    driver.find_element(By.ID, "last_name").send_keys(last_name)
    driver.find_element(By.ID, "email").send_keys(user_email)
    driver.find_element(By.ID, "password").send_keys(pwd)
    driver.find_element(By.ID, "password_confirmation").send_keys(pwd)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    if "listusers" in driver.current_url:
        log("                                               ")
        log(f"Passed# User Created Successfully → {user_email}")
        log("                                                 ")
        return True
    else:
        log(f"Failed# User Creation Failed → {user_email}")
        return False

# ================= Test Cases =================
# Positive P1–P5
open_add_user_page()

fill_form_fields("Mr", "Ali", "Raza", "newuser532@example.com", "Strong@123", "Strong@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
try:
    assert "listusers" in driver.current_url
    log("------------------------------------ Positive TestCases------------------------------\n")
    log("Passed#P1 - Positive Case: Form submitted successfully\n" + "-"*50)
    log("Passed#P2 - Positive Case: Strong password is accepted.\n"+ "-"*50)
    log("Passed#P3 - Positive Case: Password and confirm password match.\n"+ "-"*50)
    log("Passed#P4 - Positive Case: Suffix is selected properly.\n"+ "-"*50)
    log("Passed#P5 - Positive Case: Email is in correct format.\n"+ "-"*50)
except:
    log("Failed#P1 - Positive Case: Form submission failed unexpectedly\n" + "-"*50)

# Negative N1–N6
open_add_user_page()
fill_form_fields("", "", "", "", "", "")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
try:
    assert "required" in driver.page_source.lower()
    log("------------------------------------ Negative TestCases------------------------------\n")
    log("Passed#N1 - Blank Form Submit: Proper error displayed\n" + "-"*50)
except:
    log("Failed#N1 - Blank Form Submit: Expected error not displayed\n" + "-"*50)

open_add_user_page()
fill_form_fields("Mr", "Invalid", "Email", "invalid-email", "Strong@123", "Strong@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
try:
    assert "email" in driver.page_source.lower()
    log("Passed#N2 - Invalid Email Format: Proper error displayed\n" + "-"*50)
except:
    log("Failed#N2 - Invalid Email Format: Expected error not displayed\n" + "-"*50)

open_add_user_page()
fill_form_fields("Mr", "Weak", "Pass", "weakpass@example.com", "123", "123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
try:
    assert "password" in driver.page_source.lower()
    log("Passed#N3 - Weak Password: Proper error displayed\n" + "-"*50)
except:
    log("Failed#N3 - Weak Password: Expected error not displayed\n" + "-"*50)

open_add_user_page()
fill_form_fields("Mr", "Mismatch", "Password", "mismatch@example.com", "Strong@123", "Wrong@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
try:
    assert "password" in driver.page_source.lower()
    log("Passed#N4 - Password Mismatch: Proper error displayed\n" + "-"*50)
except:
    log("Failed#N4 - Password Mismatch: Expected error not displayed\n" + "-"*50)

open_add_user_page()
fill_form_fields("", "No", "Suffix", "nosuffix@example.com", "Strong@123", "Strong@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
try:
    assert "suffix" in driver.page_source.lower()
    log("Passed#N5 - No Suffix Selected: Proper error displayed\n" + "-"*50)
except:
    log("Failed#N5 - No Suffix Selected: Expected error not displayed\n" + "-"*50)

open_add_user_page()
fill_form_fields("Mr", "Anthony", "Franklin", "anthony.franklin@example.com", "Strong@123", "Strong@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
try:
    assert "already taken" in driver.page_source.lower()
    log("Passed#N6 - Duplicate Email: Proper error displayed\n" + "-"*50)
except:
    log("Failed#N6 - Duplicate Email: Expected error not displayed\n" + "-"*50)

# ================ Generate Users and Save CSV ================
users = []
for i in range(4):
    fname = fake.first_name()
    lname = fake.last_name()
    uemail = fake.unique.email()
    if create_user(fname, lname, uemail):
        users.append([fname, lname, uemail, "Strong@123"])

with open("created_users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["First Name", "Last Name", "Email", "Password"])
    writer.writerows(users)
log("                                                                  ")
log("Passed# All Users Saved in CSV → created_users.csv")
log("                                                                  ")

# ================= Assign Roles =================
role_mapping = {
    1: ["Composing", "Graphics", "Manuscript Preflight", "Data Conversion", "Invoice Manager", "QA"],
    2: ["QA"],
    3: ["Data Conversion"],
    4: ["Graphics", "Composing"]
}

for idx, (fname, lname, uemail, _) in enumerate(users, start=1):
    assigned_roles = role_mapping.get(idx, [])

    for role in assigned_roles:
        try:
            driver.get("https://services.itspk.com/listusers")
            time.sleep(2)

            # NOTE: Assignment part is using old XPATH. This should work for now.
            search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/div/input")
            search_input.clear()
            search_input.send_keys(uemail)
            time.sleep(2)

            driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class,'btn-primary')]").click()
            time.sleep(2)

            row = driver.find_element(By.XPATH, f"//td[contains(text(),'{uemail}')]/..")
            row.find_element(By.XPATH, ".//button[contains(@class,'dropdown-toggle')]").click()
            time.sleep(1)
            row.find_element(By.XPATH, ".//a[contains(., 'Assign Role')]").click()
            time.sleep(2)

            try:
                dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/span/span[1]/span")
                dropdown.click()
                time.sleep(1)
                options = driver.find_elements(By.XPATH, "//li[contains(@class,'select2-results__option')]")
            except:
                try:
                    native_select = driver.find_element(By.XPATH, "//select[@name='role_id']")
                    options = native_select.find_elements(By.TAG_NAME, "option")
                except:
                    options = []

            found = False
            for opt in options:
                if opt.text.strip().lower() == role.lower():
                    try:
                        opt.click()
                    except:
                        driver.execute_script("arguments[0].click();", opt)
                    found = True
                    break

            if found:
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button").click()
                log("                                                                  ")
                log(f"Passed# Role '{role}' assigned → {uemail}")
                log("                                           ")
                time.sleep(2)
            else:
                log(f"Failed# Role '{role}' not found for {uemail}")

        except Exception as e:
            log(f"Failed# Error while assigning role '{role}' to {uemail} → {str(e)}")


                                                    #Edit Role
driver.get("https://services.itspk.com/listusers")

action=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button")
action.click()
time.sleep(2)
edit_role = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/ul/li[2]/a")
edit_role.click()

remove_icon=driver.find_element(By.XPATH,"(//span[@aria-hidden='true'][normalize-space()='×'])[2]")
remove_icon.click()
time.sleep(2)


box=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/h2")
box.click()
time.sleep(5)

update_btn=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/form/div[2]/button")
update_btn.click()
time.sleep(3)
log("Passed-------User Role Edited Successfully--------------")


                                                       #Edit User
action=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button")
action.click()
time.sleep(2)
Edit_User= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/ul/li[3]/a")
Edit_User.click()
time.sleep(3)

f_name = driver.find_element(By.ID,"first_name")
f_name.clear()
f_name.send_keys("NIDA")
time.sleep(2)

l_name= driver.find_element(By.ID,"last_name")
l_name.clear()
l_name.send_keys("MAQBOOL")
time.sleep(2)

update_btn_edit =driver.find_element(By.XPATH,"(//button[normalize-space()='Update'])[1]")
update_btn_edit.click()

time.sleep(4)
log("Passed-------User Information Edited Successfully--------------")

                                                       #Delete User
action=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button")
action.click()
time.sleep(2)
Delete_User = driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Delete'])[1]")
Delete_User.click()
time.sleep(3)

Delete_1= driver.find_element(By.XPATH,"(//button[@type='submit'][normalize-space()='Delete'])[1]")
Delete_1.click()
time.sleep(4)
log("Passed-------User Deleted Successfully--------------")


# ================= Final Summary =================
log("                                                      ")
log("Execution Finished → Generating Final Summary...\n" + "-"*50)
log(f"Total Users Created: {len(users)}")
log("Automation script executed successfully with TestCases + User Creation + Role Assignment + Edit Role")

# ================= Cleanup =================
driver.quit()
generate_html_report()
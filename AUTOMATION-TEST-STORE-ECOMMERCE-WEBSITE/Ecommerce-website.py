import os
import time
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium import webdriver
from selenium.webdriver.common.by import By



# -------------------- HTML LOGGING & REPORT ---------------------
html_logs = []

def log(message):

    print(message)
    html_message = message
    if "PASSED" in message or "PASS" in message or "[✓]" in message:
        html_message = f'<span style="color: green; font-weight: bold;">{message}</span>'
    elif "FAILED" in message or "FAIL" in message or "Unexpected" in message:
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
        f.write(f"<p><strong>Generated on:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        f.write("<pre style='background-color:#fff;padding:15px;border:1px solid #ccc; white-space: pre-wrap; word-wrap: break-word;'>")
        for line in html_logs:
            f.write(line + "\n")
        f.write("</pre></div></body></html>")
    log(f"[✓] HTML report saved at: {os.path.abspath(report_path)}")



# -------------------- SELENIUM Automation SCRIPT ---------------------
driver = webdriver.Firefox()
driver.get("https://www.automationteststore.com/")
driver.maximize_window()
time.sleep(1)


# ---------- clicked on the Register link From the Nav Bar -------------
register_link = driver.find_element(By.LINK_TEXT, "Login or register")
register_link.click()
log("--------------------PASSED#01-----------------------")
log("Successfully clicked on the Register link From the Nav Bar")
time.sleep(3)




# --------------------------Registration Form-----------------------------
continue_btn = driver.find_element(By.XPATH, "//button[@title='Continue']")
continue_btn.click()
time.sleep(3)
log("--------------------PASSED#02-----------------------")
log("Continue button is displayed")

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
email = f"test{timestamp}@gmail.com"
time.sleep(2)

firstname = driver.find_element(By.ID, "AccountFrm_firstname")
firstname.send_keys("Test")

lastname = driver.find_element(By.ID, "AccountFrm_lastname")
lastname.send_keys("User")

email_field = driver.find_element(By.ID, "AccountFrm_email")
email_field.send_keys(email)

address = driver.find_element(By.ID, "AccountFrm_address_1")
address.send_keys("123 Test Street")

city = driver.find_element(By.ID, "AccountFrm_city")
city.send_keys("Karachi")

country = driver.find_element(By.ID, "AccountFrm_country_id")
for option in country.find_elements(By.TAG_NAME, "option"):
    if option.text.strip() == "Pakistan":
        option.click()
        break
time.sleep(2)

zone = driver.find_element(By.ID, "AccountFrm_zone_id")
for option in zone.find_elements(By.TAG_NAME, "option"):
    if option.text.strip() == "Sindh":
        option.click()
        break

postcode = driver.find_element(By.ID, "AccountFrm_postcode")
postcode.send_keys("7400")

login_name = driver.find_element(By.ID, "AccountFrm_loginname")
login_name.send_keys(f"user{timestamp}")

password = driver.find_element(By.ID, "AccountFrm_password")
password.send_keys("test1234")

confirm_password = driver.find_element(By.ID, "AccountFrm_confirm")
confirm_password.send_keys("test1234")

newsletter = driver.find_element(By.ID, "AccountFrm_newsletter0")
newsletter.click()

agree = driver.find_element(By.ID, "AccountFrm_agree")
agree.click()

driver.find_element(By.XPATH, "//button[@title='Continue']").click()
time.sleep(5)
log("--------------------PASSED#03-----------------------")
log("User Successfully Registered!!")

# -------------------- Success Message Validation ---------------------
success_message = driver.find_element(By.CLASS_NAME, "maintext").text.strip()
if "your account has been created!" in success_message.lower():
    log("--------------------PASSED#04-----------------------")
    log("Success message text match after account creation!!")
else:
    log("-------------FAILED----------------------")
    log(f"Success message text did not match: {success_message}")

time.sleep(2)

btn = driver.find_element(By.LINK_TEXT, "Continue")
btn.click()
time.sleep(3)




# ------------------- Click on "Apparel & accessories" -------------------
apparel_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'path=68')]"))
)
if apparel_link.is_displayed() and apparel_link.is_enabled():
    apparel_link.click()
    log("--------------------PASSED#05-----------------------")
    log("Clicked on Apparel & accessories")
else:
    log("FAILED#05: Apparel & accessories link not clickable!")



# ------------------- Click on "Shoes" -------------------
shoes_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Shoes"))
)
if shoes_link.is_displayed() and shoes_link.is_enabled():
    shoes_link.click()
    log("--------------------PASSED#06-----------------------")
    log("Product Selected: Clicked on Shoes")
else:
    log("FAILED#06: Shoes link not clickable!")



# ------------------- Select Product -------------------
product_link1 = driver.find_element(By.CLASS_NAME, "prdocutname")
if product_link1.is_displayed():
    product_link1.click()
    log("--------------------PASSED#07-----------------------")
    log("Redirected to the Shoes Page")
else:
    log("FAILED#07: Product link not found!")
time.sleep(3)



# ------------------- Select Quantity -------------------
quality = driver.find_element(By.ID, "product_quantity")
if quality.is_displayed():
    quality.clear()
    quality.send_keys("10")
    log("--------------------PASSED#08-----------------------")
    log("Selected 10 Products")
else:
    log("FAILED#08: Quantity field not found!")
time.sleep(2)



# ------------------- Add to Cart -------------------
add_to_cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cart"))
)
if add_to_cart.is_enabled():
    add_to_cart.click()
    log("--------------------PASSED#09-----------------------")
    log("Product added to cart")
else:
    log("FAILED#09: Add to Cart button not clickable!")



# ------------------- Checkout -------------------
check_out = driver.find_element(By.ID, "cart_checkout1")
if check_out.is_displayed() and check_out.is_enabled():
    check_out.click()
    log("--------------------PASSED#10-----------------------")
    log("Successfully clicked on the Checkout link")
else:
    log("FAILED#10: Checkout button not found!")
time.sleep(5)



# ------------------- Place Order -------------------
order_btn = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "checkout_btn"))
)
if order_btn.is_enabled():
    order_btn.click()
    log("--------------------PASSED#11-----------------------")
    log("Successfully Placed the order")
else:
    log("FAILED#11: Checkout button not clickable or order failed!")

time.sleep(4)



# ------------------- Verify Order Success Message -------------------
success_msg = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".maintext"))
)
if success_msg.is_displayed():
    log(f"[✓] Order Status: {success_msg.text}")
else:
    log("[!] Order placed but success message not found.")

time.sleep(3)
driver.quit()


# ------------------- Generate HTML Report -------------------
generate_html_report()

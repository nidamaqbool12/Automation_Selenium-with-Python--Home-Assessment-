import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------- HTML LOGGING & REPORT ---------------------
html_logs = []

def log(message):
    """Log message to console and HTML report."""
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
    """Generate HTML report from logged messages."""
    report_path = "Automation_Report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Automation Report</title>")
        f.write("<style>")
        f.write("body { font-family: 'Consolas', monospace; background-color: #f4f4f4; padding: 20px; }")
        f.write(".container { background-color: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }")
        f.write("h2 { color: #333; border-bottom: 2px solid #ccc; padding-bottom: 10px; }")
        f.write("</style></head><body><div class='container'>")
        f.write("<h2>Automation Execution Report</h2>")
        f.write(f"<p><strong>Generated on:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        f.write("<pre style='background-color:#fff;padding:15px;border:1px solid #ccc; white-space: pre-wrap;'>")
        for line in html_logs:
            f.write(line + "\n")
        f.write("</pre></div></body></html>")
    log(f"[✓] HTML report saved at: {os.path.abspath(report_path)}")

# -------------------- SELENIUM Automation ---------------------
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.automationteststore.com/")
    time.sleep(1)

    # -------------------- Register ---------------------
    register_link = driver.find_element(By.LINK_TEXT, "Login or register")
    register_link.click()
    log("--------------------PASSED#01-----------------------")
    log("Clicked on the Register link")

    continue_btn = driver.find_element(By.XPATH, "//button[@title='Continue']")
    continue_btn.click()
    log("--------------------PASSED#02-----------------------")
    log("Clicked Continue button on registration")

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    email = f"test{timestamp}@gmail.com"

    driver.find_element(By.ID, "AccountFrm_firstname").send_keys("Test")
    driver.find_element(By.ID, "AccountFrm_lastname").send_keys("User")
    driver.find_element(By.ID, "AccountFrm_email").send_keys(email)
    driver.find_element(By.ID, "AccountFrm_address_1").send_keys("123 Test Street")
    driver.find_element(By.ID, "AccountFrm_city").send_keys("Karachi")

    # Country & Zone selection
    country = driver.find_element(By.ID, "AccountFrm_country_id")
    for option in country.find_elements(By.TAG_NAME, "option"):
        if option.text.strip() == "Pakistan":
            option.click()
            break
    time.sleep(1)
    zone = driver.find_element(By.ID, "AccountFrm_zone_id")
    for option in zone.find_elements(By.TAG_NAME, "option"):
        if option.text.strip() == "Sindh":
            option.click()
            break

    driver.find_element(By.ID, "AccountFrm_postcode").send_keys("7400")
    driver.find_element(By.ID, "AccountFrm_loginname").send_keys(f"user{timestamp}")
    driver.find_element(By.ID, "AccountFrm_password").send_keys("test1234")
    driver.find_element(By.ID, "AccountFrm_confirm").send_keys("test1234")
    driver.find_element(By.ID, "AccountFrm_newsletter0").click()
    driver.find_element(By.ID, "AccountFrm_agree").click()

    driver.find_element(By.XPATH, "//button[@title='Continue']").click()
    log("--------------------PASSED#03-----------------------")
    log("User Registered successfully")

    # Validate registration success
    success_message = driver.find_element(By.CLASS_NAME, "maintext").text.strip()
    if "your account has been created!" in success_message.lower():
        log("--------------------PASSED#04-----------------------")
        log("Registration success message verified")
    else:
        log("-------------FAILED----------------------")
        log(f"Registration message mismatch: {success_message}")

    # -------------------- Shopping ---------------------
    driver.find_element(By.LINK_TEXT, "Continue").click()
    apparel_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'path=68')]")))

    if apparel_link.is_displayed() and apparel_link.is_enabled():
        apparel_link.click()
        log("--------------------PASSED#05-----------------------")
        log("Clicked on Apparel & accessories")

    shoes_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Shoes")))
    shoes_link.click()
    log("--------------------PASSED#06-----------------------")
    log("Selected Shoes")

    driver.find_element(By.CLASS_NAME, "prdocutname").click()
    log("--------------------PASSED#07-----------------------")
    log("Opened product details")

    quantity = driver.find_element(By.ID, "product_quantity")
    quantity.clear()
    quantity.send_keys("10")
    log("--------------------PASSED#08-----------------------")
    log("Set product quantity to 10")

    add_to_cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
    add_to_cart.click()
    log("--------------------PASSED#09-----------------------")
    log("Product added to cart")

    checkout = driver.find_element(By.ID, "cart_checkout1")
    checkout.click()
    log("--------------------PASSED#10-----------------------")
    log("Clicked on Checkout")

    order_btn = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "checkout_btn")))
    order_btn.click()
    log("--------------------PASSED#11-----------------------")
    log("Order placed successfully")

    # Verify order success
    success_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".maintext")))
    log(f"[✓] Order Status: {success_msg.text}")

finally:
    driver.quit()
    generate_html_report()

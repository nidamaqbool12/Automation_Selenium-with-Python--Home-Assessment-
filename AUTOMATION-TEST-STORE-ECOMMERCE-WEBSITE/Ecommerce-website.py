import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

# -------------------- HTML LOGGING & REPORT ---------------------
html_logs = []

def log(message):
    print(message)
    html_message = message

    if "PASSED" in message or "PASS" in message or "[✓]" in message:
        html_message = f'<span style="color: green; font-weight: bold;">{message}</span>'
    elif "FAILED" in message or "FAIL" in message or "Unexpected" in message:
        html_message = f'<span style="color: red; font-weight: bold;">{message}</span>'
    elif message.startswith("=" * 20):
        html_message = "<hr style='border:1px dashed #bbb;'>"

    html_logs.append(html_message)

def generate_html_report():
    report_path = "Automation_Report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("""
        <html><head><title>Automation Report</title>
        <style>
            body {font-family:Consolas;background:#f4f4f4;padding:20px;}
            .container {background:#fff;padding:25px;border-radius:8px;}
        </style></head>
        <body><div class='container'>
        <h2>Automation Execution Report</h2>
        """)
        f.write(f"<p>Generated on: {datetime.datetime.now()}</p><pre>")
        for line in html_logs:
            f.write(line + "\n")
        f.write("</pre></div></body></html>")
    print(f"[✓] HTML Report Generated: {os.path.abspath(report_path)}")

# -------------------- SELENIUM SETUP ---------------------
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://www.automationteststore.com/")
    time.sleep(3) # Initial hard wait for CI stability

    # -------------------- REGISTER ---------------------
    register_link_xpath = "//a[normalize-space()='Login or register']"
    
    # ULTIMATE FIX 1: Use JavaScript to force the click (for initial link)
    register_link = wait.until(
        EC.presence_of_element_located((By.XPATH, register_link_xpath))
    )
    driver.execute_script("arguments[0].click();", register_link) # FORCED CLICK

    log("==================== PASSED #01 ====================")
    log("Clicked Login or Register via JavaScript Executor")

    # Click Continue on Registration page
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@title='Continue']"))
    ).click()

    log("==================== PASSED #02 ====================")
    log("Clicked Continue on Registration")

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    email = f"test{timestamp}@gmail.com"

    # Fill form data
    driver.find_element(By.ID, "AccountFrm_firstname").send_keys("Test")
    driver.find_element(By.ID, "AccountFrm_lastname").send_keys("User")
    driver.find_element(By.ID, "AccountFrm_email").send_keys(email)
    driver.find_element(By.ID, "AccountFrm_address_1").send_keys("123 Test Street")
    driver.find_element(By.ID, "AccountFrm_city").send_keys("Karachi")

    # Country Selection
    country = driver.find_element(By.ID, "AccountFrm_country_id")
    for opt in country.find_elements(By.TAG_NAME, "option"):
        if opt.text.strip() == "Pakistan":
            opt.click()
            break

    time.sleep(1) # Small wait for Zone dropdown to populate

    # Zone Selection
    zone = driver.find_element(By.ID, "AccountFrm_zone_id")
    for opt in zone.find_elements(By.TAG_NAME, "option"):
        if opt.text.strip() == "Sindh":
            opt.click()
            break

    driver.find_element(By.ID, "AccountFrm_postcode").send_keys("74000")
    driver.find_element(By.ID, "AccountFrm_loginname").send_keys(f"user{timestamp}")
    driver.find_element(By.ID, "AccountFrm_password").send_keys("test1234")
    driver.find_element(By.ID, "AccountFrm_confirm").send_keys("test1234")
    driver.find_element(By.ID, "AccountFrm_newsletter0").click()
    driver.find_element(By.ID, "AccountFrm_agree").click()

    # Submit final form
    driver.find_element(By.XPATH, "//button[@title='Continue']").click()

    # FIX: Wait explicitly for the success message element after submission
    success_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "maintext")))
    success_text = success_element.text.lower()

    if "your account has been created" in success_text:
        log("==================== PASSED #03 ====================")
        log("Registration Successful")
    else:
        log("==================== FAILED ====================")
        log(f"Registration Failed. Expected success message, but found: {success_text}")


    # -------------------- SHOPPING ---------------------
    driver.find_element(By.LINK_TEXT, "Continue").click()

    # Wait for Apparel link
    apparel_xpath = "//a[contains(@href,'path=68')]"
    
    # ULTIMATE FIX 2: Use JavaScript to force the click on the Apparel link
    apparel = wait.until(EC.presence_of_element_located((By.XPATH, apparel_xpath)))
    driver.execute_script("arguments[0].click();", apparel) # FORCED CLICK

    log("==================== PASSED #04 ====================")
    log("Clicked Apparel & Accessories via JavaScript Executor")

    # Wait for Shoes link
    shoes = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Shoes")))
    if shoes.is_displayed():
        shoes.click()
        log("==================== PASSED #05 ====================")
        log("Shoes selected")
    else:
        log("==================== FAILED ====================")
        log("Shoes not visible")

    # Wait for product to click
    product = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "prdocutname")))
    if product.is_displayed():
        product.click()
        log("==================== PASSED #06 ====================")
        log("Product opened")
    else:
        log("==================== FAILED ====================")
        log("Product not opened")

    # Set quantity
    qty = driver.find_element(By.ID, "product_quantity")
    if qty.is_enabled():
        qty.clear()
        qty.send_keys("10")
        log("==================== PASSED #07 ====================")
        log("Quantity set to 10")
    else:
        log("==================== FAILED ====================")
        log("Quantity field disabled")

    # Add to cart
    add_cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
    if add_cart.is_enabled():
        add_cart.click()
        log("==================== PASSED #08 ====================")
        log("Added to cart")
    else:
        log("==================== FAILED ====================")
        log("Add to cart failed")

    # Checkout
    checkout = driver.find_element(By.ID, "cart_checkout1")
    if checkout.is_displayed():
        checkout.click()
        log("==================== PASSED #09 ====================")
        log("Checkout clicked")
    else:
        log("==================== FAILED ====================")
        log("Checkout button missing")

    # Place Order
    order_btn = wait.until(EC.presence_of_element_located((By.ID, "checkout_btn")))
    if order_btn.is_enabled():
        order_btn.click()
        log("==================== PASSED #10 ====================")
        log("Order placed")
    else:
        log("==================== FAILED ====================")
        log("Order button disabled")

    # Verify Order Success
    # FIX: Wait for the final order success message
    order_success_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "maintext")))
    order_msg = order_success_element.text.lower()

    if "your order has been processed" in order_msg:
        log("==================== PASSED #11 ====================")
        log("Order success message verified")
    else:
        log("==================== FAILED ====================")
        log(f"Order confirmation missing. Actual message: {order_msg}")

except Exception as e:
    log("==================== FAILED ====================")
    log(f"An unexpected error occurred: {type(e).__name__}: {str(e)}")

finally:
    driver.quit()
    generate_html_report()

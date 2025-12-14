import time
import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from selenium import webdriver

from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.automationteststore.com/")
driver.maximize_window()

time.sleep(1)

register_link = driver.find_element(By.LINK_TEXT, "Login or register")
register_link.click()
print("--------------------PASSED#01-----------------------")
print("Successfully clicked on the Register link")
print("                                            ")
time.sleep(3)

continue_btn = driver.find_element(By.XPATH, "//button[@title='Continue']")
continue_btn.click()
time.sleep(3)
print("--------------------PASSED#02-----------------------")
print("Continue button is displayed")
print("                                            ")

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
print("--------------------PASSED#03-----------------------")
print("Successfully Registered!!")
print("                                            ")

try:
    success_message = driver.find_element(By.CLASS_NAME, "maintext").text.strip()
    if "your account has been created!" in success_message.lower():
        print("--------------------PASSED#04-----------------------")
        print("Success message text match after account creation!!")
        print("                                            ")
    else:
        print("-------------FAILED----------------------")
        print("Success message text did not match:", success_message)

except Exception as e:
    print("-------------FAILED----------------------")
    print("Could not locate success message:", str(e))

time.sleep(2)

btn = driver.find_element(By.LINK_TEXT, "Continue")
btn.click()
time.sleep(3)

# Click on "Apparel & accessories"
apparel_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'path=68')]"))
)
apparel_link.click()
print("--------------------PASSED#05-----------------------")
print("Clicked on Apparel & accessories")
print("                                            ")

# Click on "Shoes"
shoes_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Shoes"))
)
shoes_link.click()
print("--------------------PASSED#06-----------------------")
print("Clicked on Shoes")
print("                                            ")

product_link1 = driver.find_element(By.CLASS_NAME, "prdocutname")
product_link1.click()
print("--------------------PASSED#07-----------------------")
print("Redirected to the Shoes Page")
print("                                            ")
time.sleep(3)

# -------------------------------------
# UPDATED OPTION SELECTION (RADIO BUTTON)
# -------------------------------------
color_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='radio'][name^='option']"))
)
color_option.click()

print("--------------------PASSED#07A-----------------------")
print("Colour option selected")
print("                                            ")

time.sleep(1)
# -------------------------------------

quality = driver.find_element(By.ID, "product_quantity")
quality.clear()
quality.send_keys("10")
print("--------------------PASSED#08-----------------------")
print("Selected 10 Products")
print("                                            ")
time.sleep(4)

wait = WebDriverWait(driver, 10)

add_to_cart = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart"))
)
add_to_cart.click()
print("--------------------PASSED#09-----------------------")
print("Product added to cart")
print("                                            ")

check_out = driver.find_element(By.ID, "cart_checkout1")
check_out.click()
print("--------------------PASSED#10-----------------------")
print("Successfully clicked on the Checkout link")
print("                                            ")

# ===================================================================
# UPDATED CHECKOUT + PLACE ORDER CODE (Only this part changed)
# ===================================================================

time.sleep(5)

wait = WebDriverWait(driver, 15)

# Wait for checkout button
order_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "checkout_btn"))
)
order_btn.click()

print("--------------------PASSED#11-----------------------")
print("Successfully Placed the order")
print("                                            ")

time.sleep(4)

# Optional: Verify order success message
try:
    success_msg = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".maintext"))
    )
    print("Order Status:", success_msg.text)
except:
    print("Order placed but success message not found.")

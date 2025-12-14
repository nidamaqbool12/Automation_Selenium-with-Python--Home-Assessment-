from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# WebDriver setup (Chrome)
driver = webdriver.Chrome()

try:
    # Website ka Create Account page open karo
    driver.get("https://automationteststore.com/index.php?rt=account/create")

    # Thoda wait karo jab tak page load ho jaye
    time.sleep(2)

    # Form fields fill karo
    driver.find_element(By.NAME, "firstname").send_keys("Ali")
    driver.find_element(By.NAME, "lastname").send_keys("Khan")
    driver.find_element(By.NAME, "email").send_keys("alikhan123@example.com")
    driver.find_element(By.NAME, "telephone").send_keys("03001234567")

    driver.find_element(By.NAME, "company").send_keys("My Company")
    driver.find_element(By.NAME, "address_1").send_keys("123 Street")
    driver.find_element(By.NAME, "address_2").send_keys("Suite 4")
    driver.find_element(By.NAME, "city").send_keys("Lahore")

    # Country dropdown select karna
    country = Select(driver.find_element(By.NAME, "country_id"))
    country.select_by_visible_text("Pakistan")

    # Region / State dropdown
    time.sleep(1)  # state list load hone mein thora waqt
    state = Select(driver.find_element(By.NAME, "zone_id"))
    state.select_by_visible_text("Punjab")

    driver.find_element(By.NAME, "postcode").send_keys("54000")

    # Login / account credentials
    driver.find_element(By.NAME, "loginname").send_keys("alikhan123")
    driver.find_element(By.NAME, "password").send_keys("MySecureP@ss1")
    driver.find_element(By.NAME, "confirm").send_keys("MySecureP@ss1")

    # Newsletter option (Yes ya No): yahan No choose kia hai
    driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='0']").click()

    # Privacy policy ko accept karo
    driver.find_element(By.NAME, "agree").click()

    # Continue / Submit button
    driver.find_element(By.XPATH, "//button[@title='Continue']").click()

    # Thodi der result dekhne ke liye
    time.sleep(3)

finally:
    driver.quit()

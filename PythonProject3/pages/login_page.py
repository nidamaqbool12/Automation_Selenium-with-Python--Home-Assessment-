from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-block.btn-lg")

    def open_login_page(self):
        self.driver.get("https://conference.itspk.com/")

    def login(self, email, password):
        short_wait = WebDriverWait(self.driver, 3)
        long_wait = WebDriverWait(self.driver, 3)


        try:
            login_link = short_wait.until(EC.element_to_be_clickable(self.LOGIN_LINK))
            login_link.click()
        except:
            print("[INFO] Login link not found or already on login page.")

        # Enter email and password
        short_wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)

        # Click login button
        try:
            login_btn = short_wait.until(EC.element_to_be_clickable(self.LOGIN_BTN))
            login_btn.click()
        except:
            # Sometimes button is covered by overlay; use JS click
            btn = self.driver.find_element(*self.LOGIN_BTN)
            self.driver.execute_script("arguments[0].click();", btn)

        # Verify login success by checking for submission page link
        try:
            long_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href,'abstract-submission-form')]")
            ))
            print(f"[SUCCESS] {email} logged in successfully.")
            return True
        except:
            print(f"[ERROR] {email} failed to log in.")
            return False

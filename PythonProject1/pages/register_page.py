import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    URL = "https://conference.itspk.com/register/1/0"

    # Locators
    EMAIL = (By.XPATH, "//*[@id='auth-left']/div[1]/form/div[1]/div/input")
    FIRST_NAME = (By.XPATH, "//*[@id='auth-left']/div[1]/form/div[2]/div/input")
    LAST_NAME = (By.XPATH, "//*[@id='auth-left']/div[1]/form/div[3]/div/input")
    COMPANY = (By.XPATH, "//input[@placeholder='Company/Instititution Name *']")
    HOME_PHONE = (By.XPATH, "//input[@placeholder='Home Phone ']")
    CELL_PHONE = (By.XPATH, "(//input[@placeholder='Cell Phone *'])[1]")
    ROLE = (By.ID, "roleSelect")
    COUNTRY = (By.NAME, "country")
    CITY = (By.XPATH, "//*[@id='auth-left']/div[1]/form/div[9]/div/input")
    PROVINCE = (By.XPATH, "//*[@id='auth-left']/div[1]/form/div[10]/div/input")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm_password")
    TOGGLE_FIELDS = (By.ID, "toggleFields")
    EXTRA1 = (By.XPATH, "//*[@id='fieldContainer']/div/div/div[1]/div/input")
    EXTRA2 = (By.XPATH, "//*[@id='fieldContainer']/div/div/div[2]/div/input")
    EXTRA3 = (By.XPATH, "//*[@id='fieldContainer']/div/div/div[3]/div/input")
    SUBMIT = (By.XPATH, "//button[normalize-space()='Sign Up']")
    ERRORS = (By.XPATH, "//*[contains(text(),'Please select') or contains(text(),'taken') or contains(@class, 'alert-danger')]")

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, user):
        #Generate unique email with timestamp
        if user.get("email"):
            base_email = user["email"]
            if "@" in base_email:
                name, domain = base_email.split("@")
                unique_email = f"{name}_{int(time.time())}@{domain}"
            else:
                unique_email = f"{base_email}_{int(time.time())}@example.com"

            print(f"[INFO] Using email: {unique_email}")
            self.type(self.EMAIL, unique_email)

        self.type(self.FIRST_NAME, user["first_name"])
        self.type(self.LAST_NAME, user["last_name"])
        self.type(self.COMPANY, user["company"])
        self.type(self.HOME_PHONE, user["home_phone"])
        self.type(self.CELL_PHONE, user["cell_phone"])

        if user.get("registration_type"):
            self.select_by_visible_text(self.ROLE, user["registration_type"])
        if user.get("country"):
            self.select_by_visible_text(self.COUNTRY, user["country"])

        self.type(self.CITY, user["city"])
        self.type(self.PROVINCE, user["province"])
        self.type(self.PASSWORD, user["password"])
        self.type(self.CONFIRM_PASSWORD, user["confirm_password"])

        self.click(self.TOGGLE_FIELDS)
        self.type(self.EXTRA1, user["extra1"])
        self.type(self.EXTRA2, user["extra2"])
        self.type(self.EXTRA3, user["extra3"])

    def submit(self):
        self.click(self.SUBMIT)

    def get_errors(self):
        return [e.text for e in self.driver.find_elements(*self.ERRORS)]

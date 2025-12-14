import pytest
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def _screenshot_name(self, name):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f".\\screenshots\\{name}_{timestamp}.png"

    def _capture_screenshot(self, driver, test_name):
        screenshot_path = self._screenshot_name(test_name)
        driver.save_screenshot(screenshot_path)
        self.logger.error(f"Screenshot captured: {screenshot_path}")

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("*********** Test_01_Admin_Login -> test_title_verification *************")
        driver = setup
        driver.get(self.admin_page_url)

        try:
            WebDriverWait(driver, 10).until(EC.title_is("Your store. Login"))
            assert driver.title == "Your store. Login", \
                f"Title mismatch. Expected: 'Your store. Login', Got: '{driver.title}'"
            self.logger.info("Title matched successfully ✅")
        except AssertionError as e:
            self._capture_screenshot(driver, "test_title_verification")
            raise e

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self, setup):
        self.logger.info("*********** Test_01_Admin_Login -> test_valid_admin_login *************")
        driver = setup
        driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(driver)

        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()

        try:
            dashboard_header = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='content-header']/h1"))
            ).text.strip()

            assert dashboard_header == "Dashboard", \
                f"Dashboard header mismatch. Expected: 'Dashboard', Got: '{dashboard_header}'"
            self.logger.info("Dashboard text matched successfully ")
        except AssertionError as e:
            self._capture_screenshot(driver, "test_valid_admin_login")
            raise e

    @pytest.mark.regression
    def test_invalid_admin_login(self, setup):
        self.logger.info("*********** Test_01_Admin_Login -> test_invalid_admin_login *************")
        driver = setup
        driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(driver)

        admin_lp.enter_username(self.invalid_username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()

        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//li"))
            ).text

            assert "No customer account found" in error_message, \
                f"Error message mismatch. Got: '{error_message}'"
            self.logger.info("Invalid login error message matched successfully ")
        except AssertionError as e:
            self._capture_screenshot(driver, "test_invalid_admin_login")
            raise e

import this

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def select_by_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_visible_text(text)


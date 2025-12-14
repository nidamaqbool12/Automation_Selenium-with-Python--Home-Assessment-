from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        self.driver.execute_script("arguments[0].click();", el)

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def select_by_visible_text(self, locator, text):
        from selenium.webdriver.support.ui import Select
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        Select(el).select_by_visible_text(text)

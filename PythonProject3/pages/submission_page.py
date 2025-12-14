import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class SubmissionPage(BasePage):
    SUBMISSION_LINK = (By.XPATH, "//a[contains(@href, 'abstract-submission-form') and .//span[text()='New Submission']]")
    MAIN_TRACK_SELECT = (By.ID, "mainTrackSelect")
    SUB_TRACK_SELECT = (By.ID, "childTrackSelect")
    TITLE_INPUT = (By.NAME, "title")
    ABSTRACT_INPUT = (By.NAME, "abstract")
    KEYWORDS_INPUT = (By.XPATH, "//div[@class='bootstrap-tagsinput col-md-12']//input[@placeholder='Press enter to insert']")
    REF_CODE_INPUT = (By.ID, "reference_number")
    SUBMIT_BTN = (By.ID, "submit-btn")

    def open_submission_form(self):
        self.click(self.SUBMISSION_LINK)

    def fill_submission_form(self, main_track, sub_track, title, abstract, keywords, ref_code):
        self.select_by_text(self.MAIN_TRACK_SELECT, main_track)
        self.select_by_text(self.SUB_TRACK_SELECT, sub_track)

        # Generate unique title
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        unique_title = f"{title} {timestamp}"
        self.type(self.TITLE_INPUT, unique_title)

        self.type(self.ABSTRACT_INPUT, abstract)

        # Fill keywords
        keyword_input = self.driver.find_element(*self.KEYWORDS_INPUT)
        for kw in keywords.split(","):
            keyword_input.send_keys(kw.strip())
            keyword_input.send_keys(Keys.ENTER)

        self.type(self.REF_CODE_INPUT, ref_code)

        # Print in console
        print(f"\n[INFO] Unique Title Used: {unique_title}")

        # Return so tests can attach it in HTML report
        return unique_title

    def submit(self):
        submit_btn = self.driver.find_element(*self.SUBMIT_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_BTN))
        self.driver.execute_script("arguments[0].click();", submit_btn)

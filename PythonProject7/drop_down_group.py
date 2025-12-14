from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

actions = ActionChains(driver)

# Click dropdown
dropdown = driver.find_element(By.XPATH, "//div[@id='withOptGroup']//div[@class=' css-1hwfws3']")
dropdown.click()
time.sleep(1)

# Type in input box
input_box = driver.find_element(By.XPATH, "//div[@id='withOptGroup']//input")
input_box.send_keys("Group 1")
time.sleep(1)

# Wait and click visible option
option = driver.find_element(By.XPATH, "//div[@id='withOptGroup']//div[contains(text(),'Group 1, option 1')]")

option.click()

# Click outside
actions.move_by_offset(10, 10).click().perform()
time.sleep(1)

driver.quit()

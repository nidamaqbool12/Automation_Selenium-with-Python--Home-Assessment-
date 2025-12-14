import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://admirhodzic.github.io/multiselect-dropdown/demo.html")
driver.maximize_window()

actions = ActionChains(driver)


dropdown = driver.find_element(By.XPATH, "(//div[@class='multiselect-dropdown'])[1]")
dropdown.click()
time.sleep(1)

# check Audi
audi = driver.find_element(By.XPATH, "(//div)[7]")
audi.click()
time.sleep(1)

# Uncheck BMW
bmw = driver.find_element(By.XPATH, "(//div)[8]")
bmw.click()
time.sleep(1)

#checked volvo
volvo = driver.find_element(By.XPATH, "(//div)[10]")
volvo.click()
time.sleep(0.5)
volvo.click()
time.sleep(1)

actions.move_by_offset(10, 10).click().perform()
time.sleep(1)



dropdown_2 = driver.find_element(By.XPATH, "(//div[@class='multiselect-dropdown'])[2]")
dropdown_2.click()
time.sleep(1)

# Enter search text
search = driver.find_element(By.XPATH, "(//input[@placeholder='search'])[2]")
search.send_keys("Ford")
time.sleep(1)
ford_item = driver.find_element(By.XPATH,"(//div[@class='multiselect-dropdown'])[2]//div[@class='multiselect-dropdown-list']/div[not(contains(@style,'display: none'))]")

ford_item.click()
time.sleep(1)
actions.move_by_offset(10, 10).click().perform()




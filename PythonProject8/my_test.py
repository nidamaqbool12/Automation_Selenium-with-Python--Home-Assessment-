import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://ror.org/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# ---------- Search Karachi University ----------
search_uni = wait.until(EC.presence_of_element_located((By.ID, "query")))
search_uni.clear()
search_uni.send_keys("Karachi University")
search_uni.send_keys(Keys.ENTER)

# ---------- Click first result ----------
first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.search-result a")))
first_result.click()

# ---------- Extract GRID ----------
# Wait until the "Other Identifiers" section loads
grid_label = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='GRID']")))

# GRID number is usually in the next sibling text node
grid_text = driver.execute_script("return arguments[0].nextSibling.textContent.trim();", grid_label)

# Extract GRID number
match = re.search(r"(grid\.[\w\.]+)", grid_text, re.IGNORECASE)
grid_number = match.group(1) if match else None

print(f"Karachi University GRID Number: {grid_number}")

# ---------- Save to CSV ----------
data = [{"university": "Karachi University", "grid_number": grid_number}]
df = pd.DataFrame(data)
df.to_csv("karachi_uni_grid.csv", index=False)

driver.quit()
print("\nGRID number saved in karachi_uni_grid.csv")

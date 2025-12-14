from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import time

# ---------- Universities List ----------
universities = [
    "University of Karachi",
    "NED University of Engineering and Technology"
]

# ---------- Setup Driver ----------
driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 20)  # increased wait time

results = []

for uni in universities:
    print(f"\nSearching: {uni}")
    driver.get("https://ror.org/")

    # ---------- Wait for the search input ----------
    try:
        # Sometimes search box is inside iframe
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            driver.switch_to.frame(iframes[0])

        # locate search input by type='search'
        search_box = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        search_box.clear()
        search_box.send_keys(uni)
        search_box.send_keys(Keys.ENTER)

        # Give search results some time to load
        time.sleep(2)

        # ---------- Click First Result ----------
        first_result = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[contains(@class,'search-result')])[1]")
            )
        )
        first_result.click()

        # Switch back to main content if needed
        driver.switch_to.default_content()

        # ---------- Extract GRID Number ----------
        try:
            grid_span = wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='GRID']"))
            )

            grid_text = driver.execute_script("""
                return arguments[0].nextSibling.textContent.trim();
            """, grid_span)

            match = re.search(r"(grid\.[\w\.]+)", grid_text, re.IGNORECASE)
            grid_number = match.group(1) if match else None
            print(f"{uni} GRID Number: {grid_number}")

        except Exception as e:
            grid_number = None
            print(f"{uni} GRID Number not found: {e}")

    except Exception as e:
        grid_number = None
        print(f"{uni} Search failed: {e}")

    # Append results
    results.append({
        "university": uni,
        "grid_number": grid_number
    })

# ---------- Save to CSV ----------
df = pd.DataFrame(results)
df.to_csv("grid_numbers_detail_page.csv", index=False)

print("\nAll done! Results saved in grid_numbers_detail_page.csv")

driver.quit()

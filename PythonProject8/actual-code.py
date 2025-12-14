from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

# ---------- Universities List ----------
universities = [
    "University of Karachi",
    "NED University of Engineering and Technology"
]

# ---------- Setup Driver ----------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

results = []

for uni in universities:
    print(f"\nSearching: {uni}")
    driver.get("https://ror.org/")

    # ----------- Search Box -----------
    search_box = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/section[4]/div/div/div/div[1]/div[2]/form/input")
        )
    )
    search_box.clear()
    search_box.send_keys(uni)
    search_box.send_keys(Keys.ENTER)

    # ----------- Click First Result to go to detail page -----------
    first_result = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div[4]")
        )
    )
    first_result.click()

    # ----------- Extract GRID Number from detail page -----------
    try:
        grid_span = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='GRID']"))
        )
        grid_text = driver.execute_script(
            "return arguments[0].nextSibling.textContent;", grid_span
        ).strip()
        match = re.search(r"grid\.(.+)", grid_text, re.IGNORECASE)
        grid_number = match.group(1) if match else None
        print(f"{uni} GRID Number: {grid_number}")
    except Exception as e:
        grid_number = None
        print(f"{uni} GRID Number not found:", e)

    results.append({
        "university": uni,
        "grid_number": grid_number
    })

# ---------- Save to CSV ----------
df = pd.DataFrame(results)
df.to_csv("grid_numbers_detail_page.csv", index=False)
print("\nAll done! Results saved in grid_numbers_detail_page.csv")

driver.quit()
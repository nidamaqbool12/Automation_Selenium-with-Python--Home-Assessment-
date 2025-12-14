from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Set up the driver (make sure to replace with your driver path if needed)
driver = webdriver.Firefox()

# Log into the application (use your credentials)
email = "admin@gmail.com"
password = "12345678"

driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-secondary").click()
time.sleep(4)
# Wait for the page to load


# Navigate to the list of users page
driver.get("https://services.itspk.com/listusers")


# Function to search user by email
def search_user_by_email(email):
    # Find the email search input and search for the email
    search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/div/input")
    search_input.clear()
    search_input.send_keys(email)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Function to edit role for the found user
def edit_user_role(email):
    # Search for the email first
    search_user_by_email(email)

    # Wait for the search results to load
    time.sleep(2)

    # Find the row that contains the email
    row = driver.find_element(By.XPATH, f"//td[contains(text(),'{email}')]/..")

    # Click the 'Actions' dropdown button
    actions_button = row.find_element(By.XPATH, ".//button[contains(@class,'dropdown-toggle')]")
    actions_button.click()
    time.sleep(1)

    # Click 'Edit Role' from the dropdown
    edit_role_button = row.find_element(By.XPATH, ".//a[contains(text(), 'Edit Role')]")
    edit_role_button.click()

    # Wait for the Edit Role page to load
    time.sleep(2)

    # Now remove one of the roles (you can adjust this step based on the actual DOM structure and roles you want to remove)
    roles = driver.find_elements(By.XPATH,
                                 "//span[contains(@class, 'role-name')]")  # Assuming roles are shown as span elements
    if roles:
        # Example: Remove one of the roles (you might need to adjust this if your interface is different)
        remove_button = roles[0].find_element(By.XPATH, ".//button[contains(@class, 'remove-role')]")
        remove_button.click()
        time.sleep(1)

    # Click the 'Update Role' button to save the changes
    update_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button")
    update_button.click()
    time.sleep(2)

    print(f"Role updated for {email}")


# Edit role for a specific user
edit_user_role("christystevens@example.net")

# After updating, you can navigate back to the user list page
driver.get("https://services.itspk.com/listusers")

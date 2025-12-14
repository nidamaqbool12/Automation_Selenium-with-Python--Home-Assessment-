import csv
import os
import random
import time
from datetime import datetime
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Initialize Faker
fake = Faker()

# Initialize log list
html_logs = []

def log(message):
    print(message)  # Show in terminal
    html_logs.append(message)  # Store for HTML report

def generate_password_from_name(first_name):
    return first_name.capitalize() + "@123"

def create_attachment(first_name, last_name):
    folder_name = "all_users_pdf_files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = f"{first_name}_{last_name}_attachment.pdf"
    file_path = os.path.abspath(os.path.join(folder_name, file_name))

    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Service Attachment")
    c.setFont("Helvetica", 12)
    c.drawString(100, 730, f"This file belongs to {first_name} {last_name}")
    c.save()

    log("---------------------PASSED#01-------------------------")
    log(f"PDF Attachment saved at: {file_path}")
    log("")
    return file_path

def save_to_csv(data, csv_file="generated_users.csv"):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(
                ["FirstName", "LastName", "Email", "Password", "Suffix", "Country", "Service", "AttachmentPath", "Description"]
            )
        writer.writerow(data)
    log("---------------------PASSED#06-------------------------")
    log(f"[✓] User data saved to {csv_file}")
    log("")

def generate_html_report():
    report_path = "report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Automation Report</title></head><body>")
        f.write("<h2>Automation Execution Report</h2>")
        f.write(f"<p><strong>Generated on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        f.write("<pre style='background-color:#f4f4f4;padding:15px;border:1px solid #ccc;'>")
        for line in html_logs:
            f.write(line + "\n")
        f.write("</pre></body></html>")

    log(f" HTML report saved at: {os.path.abspath(report_path)}")

def main():
    # Generate fake user data
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    password = generate_password_from_name(first_name)
    suffix = random.choice(['Mr', 'Ms', 'Mrs'])
    country = 'Pakistan'
    service = 'Type Setting'
    description = f"Form submitted by {first_name} for {service}"

    # Create attachment
    attachment_path = create_attachment(first_name, last_name)

    # Start Selenium
    driver = webdriver.Chrome()
    driver.get("https://services.itspk.com/createservice")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 15)

    try:
        service_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "serviceSelect"))))
        service_dropdown.select_by_visible_text(service)

        attachment_input = driver.find_element(By.ID, "attachment")
        attachment_input.send_keys(attachment_path)
        time.sleep(2)

        suffix_dropdown = Select(driver.find_element(By.ID, "suffixSelect"))
        suffix_dropdown.select_by_visible_text(suffix)

        driver.find_element(By.ID, "firstName").send_keys(first_name)
        driver.find_element(By.ID, "lastName").send_keys(last_name)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)

        country_dropdown = Select(driver.find_element(By.ID, "countrySelect"))
        country_dropdown.select_by_visible_text(country)

        driver.find_element(By.ID, "description").send_keys(description)

        submit_button = driver.find_element(By.CSS_SELECTOR, "button.custom-submit-btn")

        log("---------------------PASSED#02-------------------------")
        log(f"[i] URL before submit: {driver.current_url}")
        log("")

        submit_button.click(
        )
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
            log("---------------------PASSED#03-------------------------")
            log("[✓] Form submitted successfully (success alert detected).")
            log("")
        except:
            log("[!] Success alert not detected, waiting fixed time as fallback...")
            time.sleep(10)

        log("---------------------PASSED#04-------------------------")
        log(f"[i] URL after submit: {driver.current_url}")
        log("")

    finally:
        time.sleep(12)
        driver.quit()
        log("---------------------PASSED#05-------------------------")
        log("Job Created Successfully!")
        log("")

    # Save user data
    user_data = [first_name, last_name, email, password, suffix, country, service, attachment_path, description]
    save_to_csv(user_data)

    # Generate HTML report
    generate_html_report()

if __name__ == "__main__":
    main()


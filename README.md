# Automation_Selenium-with-Python--Home-Assessment-

E-commerce Website End-to-End Test Automation (Selenium-Python)

This repository contains a comprehensive end-to-end automation test suite for the Automation Test Store e-commerce website. The automation is built using Python and Selenium WebDriver, and is integrated with GitHub Actions for CI/CD execution.

The project demonstrates expertise in stable test design, dynamic data handling, robust explicit waits, and continuous integration, simulating a real-world e-commerce user journey.

Project Purpose

This project is designed for home assessment purposes to showcase proficiency in the following areas:

Assessment Requirement	Demonstrated Skills in Project
Test Automation Foundation	Automation using Python and Selenium WebDriver.
Real-world Scenario	Full e-commerce user journey: Registration, Shopping, Checkout.
Stable Test Design	Use of explicit waits (WebDriverWait) to handle dynamic loading.
Robustness	JavaScript Executor used for critical clicks to bypass CI/browser issues.
Dynamic Test Data	Automatic generation of unique timestamped emails and usernames to prevent conflicts.
Validation & Reporting	Assertions on success messages with color-coded HTML test reports.
DevOps/CI Integration	Fully integrated with GitHub Actions CI/CD pipeline.
End-to-End Automation Flow

The Python automation script executes the following complete user journey:

1. Registration

Navigate to the homepage and click “Login or register”.

Create a unique user account using a timestamped email.

Fill out registration details including Country (Pakistan) and Zone (Sindh).

Verify “Account has been created” success message.

2. Shopping Journey

Click “Continue” to return to homepage.

Navigate to Apparel & Accessories → Shoes.

Select a product and go to its detail page.

3. Checkout

Update product quantity to 10.

Add product to cart.

Proceed to checkout using pre-filled registration details.

Place the order.

4. Final Verification

Validate Checkout Confirmation page to ensure order was successfully processed.

Project Setup and Installation

This project can be run locally in PyCharm or any Python environment.

1. Prerequisites

Python 3.8+

Git

Google Chrome installed

PyCharm or any IDE for Python

2. Clone the Repository
git clone [YOUR_GITHUB_REPO_LINK]
cd Automation_Selenium-with-Python--Home-Assessment-

3. Connect GitHub Repository (Optional)
git remote add origin [YOUR_GITHUB_REPO_LINK]
git branch -M main
git push -u origin main

4. Create & Activate Virtual Environment
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate

5. Install Dependencies
pip install selenium

Running the Automation Script
From Terminal
python AUTOMATION-TEST-STORE-ECOMMERCE-WEBSITE/Ecommerce-website.py


The script runs Chrome in headless mode by default for faster execution and CI/CD compatibility.

From PyCharm

Open the project in PyCharm.

Right-click on Ecommerce-website.py.

Click Run 'Ecommerce-website'.

CI/CD Integration (GitHub Actions)

This project uses GitHub Actions for continuous testing.

Workflow Overview

Trigger: Runs on push to main branch.

Environment Setup: Uses Ubuntu Linux runner and installs Python and required dependencies (selenium).

Test Execution: Selenium script executes in headless Chrome.

Reporting: Generates Automation_Report.html, which is uploaded as a workflow artifact.

Viewing the HTML Report

Go to Actions tab in your GitHub repository.

Select the latest workflow run.

Scroll to Artifacts and download Automation_Test_Report.

Project Structure
Automation_Selenium-with-Python--Home-Assessment-/
├── .github/
│   └── workflows/
│       └── main.yml           # GitHub Actions CI/CD pipeline
├── AUTOMATION-TEST-STORE-ECOMMERCE-WEBSITE/
│   └── Ecommerce-website.py   # Main Python automation script
├── Automation_Report.html     # Auto-generated HTML Test Report (after run)
└── README.md                  # Project documentation

Notes

The website used is a test e-commerce site, so all orders are dummy.

Script ensures dynamic data handling to prevent duplicate registrations.

Explicit waits and JS Executor ensure stability across CI/CD and local runs.

Recommended to run in PyCharm for better debugging and inspection.

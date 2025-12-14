# E-commerce Website End-to-End Test Automation Using Selenium and Python

This repository contains a comprehensive end-to-end automation test suite designed for the Automation Test Store e-commerce website. The automation framework is built using Python and Selenium WebDriver, and is fully integrated with GitHub Actions for continuous integration and deployment (CI/CD).

The project demonstrates expertise in designing stable and maintainable test scripts, handling dynamic test data, implementing robust explicit wait strategies, and integrating automated tests into a CI/CD pipeline, simulating a realistic e-commerce user journey from registration to checkout.

---

# Purpose and Objective of the Project

This project has been developed specifically for home assessment purposes to showcase proficiency and practical skills in test automation. The key objectives and skills demonstrated include:

| Assessment Requirement | Demonstrated Skills in This Project |
|------------------------|------------------------------------|
| Test Automation Foundation | Implementing automation using Python and Selenium WebDriver. |
| Real-world Scenario Simulation | Executing a complete e-commerce user journey: Registration, Browsing, Shopping, and Checkout. |
| Stable Test Design | Using explicit waits (WebDriverWait) to handle dynamic page loads and element availability. |
| Robustness of Tests | Using JavaScript Executor for critical interactions to ensure reliability in CI environments. |
| Dynamic Test Data Generation | Automatically creating unique, timestamped emails and usernames to avoid duplicate account issues. |
| Validation and Reporting | Implementing assertions on success messages and generating color-coded HTML test reports. |
| DevOps/CI Integration | Integration with GitHub Actions for automated test execution on every code push. |

---

# End-to-End Automation Test Flow and User Journey

The automation script covers a complete end-to-end user journey on the e-commerce website, simulating real user behavior.

## 1. User Registration Process

1. Navigate to the homepage of the website and click the **“Login or register”** option.  
2. Create a new user account using a **dynamically generated timestamped email**.  
3. Fill in the registration form with details including **Country (Pakistan)** and **Zone (Sindh)**.  
4. Verify the presence of the **“Account has been created”** success message to confirm successful registration.  

## 2. Shopping and Product Selection Journey

1. Click **“Continue”** to return to the homepage after registration.  
2. Navigate through the product categories: **Apparel & Accessories → Shoes**.  
3. Select a desired product and navigate to its **product detail page** for further actions.  

## 3. Checkout and Order Placement Process

1. Update the product quantity to **10 units** as part of the test scenario.  
2. Add the product to the shopping cart.  
3. Proceed to the checkout process using the **pre-filled registration details**.  
4. Complete the purchase and place the order.  

## 4. Verification of Successful Checkout

1. Validate that the **Checkout Confirmation page** appears and confirms that the order has been successfully processed.  

---

# Project Setup and Local Installation Instructions

The automation project can be executed locally using PyCharm or any other Python IDE. The setup steps are as follows:

## 1. Prerequisites for Running the Project

- Python version 3.8 or higher installed on your system.  
- Git installed and configured for repository management.  
- Google Chrome browser installed.  
- PyCharm IDE or any preferred Python development environment.  

## 2. Cloning the Project Repository

To clone the project repository to your local machine:

# Automation Selenium with Python - Home Assessment

## 1. Cloning the Project Repository

To clone the project repository to your local machine:

git clone [YOUR_GITHUB_REPO_LINK]
cd Automation_Selenium-with-Python--Home-Assessment-


## 2. Connecting Local Repository to GitHub 

git remote add origin [YOUR_GITHUB_REPO_LINK]
git branch -M main
git push -u origin main


## 3 Installing Required Python Dependencies

pip install selenium


## 4 Instructions for Running the Automation Test Script 

git add AUTOMATION-TEST-STORE-ECOMMERCE-WEBSITE/Ecommerce-website.py
git commit -m "checkout confirmation."
git push origin main
  Note: The script is configured to run Chrome in headless mode by default, providing faster execution and compatibility with CI/CD pipelines.


## From PyCharm

Open the project in PyCharm.
Locate Ecommerce-website.py in the project explorer.
Right-click on the script and select Run 'Ecommerce-website'.


# Continuous Integration and Deployment (CI/CD) Using GitHub Actions

## Workflow Overview

Trigger: The workflow runs automatically on every push to the main branch.
Environment Setup: The CI job runs on an Ubuntu Linux runner, installs Python, and the required dependencies (selenium).
Test Execution: The Selenium automation script runs in headless Chrome.
Reporting: After execution, the Automation_Report.html file is generated and uploaded as a workflow artifact for review.


## Viewing the Automation Test Report

Navigate to the Actions tab in your GitHub repository.
Select the most recent workflow run.
Scroll to the Artifacts section and download `Automation_Test_Report.html

## Project Directory Structure
<img width="874" height="245" alt="image" src="https://github.com/user-attachments/assets/5dfd57ff-2383-478b-8f59-2cd723fc8467" />


## Important Notes and Considerations

The website used for testing is a dummy e-commerce site, and all orders are non-functional.
The automation script dynamically generates test data to prevent duplicate registrations.
The use of explicit waits and JavaScript Executor ensures stable and reliable execution across both local and CI/CD environments.
Running the script in PyCharm is recommended for debugging, viewing logs, and inspecting web elements during development.



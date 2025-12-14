End-to-End Automation Test Flow and User Journey
The automation script covers a complete end-to-end user journey on the e-commerce website, simulating real user behavior.
1. User Registration Process
1.	Navigate to the homepage of the website and click the “Login or register” option.
2.	Create a new user account using a dynamically generated timestamped email.
3.	Fill in the registration form with details including Country (Pakistan) and Zone (Sindh).
4.	Verify the presence of the “Account has been created” success message to confirm successful registration.
2. Shopping and Product Selection Journey
1.	Click “Continue” to return to the homepage after registration.
2.	Navigate through the product categories: Apparel & Accessories → Shoes.
3.	Select a desired product and navigate to its product detail page for further actions.
3. Checkout and Order Placement Process
1.	Update the product quantity to 10 units as part of the test scenario.
2.	Add the product to the shopping cart.
3.	Proceed to the checkout process using the pre-filled registration details.
4.	Complete the purchase and place the order.
4. Verification of Successful Checkout
1.	Validate that the Checkout Confirmation page appears and confirms that the order has been successfully processed.
________________________________________
Project Setup and Local Installation Instructions
The automation project can be executed locally using PyCharm or any other Python IDE. The setup steps are as follows:
1. Prerequisites for Running the Project
•	Python version 3.8 or higher installed on your system.
•	Git installed and configured for repository management.
•	Google Chrome browser installed.
•	PyCharm IDE or any preferred Python development environment.
2. Cloning the Project Repository
To clone the project repository to your local machine:
git clone [YOUR_GITHUB_REPO_LINK]
cd Automation_Selenium-with-Python--Home-Assessment-
3. Connecting Local Repository to GitHub (Optional)
If you intend to push changes back to the GitHub repository:
git remote add origin [YOUR_GITHUB_REPO_LINK]
git branch -M main
git push -u origin main
4. Creating and Activating a Virtual Environment
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
5. Installing Required Python Dependencies
pip install selenium
________________________________________
Instructions for Running the Automation Test Script
The automation script can be executed directly from the terminal or using PyCharm.
From the Terminal
python AUTOMATION-TEST-STORE-ECOMMERCE-WEBSITE/Ecommerce-website.py
Note: The script is configured to run Chrome in headless mode by default, providing faster execution and compatibility with CI/CD pipelines.
From PyCharm
1.	Open the project in PyCharm.
2.	Locate Ecommerce-website.py in the project explorer.
3.	Right-click on the script and select Run 'Ecommerce-website'.
________________________________________
Continuous Integration and Deployment (CI/CD) Using GitHub Actions
This project is integrated with GitHub Actions to provide automated testing and immediate feedback upon code changes.
Workflow Overview
•	Trigger: The workflow runs automatically on every push to the main branch.
•	Environment Setup: The CI job runs on an Ubuntu Linux runner, installs Python, and the required dependencies (selenium).
•	Test Execution: The Selenium automation script runs in headless Chrome.
•	Reporting: After execution, the Automation_Report.html file is generated and uploaded as a workflow artifact for review.
Viewing the Automation Test Report
1.	Navigate to the Actions tab in your GitHub repository.
2.	Select the most recent workflow run.
3.	Scroll to the Artifacts section and download Automation_Test_Report.html to view the detailed test execution log.
________________________________________
Project Directory Structure
Automation_Selenium-with-Python--Home-Assessment-/
├── .github/
│   └── workflows/
│       └── main.yml           # GitHub Actions CI/CD pipeline configuration
├── AUTOMATION-TEST-STORE-ECOMMERCE-WEBSITE/
│   └── Ecommerce-website.py   # Main Python automation script
├── Automation_Report.html     # Auto-generated HTML test report
└── README.md                  # Project documentation
________________________________________
Important Notes and Considerations
•	The website used for testing is a dummy e-commerce site, and all orders are non-functional.
•	The automation script dynamically generates test data to prevent duplicate registrations.
•	The use of explicit waits and JavaScript Executor ensures stable and reliable execution across both local and CI/CD environments.
•	Running the script in PyCharm is recommended for debugging, viewing logs, and inspecting web elements during development.


import csv
import pytest
from pytest_html import extras
from pages.login_page import LoginPage
from pages.submission_page import SubmissionPage

# Read CSV data
with open("data_test_login.csv", newline="", encoding="utf-8") as f:
    users = list(csv.DictReader(f))

@pytest.mark.parametrize("user", users)
def test_login_and_submission(driver, user, request):
    login_page = LoginPage(driver)
    submission_page = SubmissionPage(driver)

    # Login
    login_page.open_login_page()
    assert login_page.login(user["email"], user["password"]), f"[ERROR] {user['email']} failed to log in."

    # Open submission form
    submission_page.open_submission_form()

    # Validation
    results = {}  # store validation results

    # Title length
    title_len = len(user["title"])
    results["Title length"] = "PASS" if title_len == 50 else f"FAIL ({title_len})"

    # Abstract word count
    abstract_len = len(user["abstract"].split())
    results["Abstract word count"] = "PASS" if 195 <= abstract_len <= 205 else f"FAIL ({abstract_len})"

    # Keywords count
    keyword_count = len([k.strip() for k in user["keywords"].split(",") if k.strip()])
    results["Keywords count"] = "PASS" if keyword_count == 7 else f"FAIL ({keyword_count})"

    # Print results in terminal
    print(f"\n[VALIDATION RESULTS] {user['email']}:")
    for key, value in results.items():
        print(f" - {key}: {value}")

    # Attach results to HTML report
    extra_info = "\n".join(f"{key}: {value}" for key, value in results.items())
    if hasattr(request.config, "_html"):
        request.config._html.extra.append(extras.text(extra_info, name=f"Validation Results ({user['email']})"))

    # Fill submission form
    submission_page.fill_submission_form(
        user["main_track"],
        user["sub_track"],
        user["title"],
        user["abstract"],
        user["keywords"],
        user["manuscript_ref_code"]
    )

    # Submit
    submission_page.submit()

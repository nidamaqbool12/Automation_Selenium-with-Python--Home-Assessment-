import csv
import pytest
from pages.register_page import RegisterPage

def read_users():
    with open("Valid_Register_data.csv", newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))

@pytest.mark.parametrize("user", read_users())
def test_registration(driver, user):
    page = RegisterPage(driver)
    page.open()
    page.fill_form(user)
    page.submit()

    errors = page.get_errors()
    if errors:
        print(f"[ERROR] {user['email']} → {' | '.join(errors)}")
    else:
        print(f"[SUCCESS] Registration submitted for {user['email']}")

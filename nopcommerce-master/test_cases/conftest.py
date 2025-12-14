import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Specify the browser: chrome or firefox or edge"
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()


########### For pytest-html reports ###########

# Hook for adding environment info in HTML report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project - nopcommerce'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Parag'


# Hook for deleting/modifying environment info in HTML report
@pytest.hookimpl(optionalhook=True)   # ✅ replaced deprecated decorator
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

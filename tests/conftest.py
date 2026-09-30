import allure
import pytest

from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(
        options=options
    )

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshot = (
                driver.get_screenshot_as_png()
            )

            allure.attach(
                screenshot,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )
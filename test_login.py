from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Load scenarios
scenarios('../features/login.feature')

@given("the user is on the login page")
def navigate_to_login(browser):
    browser.get("https://example.com/login")
    assert "Login" in browser.title

@when("the user enters valid username and password")
def enter_valid_credentials(browser):
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    
    username.send_keys("testuser@example.com")
    password.send_keys("ValidPass123")

@when("clicks the login button")
def click_login(browser):
    login_btn = browser.find_element(By.ID, "login-btn")
    login_btn.click()

@then("the user should be redirected to the dashboard")
def verify_dashboard_redirect(browser):
    WebDriverWait(browser, 10).until(
        EC.url_contains("/dashboard")
    )

@then(parsers.parse('an error message "{message}" should appear'))
def verify_error_message(browser, message):
    error_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
    )
    assert message in error_element.text

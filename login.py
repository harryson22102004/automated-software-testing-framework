from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTask:
    def __init__(self, actor):
        self.actor = actor
        
    def with_credentials(self, username, password):
        """Perform login with given credentials"""
        driver = self.actor.ability_to_browse_the_web().driver
        
        # Enter username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.clear()
        username_field.send_keys(username)
        
        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        
        # Click login button
        login_button = driver.find_element(By.ID, "login-btn")
        login_button.click()
        
        return self.actor

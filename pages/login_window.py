import time

from settings.log_setup import general_logger, exception_logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginWindow:
    def __init__(self, driver):
        self.driver = driver
        self.loginWindow_class = 'login-box'
        self.form_field_user_name_id = 'user-name'
        self.form_field_user_password_id = 'password'
        self.error_message_container = 'error-message-container'
        self.submit_button_id = 'login-button'
    
    def wait_for_element(self, by, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
        except Exception as e:
            exception_logger.error(f"Element {locator} not found: {e}")
            return None
    
    def open_login_window(self):
        try:
            login_window = self.wait_for_element(By.ID, self.loginWindow_id)
            if login_window:    
                general_logger.info("Login Pop Up Window Click")
            return True
        except Exception as e:
            exception_logger.error(f"Error opening Login Pop Up Window Click {e}")
            return False
    
    

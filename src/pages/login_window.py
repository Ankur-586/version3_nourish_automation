import time

from settings.log_setup import general_logger, exception_logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginWindow:
    def __init__(self, driver):
        self.driver = driver
        self.login_svg_button_navbar = "div.align-bottom svg"
        self.form_field_mobile_input_box = "input[placeholder='Enter Number']"
        self.form_field_continue_button = "button[type='submit']"
        self.otp_box_1 = "input[aria-label='Please enter OTP character 1']"
        self.otp_box_2 = "input[aria-label='Please enter OTP character 2']"
        self.otp_box_3 = "input[aria-label='Please enter OTP character 3']"
        self.otp_box_4 = "input[aria-label='Please enter OTP character 4']"
        self.otp_box_5 = "input[aria-label='Please enter OTP character 5']"
        self.otp_box_6 = "input[aria-label='Please enter OTP character 6']"
        self.otp_submit_button = "button[type='submit']"
     
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
            login_window = self.wait_for_element(By.CSS_SELECTOR, self.login_svg_button_navbar)
            if login_window:
                login_window.click()    
                general_logger.info("Login Pop Up Window Click")

                mobile_input_box = self.wait_for_element(By.CSS_SELECTOR, self.form_field_mobile_input_box)
                mobile_input_box.send_keys("8884154409")
                
                continue_button = self.wait_for_element(By.CSS_SELECTOR, self.form_field_continue_button)
                continue_button.click()
                
                otp_input_box_1 = self.wait_for_element(By.CSS_SELECTOR, self.otp_box_1)
                otp_input_box_2 = self.wait_for_element(By.CSS_SELECTOR, self.otp_box_2)
                otp_input_box_3 = self.wait_for_element(By.CSS_SELECTOR, self.otp_box_3)
                otp_input_box_4 = self.wait_for_element(By.CSS_SELECTOR, self.otp_box_4)
                otp_input_box_5 = self.wait_for_element(By.CSS_SELECTOR, self.otp_box_5)
                otp_input_box_6 = self.wait_for_element(By.CSS_SELECTOR, self.otp_box_6)

                otp_input_box_1.send_keys(1)
                otp_input_box_2.send_keys(2)
                otp_input_box_3.send_keys(3)
                otp_input_box_4.send_keys(4)
                otp_input_box_5.send_keys(5)
                otp_input_box_6.send_keys(6)
                
                otp_submit = self.wait_for_element(By.CSS_SELECTOR, self.otp_submit_button)
                otp_submit.click()
                time.sleep(5)
                return True
            return False
        except Exception as e:
            exception_logger.error(f"Error opening Login Pop Up Window Click {e}")
            return False
    
    # def _xyzget_login_window(self, input_field_mobile):
    #     try:
    #         login_window = self.wait_for_element(By.CSS_SELECTOR, self.loginWindow_button)
    #         login_window.click()
            
    #         pop_window = self.wait_for_element(By.XPATH, self.loginpopWindow)
    #         if not pop_window:
    #             general_logger.info(f'Not Found element {pop_window}')
    #             return False
            
    #         mobile_input_box = self.driver.find_element(By.XPATH, self.mobile_input_box)
    #         mobile_input_box.send_keys(input_field_mobile)
            
    #         next_button = self.driver.find_element(By.XPATH, self.next_button)
    #         next_button.click()
    #         general_logger.info("Next Button was clicked!")
            
    #         input_6_box = self.wait_for_element(By.XPATH, self.six_input_box)
    #         if not input_6_box:
    #             return False
    #         return True
            
    #     except NoSuchElementException as e:
    #         exception_logger.error(f"Element not found: {e}")
    #         return False
    #     except TimeoutException as e:
    #         exception_logger.error(f"Timeout error: {e}")
    #         return False
    #     except Exception as e:
    #         exception_logger.error(f"Unexpected error: {e}")
    #         return False

from selenium.webdriver.common.by import By

class LoginPage:

    EMAIL = (By.ID, "email")

    def __init__(self, driver):
        self.driver = driver
        
    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)
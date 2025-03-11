from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login = (By.ID, "login-button")
        self.title = (By.CLASS_NAME, "select_container")


    def login_credentials(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login).click()

    def logged_in_element_check(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.title)
        )

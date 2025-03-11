from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker

class FormPage:
    def __init__(self,driver):
        self.driver = driver
        self.faker = Faker()
        self.cart = (By.ID, "shopping_cart_container")
        self.checkout = (By.ID, "checkout")
        self.firstname = (By.NAME, "firstName")
        self.lastname = (By.NAME, "lastName")
        self.postalcode = (By.ID,"postal-code")
        self.submit = (By.NAME,"continue")
        self.finish = (By.ID,"finish")

    def open_cart_and_checkout(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.cart)).click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.checkout)).click()

    def form_fill(self):
        self.driver.find_element(*self.firstname).send_keys(self.faker.first_name())
        self.driver.find_element(*self.lastname).send_keys(self.faker.last_name())
        self.driver.find_element(*self.postalcode).send_keys(self.faker.postalcode())
        self.driver.find_element(*self.submit).click()
        self.driver.find_element(*self.finish).click()
        print("First Name -", self.faker.last_name())
        print("Last Name - ", self.faker.first_name())
        print("Postal code - ", self.faker.postalcode())

    def form_fill_check(self):
        assert "Thank you for your order!" in self.driver.page_source, "Checkout failed"






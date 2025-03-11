import json
import pytest
from webdriver_setup.webdriver_setup import get_driver
from page_object_model.login import LoginPage
from page_object_model.form_page import FormPage

@pytest.fixture
def setup():
    driver = get_driver()
    with open("Credentials/config.json") as file:
           config = json.load(file)

    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login_credentials(config["username"], config["password"])
    assert login.logged_in_element_check(), "Login Failed"
    print("Login Successful")

    yield driver
    driver.quit()

def test_form_submission(setup):
    driver = setup

    form = FormPage(driver)
    form.open_cart_and_checkout()
    print("you can proceed to checkout")

    form.form_fill()
    form.form_fill_check()
    print("Form filled successfully")





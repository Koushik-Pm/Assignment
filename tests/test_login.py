import json
import pytest
from webdriver_setup.webdriver_setup import get_driver
from page_object_model.login import LoginPage

@pytest.fixture
def setup():
    driver = get_driver()
    with open("Credentials/config.json") as file:
           config = json.load(file)

    driver.get("https://www.saucedemo.com/")
    yield driver,config
    driver.quit()

def test_login(setup):
    driver, config = setup
    login = LoginPage(driver)
    login.login_credentials(config["username"],config["password"])
    assert login.logged_in_element_check(), "Login Failed"
    print ("Login Successful")

from selenium.webdriver.common.by import By
from integration_tests.pages.base_page import BasePage
from ...tests import config


class LoginPage(BasePage):
    _login_form = {"by": By.ID, "value": "login"}
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "button"}
    _success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    _failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}

    def __init__(self, driver, url="/login"):
        self.driver = driver
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)
        assert self._is_displayed(self._login_form)

    def with_(self, username, password):
        self.driver.find_element(self._username_input["by"],
                                 self._username_input["value"]).send_keys(username)
        self.driver.find_element(self._password_input["by"],
                                 self._password_input["value"]).send_keys(password)
        self.driver.find_element(self._submit_button["by"],
                                 self._submit_button["value"]).click()

    def success_message_present(self):
        return self._is_displayed(self._success_message)

    def failure_message_present(self):
        return self._is_displayed(self._failure_message)
    
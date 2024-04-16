from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from ..tests import config


class LoginPage(BasePage):
    _login_form = {"by": By.ID, "value": "login"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "button"}
    

    def __init__(self, driver, url="/login"):
        self.driver = driver
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)
        assert self._is_displayed(self._login_form)


    def login(self):
        return True

    
import pytest

from pages.demo.login_page import LoginPage


class TestLogin():

    @pytest.fixture
    def login(self, driver):
        return LoginPage(driver)

    # @pytest.mark.foo
    # @pytest.mark.shallow
    def test_BestBuy_login(self, login):
        # login.with_("tomsmith", "SuperSecretPassword!")
        assert(True)

    # # @pytest.mark.deep
    # def test_invalid_credentials(self, login):
    #     login.with_("tomsmith", "bad password")
    #     assert(login.failure_message_present())        
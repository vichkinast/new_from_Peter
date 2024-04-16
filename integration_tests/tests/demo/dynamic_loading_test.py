import pytest
from integration_tests.pages.demo.dynamic_loading_page import DynamicLoadingPage


@pytest.mark.deep
class TestDynamicLoading():

    @pytest.fixture
    def dynamic_loading(self, driver):
        return DynamicLoadingPage(driver)

    def test_hidden_element(self, dynamic_loading):
        dynamic_loading.load_example("1")
        assert(dynamic_loading.finish_text_present())

    def test_rendered_element(self, dynamic_loading):
        dynamic_loading.load_example("2")
        assert(dynamic_loading.finish_text_present())

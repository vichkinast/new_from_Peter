import pytest

from . import config
from integration_tests.common.driver_manager import DriverManager

def pytest_addoption(parser):
    """
    Defines custom command line options for pytest.

    Args:
        parser Parser: pytest command line parser
    """
    parser.addoption("--baseurl",
                     action = "store",
                     default = config.default_base_url,
                     help = "Base URL for the application under test")
    parser.addoption("--browser",
                      action = "store",
                      default = "chrome",
                      help = "The name of the browser to test with"
                      )
    parser.addoption("--host",
                    action = "store",
                    default = "local",
                    help = "The name of the host to run tests in"
                    )
    parser.addoption("--headless",
                    action = "store",
                    default = "true",
                    help = "Switch to run headless or not"
                    )
    parser.addoption("--start-maximized",
                      action = "store",
                      default = "true",
                      help = "Switch to maximized or not"
                      )
    parser.addoption("--scope",
                      action = "store",
                      default = "session",
                      help = "Scope for which the driver exists"
                      )
    parser.addoption("--platform",
                    action = "store",
                    default = "Windows 11",
                    help = "Platform to run tests on remote"
                    )

def get_scope(fixture_name, config):
    config.scope = config.getoption("--scope")
    return config.scope

@pytest.fixture
def driver(request):
    """
    Setup fixture that runs before and after each test that invokes it as an argument.
    Stores the values of the custom command line parameters in the applcable variables in config.py
    Gets a driver from the DriverManager in driver_manager.py
    Returns a driver to the test so it can be passed into pages.
    After the test it disposes of the driver and resets the shared driver instance _driver in DriverManager to None

    Args:
        request Request: Request object from pytest

    Returns:
        webdriver: The webdriver to beused in the test.
    """
    # Store command line parameter values in config.py
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()
    config.host = request.config.getoption("--host").lower()
    config.headless = request.config.getoption("--headless")
    config.start_maximized = request.config.getoption("--start-maximized")
    
    # Get a shared drive instance
    driver_ = DriverManager.get_driver()

    def quit():
        """
        Cleans up the driver.
        """
        DriverManager.quit_session()
    # Schedule the clean up function to run after the test
    request.addfinalizer(quit)
    # Passes the driver to any test that invokes it as an argument
    return driver_


    
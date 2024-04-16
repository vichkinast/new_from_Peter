from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..tests import config

class BasePage():
    """
    Base Page for generic pages
    
    """
    
    def __init__(self, driver):
        """
        Initializes Base page.
        
        """
        # Driver passed in to Page from instantiating test
        self.driver = driver
        
        # Gets the base URL from 'conf.py' Base URL is set by a command line option defined in conftest.py. It defaults to 'hudl.com'. 
        # The value is stored in conf.py in conftest.py.  
        self._baseurl = config.baseurl
        
        # Defines generic URL to be used in methods common to all Pages. It is overwritten by the individual Pages as required.
        self._url = ""
        
        # Define a common locator to be used by wait_for_page_to_load(). It is overwritten by the individual Pages as required.
        self._page_loaded_indicator = (By.ID, "") # Must be filled in if not overwritten by individual pages
    
    def _load(self, url):
        """
        Opens the page specified by _url. When invoked on a specific page (e.g. Login page) it opens that page.
        
        """
        if self._url == "" : self._url = url
        if self._url.startswith("http"):
            self.driver.get(self._url)
        else:
            self.driver.get(config.baseurl + self._url)

    def _find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])
    
    def _click(self, locator):
        self._find(locator).click()
        
    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)
    
    def _wait_for_page_to_load(self, timeout):
        """
        Uses a reliable locator for each page with the Expected Condition to determine when the page has loaded.
        When invoked on a specific page (e.g. Login page) it waits for that page to load.
        
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self._page_loaded_indicator))
    
    def _is_current_page(self):
        """
        Checks whether or not the Page on which it is invoked is actually the current page.
        Used to verify if the current page is the expected page.
        Returns:
            bool: Indicates whether or not the page it is called on is the current page.
        """
        return self.driver.current_url in self._url
    
    def _is_displayed(self, locator, timeout=0):
        """
        Checks whether the element specified by the locator is displayed on the page within the timeout.
        If the timeout is 0 it simply checks if the element is displayed.

        Args:
            locator locator: Locator for the element being checked
            timeout (int, optional): Maximum time in seconds to wait for element to be displayed. Defaults to 0.

        Returns:
            bool: Indicates whether or not the 
        """
        if timeout > 0:
            try:
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self.driver.find_element(locator['by'], locator['value'])
            except NoSuchElementException:
                return False
    
    def _refresh(self):
        """
        Refreshes the page and waits for it to reload.
        """
        self.driver.refresh()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self._page_loaded_indicator))
    
    def _click_blocked_element(self, element):
        """
        To be used in the case when an element cannot be clcked because it is blocked by another element.

        Args:
            element element: Element to be clicked
        """
        ActionChains(self.driver).move_to_element(element).click(element).perform()
    

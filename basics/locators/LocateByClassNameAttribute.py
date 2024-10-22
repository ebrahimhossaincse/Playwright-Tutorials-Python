import unittest
from playwright.sync_api import sync_playwright
import time

class LocateElementByClassName(unittest.TestCase):

    url = "https://www.daraz.com.bd/"
    browser_name = "chrome"
    is_headless = "true"

    @classmethod
    def setUpClass(cls):
        """Set up Playwright and start the browser before all tests."""
        cls.start_browser()

    @classmethod
    def start_browser(cls):
        """Launch the specified browser."""
        cls.playwright = sync_playwright().start()

        if cls.browser_name.lower() in ['chrome', 'chromium']:
            cls.browser_type = cls.playwright.chromium
        elif cls.browser_name.lower() == 'firefox':
            cls.browser_type = cls.playwright.firefox
        elif cls.browser_name.lower() in ['edge', 'safari']:
            cls.browser_type = cls.playwright.webkit
        else:
            raise ValueError(f"This '{cls.browser_name}' is not supported.")

        cls.is_headless = cls.is_headless.lower() == "true"
        cls.browser = cls.browser_type.launch(headless=cls.is_headless)
        cls.page = cls.browser.new_page()
        print(f"**** Project Browser Name and Version is : {cls.browser_name} : {cls.browser.version}")

    def launch_application(self, url):
        """Navigate to the specified URL."""
        self.page.goto(url)
        time.sleep(5)  # Wait for the page to load

    def test_locate_element_by_class_name(self):
        """Test locating an element by class name and clicking it."""
        self.launch_application(self.url)
        element = self.page.query_selector(".bld-txt")

        if element:
            element.click()
            time.sleep(5)  # Wait after clicking to observe the result
        else:
            self.fail("Element with class '.bld-txt' not found.")

    @classmethod
    def tearDownClass(cls):
        """Close the browser and Playwright after all tests."""
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

if __name__ == "__main__":
    unittest.main()

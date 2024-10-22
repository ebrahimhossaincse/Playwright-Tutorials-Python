import unittest
from playwright.sync_api import sync_playwright
import time

class CrossBrowserConfiguration(unittest.TestCase):

    url = "https://staging-sp.dev.prep.achievetestprep.com/internal-login"
    browser_name = "firefox"
    headless = 'false'

    @classmethod
    def setUpClass(cls):
        """Setup Playwright and browser before tests."""
        cls.playwright = sync_playwright().start()
        cls.browser_type = cls.playwright.chromium  # Default to Chromium (Chrome)

        if cls.browser_name.lower() == "chrome" or cls.browser_name.lower() == "chromium":
            cls.browser_type = cls.playwright.chromium
        elif cls.browser_name.lower() == "webkit":
            cls.browser_type = cls.playwright.webkit
        elif cls.browser_name.lower() == "firefox":
            cls.browser_type = cls.playwright.firefox
        else:
            raise ValueError(f"Browser '{cls.browser_name}' is not supported.")

        # Convert the headless string to a boolean
        cls.is_headless = cls.headless.lower() == "true"
        cls.browser = cls.browser_type.launch(headless=cls.is_headless)
        cls.page = cls.browser.new_page()
        print(f"**** Project Browser Name and Version is : {cls.browser_name} : {cls.browser.version}")  # Accessing version correctly

    def launch_application(self, url):
        """Navigates to the given URL."""
        self.page.goto(url)
        time.sleep(3)  # Simulate waiting time

    @classmethod
    def tearDownClass(cls):
        """Close the Playwright browser after all tests."""
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

if __name__ == "__main__":
    unittest.main()

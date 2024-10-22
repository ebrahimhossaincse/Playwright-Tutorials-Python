import unittest
from playwright.sync_api import sync_playwright
import time

class TestChromeBrowser(unittest.TestCase):
    url = "https://staging-sp.dev.prep.achievetestprep.com/internal-login"

    @classmethod
    def setUpClass(cls):
        """Runs before all tests."""
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=True)
        cls.page = cls.browser.new_page()
        user_agent = cls.page.evaluate("navigator.userAgent")  # Fetch user agent
        print(f"**** Chrome Browser User Agent is: {user_agent}")

    def test_open_url(self):
        """Test to open a URL and wait for 5 seconds."""
        # Using class-level page object in the test
        self.page.goto(self.url)
        time.sleep(5)  # Simulating delay for loading

    @classmethod
    def tearDownClass(cls):
        """Runs after all tests."""
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

if __name__ == "__main__":
    unittest.main()

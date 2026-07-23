from typing import Optional
from playwright.sync_api import Browser, BrowserContext, Page, Playwright


class BrowserManager:
    """
    Responsible for managing the Playwright browser lifecycle.
    """

    def __init__(self, playwright: Playwright, config):
        """
        Initialize BrowserManager.

        Args:
            playwright: Playwright instance
            config: ConfigManager instance
        """
        self._playwright = playwright
        self._config = config

        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None


    def launch_browser(self):
        """
        Launch the configured browser.
        """
        browser_name = self._config.get("browser.name")
        headless = self._config.get("browser.headless")
        slow_mo = self._config.get("browser.slow_mo")

        if browser_name == "chromium":
            browser_type = self._playwright.chromium
        elif browser_name == "firefox":
            browser_type = self._playwright.firefox
        elif browser_name == "webkit":
            browser_type = self._playwright.webkit
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        self._browser = browser_type.launch(headless=headless, slow_mo=slow_mo)
        return self._browser
    
    
    def create_context(self) -> BrowserContext:
        """
        Create a new browser context which provides an isolated browser session.
        """
        if self._browser is None:
            raise RuntimeError("Browser is not launched. Call launch_browser() first.")
        
        self._context = self._browser.new_context()
        return self._context
    

    def create_page(self) -> Page:
        """
        Create a new page inside the browser context.
        """
        if self._context is None:
            raise RuntimeError("Browser context is not created. Call create_context() first.")
        
        self._page = self._context.new_page()
        return self._page
    

    def close(self) -> None:
        """
        Close the browser and release resources.
        """
        if self._context is not None:
            self._context.close()

        if self._browser is not None:
            self._browser.close()

        self._page = None
        self._context = None
        self._browser = None


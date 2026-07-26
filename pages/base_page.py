from playwright.sync_api import Page


class BasePage:
    """
    Base class for all Page Object Classes.
    Contains common browser interaction methods.
    """
    def __init__(self, page: Page):
        self.page = page

    
    def navigate(self, url: str) -> None:
        """
        Navigate to the specified URL.
        """
        self.page.goto(url)

    
    def get_title(self) -> str:
        """
        Return the current page title.
        """
        return self.page.title()
    

    def get_current_url(self) -> str:
        """
        Return the current page URL.
        """
        return self.page.url
    

    def click(self, locator: str) -> None:
        """
        Click an element using its locator.
        """
        self.page.locator(locator).click()


    def fill(self, locator: str, value: str) -> None:
        """
        Fill an input field.
        """
        self.page.locator(locator).fill(value)

    
    def get_text(self, locator: str) -> None:
        """
        Return the text content of an element.
        """
        return self.page.locator(locator).inner_text()
    

    def is_visible(self, locator: str) -> bool:
        """
        Check whether an element is visible.
        """
        return self.page.locator(locator).is_visible()


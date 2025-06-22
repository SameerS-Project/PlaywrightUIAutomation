from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def set(self, selector: str, value: str):
        self.page.fill(selector, value)

    def click(self, selector: str):
        self.page.click(selector)

    def get_text(self, selector: str):
        return self.page.inner_text(selector)

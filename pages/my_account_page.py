from playwright.sync_api import expect
from pages.base_page import BasePage

class MyAccountPage(BasePage):
    def is_heading_visible(self):
        return self.page.locator("//h2[@class='card-header h5' and text()='My Account']").is_visible()

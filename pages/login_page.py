
#from playwright.sync_api import sync_playwright, Playwright
#from pytest_playwright.pytest_playwright import browser
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "#input-email"
        self.password_input = "#input-password"
        self.login_button = "//div[@id='content']//input[@value='Login']"
        self.warning_message = "//div[contains(@class, 'alert-danger')]"
        #self.warning_message = "#account-login .alert-danger"

    def set_email(self, email):
        self.set(self.email_input, email)

    def set_password(self, password):
        self.set(self.password_input, password)

    def click_login_button(self):
        self.click(self.login_button)

    def log_into_application(self, email, password):
        """Main login method"""
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def get_warning_message(self):
        """Returns warning message if login fails"""
        return self.get_text(self.warning_message)


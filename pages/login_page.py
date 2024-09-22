from pages.base import Base
from Locators.login import Login
from data.assertions import Assertions
from playwright.sync_api import Page


class LoginPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def login_user(self, username, password):
        self.open("")
        self.input(Login.USERNAME_INPUT, username)
        self.input(Login.PASSWORD_INPUT, password)
        
    def click_login(self):
        self.click(Login.LOGIN_BTN)
    
    def check_message_error(self, message):
        self.assertion.contain_text(Login.ERROR_MESSAGE, message, "True Authorization")

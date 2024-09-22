from pages.base import Base
from Locators.checkout import Checkout
from data.assertions import Assertions
from playwright.sync_api import Page


class CheckoutPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def write_info(self, first_name, last_name, zip_code): 
        self.input(Checkout.FIRST_NAME, first_name)
        self.input(Checkout.LAST_NAME, last_name)
        self.input(Checkout.ZIP, zip_code)

    def click_continue(self):
        self.click(Checkout.CNT_BTN)

    def check_message_error(self, message):
        self.assertion.contain_text(Checkout.ERROR_MESSAGE, message, "Checkout info is entered correctly!")
    
    def check_finish(self):
        self.click(Checkout.FINISH_BTN)
        self.assertion.have_text(Checkout.FINAL_TEXT, "Checkout: Complete!", "no")

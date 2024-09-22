from pages.base import Base
from Locators.checkout import Basket
from data.assertions import Assertions
from playwright.sync_api import Page


class CheckoutPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def checkout(self): 
        self.click(Basket.CHECKOUT_BTN)
        self.input(Basket.FIRST_NAME, "Ivan")
        self.input(Basket.LAST_NAME, "Ivanov")
        self.input(Basket.ZIP, "123456")
        self.click(Basket.CNT_BTN)
        self.click(Basket.FINISH_BTN)
        self.assertion.have_text(Basket.FINAL_TEXT, "Checkout: Complete!", "no")

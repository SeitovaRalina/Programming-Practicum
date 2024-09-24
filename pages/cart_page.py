from pages.base import Base
from Locators.cart import Cart
from data.assertions import Assertions
from playwright.sync_api import Page


class CartPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def remove_item_from_cart(self, name):
        formatted_name = str.lower(name).replace(" ", "-")
        self.click(Cart.REMOVE_BTN.replace('item-name', formatted_name))

    def check_logo(self):
        self.assertion.check_presence(Cart.LOGO, "The logo is not 'Your Cart'")

    def check_count_items(self, count): 
        len_items = len(self.wait_for_all_elements(Cart.CART_ITEM))
        self.assertion.check_equals(len_items, count, f"There should be {len_items} items in the cart")

    def check_item_name_in_cart(self, item_name):
        self.assertion.contain_text(Cart.ITEM_NAME, item_name, "The item name is not correct")

    def click_go_to_market(self):
        self.click(Cart.FOLLOW_TO_MARKET_BTN)

    def click_checkout(self):
        self.click(Cart.CHECKOUT_BTN)

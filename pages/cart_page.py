from pages.base import Base
from Locators.cart import Cart
from data.assertions import Assertions
from playwright.sync_api import Page


class CartPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def remove_items_from_cart(self, item_ids):
        if isinstance(item_ids, int):
            item_ids = [item_ids]

        for id in item_ids:
            self.click_element_by_index(Cart.REMOVE_BTN, id)

    def check_logo(self):
        self.assertion.check_presence(Cart.LOGO, "The logo is not 'Your Cart'")

    def check_count_items(self, count): 
        len_items = len(self.wait_for_all_elements(Cart.CART_ITEM))
        self.assertion.check_equals(len_items, count, f"There should be {len_items} items in the cart")

    def check_items_in_cart(self, names):
        if isinstance(names, str):
            names = [names]
        items = self.wait_for_all_elements(Cart.ITEM_NAME)
        for i, item in enumerate(items):
            self.assertion.check_equals(item.text_content(), names[i], "The item name is not correct")
    
    def click_to_market_button(self):
        self.click(Cart.MARKET_BTN)

    def click_checkout_button(self):
        self.click(Cart.CHECKOUT_BTN)

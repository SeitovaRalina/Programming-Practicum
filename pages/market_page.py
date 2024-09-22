from typing import List
from pages.base import Base
from Locators.market import Market
from data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def check_logo(self):
        self.assertion.check_presence(Market.LOGO, "The logo is not 'Product'")

    def add_item_to_cart(self, name):
        formatted_name = str.lower(name).replace(" ", "-")
        self.click(Market.ADD_TO_CART_BTN.replace('item-name', formatted_name))

    def click_go_to_cart(self):
        self.click(Market.FOLLOW_TO_CART_BTN)

    def sort_items(self, value):
        self.click(Market.ITEMS_SORTER)
        self.selector(Market.ITEMS_SORTER, value)

    def check_sorted_items_by_price(self, reverse):
        items = self.wait_for_all_elements(Market.ITEM_PRICE)
        prices = [item.text_content() for item in items]

        sorted_prices = sorted(prices, key=lambda x: float(x[1:]), reverse=reverse)
        self.assertion.check_equals(prices, sorted_prices, "The items are not sorted by price")

    def check_sorted_items_by_name(self, reverse):
        items = self.wait_for_all_elements(Market.ITEM_NAME)
        names = [item.text_content() for item in items]

        sorted_names = sorted(names, reverse=reverse)
        self.assertion.check_equals(names, sorted_names, "The items are not sorted by name")

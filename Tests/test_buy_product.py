import pytest
from pages.cart_page import CartPage
from pages.market_page import MarketPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_auth')
class TestBuyProduct:
    def test_add_product_to_cart(self, browser):
        market_page = MarketPage(browser)
        cart_page = CartPage(browser)
        
        market_page.add_items_to_cart(0)

        cart_page.check_items_in_cart('Sauce Labs Backpack')
        cart_page.check_count_items(1)


    def test_add_products_to_cart(self, browser):
        market_page = MarketPage(browser)
        cart_page = CartPage(browser)
        item_ids = [0, 3, 5]
        item_names = ['Sauce Labs Backpack', 'Sauce Labs Fleece Jacket', 'Test.allTheThings() T-Shirt (Red)']
        
        market_page.add_items_to_cart(item_ids)
        
        cart_page.check_count_items(len(item_ids))
        cart_page.check_items_in_cart(item_names)






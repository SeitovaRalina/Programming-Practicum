import pytest
from pages.cart_page import CartPage
from pages.market_page import MarketPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_auth')
class TestBuyProduct:
    def test_add_product_to_cart(self, browser):
        market_page = MarketPage(browser)
        cart_page = CartPage(browser)
        item_name = 'Sauce Labs Onesie'
        
        market_page.add_item_to_cart(item_name)
        market_page.click_go_to_cart()

        cart_page.check_count_items(1)
        cart_page.check_item_name_in_cart(item_name)
    
    def test_add_products_to_cart(self, browser):
        market_page = MarketPage(browser)
        cart_page = CartPage(browser)
        item_names = ['Sauce Labs Backpack', 
                      'Sauce Labs Fleece Jacket', 
                      'Sauce Labs Bike Light']
        
        for item_name in item_names:
            market_page.add_item_to_cart(item_name)
        market_page.click_go_to_cart()
        
        cart_page.check_count_items(len(item_names))

    def test_remove_product_from_cart(self, browser):
        market_page = MarketPage(browser)
        cart_page = CartPage(browser)
        item_name = 'Sauce Labs Backpack'
        
        market_page.add_item_to_cart(item_name)
        market_page.click_go_to_cart()

        cart_page.check_count_items(1)
        cart_page.check_item_name_in_cart(item_name)

        cart_page.remove_item_from_cart(item_name)
        cart_page.check_count_items(0)

    def test_remove_all_products_from_cart(self, browser):
        market_page = MarketPage(browser)
        cart_page = CartPage(browser)
        item_names = ['Sauce Labs Bolt T-Shirt',
                      'Sauce Labs Fleece Jacket']
        
        for item_name in item_names:
            market_page.add_item_to_cart(item_name)
        market_page.click_go_to_cart()
        
        cart_page.check_count_items(len(item_names))

        for item_name in item_names:
            cart_page.remove_item_from_cart(item_name)

        cart_page.check_count_items(0)

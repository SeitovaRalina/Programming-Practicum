import pytest
from pages.market_page import MarketPage


@pytest.fixture(scope='function')
def product_buy(browser, user_auth):
    market_page = MarketPage(browser)
    item_name = 'Sauce Labs Onesie'
    
    market_page.add_item_to_cart(item_name)
    market_page.click_go_to_cart()
import pytest
from pages.market_page import MarketPage
from utils.sort_variants import testing_sort_price, testing_sort_name


@pytest.mark.regression
@pytest.mark.usefixtures('user_auth')
class TestSortProductsinMarket:
    @pytest.mark.parametrize('value, reversed_sort', testing_sort_price)
    def test_sort_items_by_price(self, browser, value, reversed_sort):
        market_page = MarketPage(browser)

        market_page.sort_items(value)
        market_page.check_sorted_items_by_price(reversed_sort)

    @pytest.mark.parametrize('value, reversed_sort', testing_sort_name)
    def test_sort_items_by_name(self, browser, value, reversed_sort):
        market_page = MarketPage(browser)

        market_page.sort_items(value)
        market_page.check_sorted_items_by_name(reversed_sort)

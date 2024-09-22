import pytest
from pages.login_page import LoginPage
from pages.market_page import MarketPage
from utils.auth_data import testing_data


@pytest.mark.regression
class TestLogin:    
    @pytest.mark.parametrize("username, password, error_message", testing_data)
    def test_user_login_fail(self, browser, username, password, error_message):
        login_page = LoginPage(browser)
        login_page.login_user(username, password)
        
        login_page.check_message_error(error_message)

    @pytest.mark.usefixtures('user_auth')
    def test_user_login(self, browser):
        market_page = MarketPage(browser)
        
        market_page.check_logo()

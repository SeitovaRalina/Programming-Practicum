import pytest
from pages.login_page import LoginPage
from data.constants import Constants


@pytest.fixture(scope='function')
def user_auth(browser):
    p = LoginPage(browser)
    p.login_user(Constants.login, Constants.password)
    p.click_login()

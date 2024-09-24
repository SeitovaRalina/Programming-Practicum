import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.checkout_data import testing_data


@pytest.mark.regression
@pytest.mark.usefixtures('product_buy')
class TestCheckout:
    @pytest.mark.parametrize('first_name, last_name, zip_code, error_message', testing_data)
    def test_checkout_fail(self, browser, first_name, last_name, zip_code, error_message):
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)

        cart_page.click_checkout()
        
        checkout_page.write_info(first_name, last_name, zip_code)
        checkout_page.click_continue()

        checkout_page.check_message_error(error_message)

    def test_checkout_success(self, browser):
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)

        cart_page.click_checkout()

        checkout_page.write_info('Test', 'Test', '12345')
        checkout_page.click_continue()

        checkout_page.check_finish()



    

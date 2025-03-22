import pytest
from playwright.sync_api import Page
from pages.cart_page import CartPage

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

def test_complete_cart_flow(page: Page, cart_page: CartPage):
    cart_page.login()
    cart_page.select_product()
    cart_page.accessing_cart()
    cart_page.checkout()
    cart_page.payments()


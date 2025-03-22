from playwright.sync_api import Page, expect
import time

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self):
        self.page.goto("https://www.saucedemo.com/v1/index.html")
        time.sleep(2)
        assert self.page.title() == "Swag Labs"
        self.page.fill("#user-name", "standard_user")
        self.page.fill("#password", "secret_sauce")
        self.page.click("#login-button")
        self.page.wait_for_url("https://www.saucedemo.com/v1/inventory.html")

    def select_product(self):
        list_locator = self.page.locator("#contents_wrapper")
        expect(list_locator).to_be_visible()

        self.page.locator(".inventory_item_name").nth(0).click()
        self.page.wait_for_url("https://www.saucedemo.com/v1/inventory-item.html?id=4")
        expect(self.page.locator('//*[contains(text(),"Sauce Labs Backpac")]')).to_be_visible()
        expect(self.page.get_by_text("$29.99", exact=True)).to_be_visible()
        self.page.click(".btn_primary.btn_inventory")

    def accessing_cart(self):
        self.page.wait_for_selector("#shopping_cart_container > a")
        self.page.click("#shopping_cart_container > a")
        self.page.wait_for_url('https://www.saucedemo.com/v1/cart.html')
        expect(self.page.get_by_text("Sauce Labs Backpack")).to_be_visible()
        self.page.wait_for_selector("a.btn_action.checkout_button")
        self.page.click("a.btn_action.checkout_button")
        self.page.wait_for_url("https://www.saucedemo.com/v1/checkout-step-one.html")

    def checkout(self):
        self.page.fill("#first-name", "Elen")
        self.page.fill("#last-name", "Crozara")
        self.page.fill("#postal-code", "38400644")
        self.page.click(".btn_primary.cart_button")

    def payments(self):
        self.page.wait_for_url("https://www.saucedemo.com/v1/checkout-step-two.html")
        expect(self.page.get_by_text("Sauce Labs Backpack")).to_be_visible()
        expect(self.page.get_by_text("$29.99", exact=True)).to_be_visible()
        expect(self.page.get_by_text("SauceCard #31337")).to_be_visible()
        expect(self.page.get_by_text("32.39")).to_be_visible()
        self.page.get_by_role("link", name="FINISH").click()
        self.page.wait_for_url("https://www.saucedemo.com/v1/checkout-complete.html")
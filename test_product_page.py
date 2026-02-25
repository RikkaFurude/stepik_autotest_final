import pytest
from .pages.product_page import ProductPage

@pytest.mark.login_guest
class TestLoginFromProductPage():
    # Фикстура setup: подготовит ссылку перед каждым тестом
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = "http://selenium1py.pythonanywhere.com"
    
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверяем, что подстрока "login" есть в текущем URL
        current_url = self.browser.current_url
        assert "login" in current_url, f"Expected 'login' in URL, but got {current_url}"

    def should_be_login_form(self):
        # Проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage): 
    def go_to_login_page(self):
        # Используем символ *, чтобы распаковать кортеж из локейторов
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # Проверяем наличие элемента, передавая кортеж целиком через *
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
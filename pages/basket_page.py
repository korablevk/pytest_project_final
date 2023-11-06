from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
import time


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket(self):
        time.sleep(3)
        assert self.is_element_present(*BasketPageLocators.MESSAGE), "No message that basket is empty"

    def should_not_be_empty_basket(self):
        time.sleep(3)
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE), "Element message that basket is empty"

    def check_should_be_empty_basket_message(self):
        a_message = self.browser.find_element(*BasketPageLocators.MESSAGE).text
        print(a_message)
        assert a_message.rstrip() == "Your basket is empty. Continue shopping", "Element message that basket is empty"
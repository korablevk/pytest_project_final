from .base_page import BasePage
from .locators import CatalogPageLocators
from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*CatalogPageLocators.ADD_TO_BASKET)
        link.click()

    def product_added(self):
        time.sleep(3)
        a_message = self.browser.find_element(*CatalogPageLocators.ADD_MESSAGE)
        title = self.browser.find_element(*CatalogPageLocators.TITLE_NAME)
        a_price = self.browser.find_element(*CatalogPageLocators.MESSAGE_PRICE)
        price = self.browser.find_element(*CatalogPageLocators.TITLE_PRICE)
        busket_price = self.browser.find_element(*CatalogPageLocators.BASKET_PRICE).text
        assert title.text == a_message.text, "Ошибка"
        assert a_price.text == price.text == busket_price[14:-12], "Ошибка"
        print("Succed")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CatalogPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*CatalogPageLocators.SUCCESS_MESSAGE), "Success message is disappear"

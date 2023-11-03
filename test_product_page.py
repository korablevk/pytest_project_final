import time

from selenium.webdriver.common.by import By
from .pages.product_page import BasketPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = BasketPage(browser, link)
    page.open()
    # page.should_be_empty_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added()
    # time.sleep(600)
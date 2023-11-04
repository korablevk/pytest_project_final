import time
import pytest
from selenium.webdriver.common.by import By
from .pages.product_page import BasketPage


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = BasketPage(browser, link)
#     page.open()
#     # page.should_be_empty_basket()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.product_added()
#     # time.sleep(600)

# @pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", marks=pytest.mark.skip),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_add_product_to_basket(browser):
    page = BasketPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = BasketPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = BasketPage(browser, link)
    page.open()
    time.sleep(2)
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = BasketPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added()
    page.success_message_should_disappear()


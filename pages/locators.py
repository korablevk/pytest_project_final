from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class CatalogPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div p strong")
    MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span[class='btn-group'] a")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    TITLE_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    TITLE_PRICE = (By.CSS_SELECTOR, "p.price_color")




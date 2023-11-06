from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.should_be_login_url('http://selenium1py.pythonanywhere.com/ru/accounts/login/'), "Login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_INPUT)
        password1_input = self.browser.find_element(*LoginPageLocators.EMAIL_PASSWORD_INPUT1)
        password2_input = self.browser.find_element(*LoginPageLocators.EMAIL_PASSWORD_INPUT2)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        register_btn.click()


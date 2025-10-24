import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        # Используем метод input_text из BasePage
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        # Используем метод input_text из BasePage
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login(self):
        # Используем метод click_element из BasePage
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Выполнить вход с email: {email} и паролем")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    @allure.step("Получить текст ошибки входа")
    def get_error_message(self):
        # Добавляем метод для получения текста ошибки
        return self.get_element_text(LoginPageLocators.ERROR_MESSAGE)

    @allure.step("Проверить наличие формы входа")
    def is_login_form_visible(self):
        # Добавляем проверку видимости формы
        return self.is_element_present(LoginPageLocators.LOGIN_FORM)

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента Заказов'")
    def click_order_feed_button(self):
        order_feed_button = self.wait_for_element_visible(MainPageLocators.ORDER_FEED_BUTTON)
        self.driver.execute_script("arguments[0].click();", order_feed_button)

    @allure.step("Кликнуть на кнопку 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.wait_for_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        counter_element = self.wait_for_element_visible(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter_element.text)

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        ingredient = self.wait_for_element_visible(MainPageLocators.INGREDIENT_ITEM)
        constructor_area = self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_AREA)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor_area).perform()

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Ожидать появления модального окна успешного заказа")
    def wait_for_order_success_modal(self):
        extended_wait = WebDriverWait(self.driver, 15)
        extended_wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_SUCCESS_MODAL))

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        close_button = self.wait_for_element_visible(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", close_button)

        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)

    @allure.step("Проверить отображение раздела 'Булки'")
    def is_buns_section_displayed(self):
        return self.find_element(MainPageLocators.BUNS_SECTION).is_displayed()
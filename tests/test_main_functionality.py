import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.suite("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))
        main_page.click_constructor_button()

        assert main_page.is_buns_section_displayed()

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        assert order_feed_page.is_order_feed_displayed()

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_ingredient_modal_opening(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()

        assert main_page.is_modal_visible()

    @allure.title("Закрытие всплывающего окна по клику на крестик")
    def test_ingredient_modal_closing(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.wait_for_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.title("Увеличение счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increase(self, driver, login):
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_constructor()

        counter = main_page.get_ingredient_counter()
        assert counter >= 0
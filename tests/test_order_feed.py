import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title("Проверка отображения счетчиков заказов")
    def test_total_orders_counter_displayed(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.wait_for_order_success_modal()
        main_page.close_order_modal()

        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        total_orders = order_feed_page.get_total_orders_count()
        today_orders = order_feed_page.get_today_orders_count()

        assert total_orders >= 0
        assert today_orders >= 0

    @allure.title("Проверка раздела 'В работе'")
    def test_orders_in_progress_section(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.wait_for_order_success_modal()
        main_page.close_order_modal()

        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        orders_in_progress = order_feed_page.get_orders_in_progress()
        assert orders_in_progress is not None

    @allure.title("Проверка навигации по ленте заказов")
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        assert order_feed_page.is_order_feed_displayed()
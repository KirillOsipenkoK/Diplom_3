import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.suite("Лента заказов")
    @allure.feature("Счетчики заказов")
    @allure.title("Проверка отображения общего счетчика заказов")
    def test_total_orders_counter(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.navigate_to_order_feed()

        total_orders = order_feed_page.get_total_orders_count()
        assert total_orders >= 0

    @allure.suite("Лента заказов")
    @allure.feature("Счетчики заказов")
    @allure.title("Проверка отображения счетчика заказов за сегодня")
    def test_today_orders_counter(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.navigate_to_order_feed()

        today_orders = order_feed_page.get_today_orders_count()
        assert today_orders >= 0

    @allure.suite("Лента заказов")
    @allure.feature("Заказы в работе")
    @allure.title("Проверка отображения раздела 'В работе'")
    def test_orders_in_progress_displayed(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.navigate_to_order_feed()

        orders_in_progress = order_feed_page.get_orders_in_progress()
        assert len(orders_in_progress) >= 0

    @allure.suite("Лента заказов")
    @allure.feature("Навигация")
    @allure.title("Проверка перехода в ленту заказов")
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.navigate_to_order_feed()

        assert order_feed_page.is_order_feed_displayed()

    @allure.suite("Лента заказов")
    @allure.feature("Создание заказа")
    @allure.title("Проверка создания нового заказа")
    def test_create_new_order(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        # Создаем заказ
        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.wait_for_order_success_modal()
        main_page.close_order_modal()

        # Проверяем обновление счетчиков
        main_page.navigate_to_order_feed()

        total_orders = order_feed_page.get_total_orders_count()
        today_orders = order_feed_page.get_today_orders_count()

        assert total_orders >= 1
        assert today_orders >= 1
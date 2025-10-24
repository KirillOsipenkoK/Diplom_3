import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Проверить отображение ленты заказов")
    def is_order_feed_displayed(self):
        # Используем метод из BasePage для проверки видимости
        return self.is_element_present(OrderFeedLocators.ORDER_FEED_SECTION)

    @allure.step("Получить количество заказов за все время")
    def get_total_orders_count(self):
        # Используем метод get_element_text из BasePage
        text = self.get_element_text(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(text)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        # Используем метод get_element_text из BasePage
        text = self.get_element_text(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(text)

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        # Используем метод find_elements из BasePage
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [elem.text for elem in elements]

    @allure.step("Проверить наличие новых заказов")
    def has_new_orders(self):
        # Добавляем дополнительную проверку
        return self.is_element_present(OrderFeedLocators.NEW_ORDER_INDICATOR)

    @allure.step("Получить статус последнего заказа")
    def get_last_order_status(self):
        # Добавляем метод для получения статуса последнего заказа
        status_element = self.find_element(OrderFeedLocators.LAST_ORDER_STATUS)
        return status_element.text

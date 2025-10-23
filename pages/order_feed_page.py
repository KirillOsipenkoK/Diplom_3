import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Проверить отображение ленты заказов")
    def is_order_feed_displayed(self):
        element = self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_SECTION)
        return element.is_displayed()

    @allure.step("Получить количество заказов за все время")
    def get_total_orders_count(self):
        element = self.wait_for_element_visible(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(element.text)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        element = self.wait_for_element_visible(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(element.text)

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [elem.text for elem in elements]
from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_SECTION = (By.XPATH, ".//h1[text()='Лента заказов']")
    TOTAL_ORDERS_COUNT = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "[class*='OrderFeed_orderListReady__'] li")
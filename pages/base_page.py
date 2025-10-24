import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Таймаут по умолчанию 10 секунд
        self.logger = logging.getLogger(__name__)

    @allure.step("Найти элемент по локатору {locator}")
    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Элемент не найден: {locator}")
            raise

    @allure.step("Ожидать появления URL, содержащего {url_part}")
    def wait_for_url_contains(self, url_part):
        try:
            self.wait.until(lambda driver: url_part in driver.current_url)
        except TimeoutException:
            raise Exception(f"URL не содержит ожидаемую часть: {url_part}")

    @allure.step("Проверить невидимость элемента {locator}")
    def is_element_invisible(self, locator):
        try:
            return self.wait_for_element_invisible(locator) is not None
        except TimeoutException:
            return False

    @allure.step("Найти все элементы по локатору {locator}")
    def find_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Элементы не найдены: {locator}")
            raise

    @allure.step("Кликнуть на элемент по локатору {locator}")
    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            self.logger.error(f"Элемент не стал кликабельным: {locator}")
            raise
        except Exception as e:
            self.logger.error(f"Ошибка при клике: {str(e)}")
            raise

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Элемент не стал видимым: {locator}")
            raise

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_element_invisible(self, locator):
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Элемент не исчез: {locator}")
            raise

    @allure.step("Ввести текст в поле {locator}")
    def input_text(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.error(f"Ошибка при вводе текста: {str(e)}")
            raise

    @allure.step("Получить текст элемента {locator}")
    def get_element_text(self, locator):
        try:
            element = self.find_element(locator)
            return element.text
        except Exception as e:
            self.logger.error(f"Ошибка при получении текста: {str(e)}")
            raise

    @allure.step("Проверить наличие элемента {locator}")
    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    @allure.step("Получить атрибут элемента {locator}")
    def get_attribute(self, locator, attribute_name):
        try:
            element = self.find_element(locator)
            return element.get_attribute(attribute_name)
        except Exception as e:
            self.logger.error(f"Ошибка при получении атрибута: {str(e)}")
            raise
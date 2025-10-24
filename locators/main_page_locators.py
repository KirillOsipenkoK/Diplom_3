from selenium.webdriver.common.by import By


class MainPageLocators:
    # Основные кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    # Ингредиенты
    INGREDIENT = (By.CSS_SELECTOR, "[class*='BurgerIngredient_ingredient__']")
    INGREDIENT_ITEM = (By.CSS_SELECTOR, "[class*='BurgerIngredient_ingredient__']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter__num__']")

    # Конструктор
    CONSTRUCTOR_AREA = (By.CSS_SELECTOR, "[class*='BurgerConstructor_basket__']")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # Модальные окна
    INGREDIENT_DETAILS_MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal__container__']")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay__']")
    ORDER_SUCCESS_MODAL = (By.CSS_SELECTOR, "h2[class*='Modal_modal__title__']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class*='Modal_modal__close__']")

    # Разделы
    BUNS_SECTION = (By.XPATH, ".//h2[text()='Булки']")
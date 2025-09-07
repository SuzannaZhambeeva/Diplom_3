# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from locators import MainPageLocators


# class MainPage:
#     URL = "https://stellarburgers.nomoreparties.site"  # ← сюда свой реальный адрес

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 20)
#         self.actions = ActionChains(driver)

#     def open(self):
#         self.driver.get(self.URL)
#         # Ждём полной загрузки страницы
#         self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#     # ===== Авторизация =====
#     def login(self, email, password):
#         """Логин пользователя через UI"""
#         self.go_to_account()

#         email_field = self.wait.until(
#             EC.visibility_of_element_located(("name", "name"))
#         )
#         password_field = self.wait.until(
#             EC.visibility_of_element_located(("name", "Пароль"))
#         )
#         email_field.clear()
#         email_field.send_keys(email)
#         password_field.clear()
#         password_field.send_keys(password)

#         enter_button = self.wait.until(
#             EC.element_to_be_clickable(("xpath", "//button[text()='Войти']"))
#         )
#         enter_button.click()

#     # ===== Навигация =====
#     def go_to_account(self):
#         account_link = self.wait.until(
#             EC.element_to_be_clickable(MainPageLocators.ACCOUNT_LINK)
#         )
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", account_link)
#         self.actions.move_to_element(account_link).click().perform()

#     def go_to_order_feed(self):
#         order_feed_link = self.wait.until(
#             EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_LINK)
#         )
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", order_feed_link)
#         self.actions.move_to_element(order_feed_link).click().perform()

#     def go_to_constructor(self):
#         constructor_button = self.wait.until(
#             EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
#         )
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", constructor_button)
#         self.actions.move_to_element(constructor_button).click().perform()

#     # ===== Работа с ингредиентами =====
#     def add_first_ingredient_to_burger(self):
#         ingredient = self.wait.until(
#             EC.visibility_of_element_located(MainPageLocators.INGREDIENT_ITEM)
#         )
#         constructor_area = self.wait.until(
#             EC.visibility_of_element_located(MainPageLocators.BURGER_CONSTRUCTOR_AREA)
#         )
#         # drag-and-drop через ActionChains (стабильно для Firefox и Chrome)
#         self.actions.click_and_hold(ingredient).move_to_element(constructor_area).release().perform()

#     # ===== Создание заказа =====
#     def make_order(self, user):
#         order_button = self.wait.until(
#             EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
#         )
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
#         self.actions.move_to_element(order_button).click().perform()

#         # ждём модальное окно с номером заказа
#         self.wait.until(
#             EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER)
#         )

#     # ===== Вспомогательные =====
#     def click_first_ingredient(self):
#         """Открытие модального окна с деталями ингредиента"""
#         ingredient = self.wait.until(
#             EC.element_to_be_clickable(MainPageLocators.INGREDIENT_ITEM)
#         )
#         self.actions.move_to_element(ingredient).click().perform()
#         self.wait.until(
#             EC.visibility_of_element_located(MainPageLocators.MODAL_INGREDIENT_DETAILS)
#         )

#     def close_ingredient_modal(self):
#         close_button = self.wait.until(
#             EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
#         )
#         close_button.click()
#         self.wait.until(
#             EC.invisibility_of_element_located(MainPageLocators.MODAL_INGREDIENT_DETAILS)
#         )

# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from locators import MainPageLocators
# # from pages.login_page import LoginPage

# # class MainPage:
# #     def __init__(self, driver):
# #         self.driver = driver
# #         self.wait = WebDriverWait(driver, 10)

# #     def go_to_account(self):
# #         account_link = self.wait.until(
# #             EC.element_to_be_clickable(MainPageLocators.ACCOUNT_LINK)
# #         )
# #         account_link.click()

# #     def login(self, email, password):
# #         login_page = LoginPage(self.driver)
# #         login_page.open()
# #         login_page.login(email, password)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage


class MainPage:
    URL = "https://stellarburgers.nomoreparties.site"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    # ===== Открытие страницы =====
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # ===== Авторизация =====
    def login(self, email, password):
        """
        Логин пользователя через UI.
        Использует LoginPage для заполнения полей.
        """
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(email, password)

    # ===== Навигация =====
    def go_to_account(self):
        """
        Переход в Личный кабинет.
        Возвращает объект AccountPage для работы с аккаунтом.
        """
        account_link = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", account_link)
        self.actions.move_to_element(account_link).click().perform()
        return AccountPage(self.driver)

    def go_to_order_feed(self):
        """
        Переход в ленту заказов.
        """
        order_feed_link = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_feed_link)
        self.actions.move_to_element(order_feed_link).click().perform()

    def go_to_constructor(self):
        """
        Переход в конструктор бургеров.
        """
        constructor_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", constructor_button)
        self.actions.move_to_element(constructor_button).click().perform()

    # ===== Работа с ингредиентами =====
    def click_first_ingredient(self):
        """
        Открытие модального окна с деталями ингредиента.
        """
        ingredient = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT_ITEM)
        )
        self.actions.move_to_element(ingredient).click().perform()
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.MODAL_INGREDIENT_DETAILS)
        )

    def close_ingredient_modal(self):
        """
        Закрытие модального окна ингредиента.
        """
        close_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        )
        close_button.click()
        self.wait.until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_INGREDIENT_DETAILS)
        )

    def drag_first_ingredient_to_constructor(self):
        """
        Добавление первого ингредиента в конструктор методом drag-and-drop.
        """
        ingredient = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_ITEM)
        )
        constructor_area = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.BURGER_CONSTRUCTOR_AREA)
        )
        self.actions.click_and_hold(ingredient).move_to_element(constructor_area).release().perform()

    def get_first_ingredient_counter(self):
        """
        Возвращает количество добавленного ингредиента (каунтер).
        """
        counter_elem = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER)
        )
        return int(counter_elem.text)

    # ===== Создание заказа =====
    def click_order_button(self):
        """
        Клик по кнопке 'Оформить заказ'.
        """
        order_btn = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        order_btn.click()

    def make_order(self):
        """
        Ждём модальное окно с номером заказа после оформления.
        """
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL_WINDOW)
        )

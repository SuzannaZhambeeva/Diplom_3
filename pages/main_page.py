from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Переход в личный кабинет")
    def open_account(self):
        self.click_element(MainPageLocators.ACCOUNT_LINK)
    
    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_ITEM)
    
    @allure.step("Переход в ленту заказов")
    def open_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)
    
    @allure.step("Переход в конструктор")
    def open_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Закрытие модального окна")
    def close_modal(self, locator):
        self.click_element(locator)

    @allure.step("Закрытие модального окна через JS")
    def close_modal_js(self, locator):
        self.click_js(locator)
    
    @allure.step("Проверка открытия модального окна")
    def is_modal_open(self, locator):
        return self.wait_until_visible(locator).is_displayed()

    @allure.step("Проверка закрытия модального окна")
    def is_modal_closed(self, locator):
        return self.wait_until_invisible(locator)

    @allure.step("Выбор ингредиента в конструктор")
    def drag_ingredient_to_burger(self):
        source = self.wait_until_visible(MainPageLocators.INGREDIENT_ITEM)
        target = self.wait_until_visible(MainPageLocators.BURGER_CONSTRUCTOR)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        
    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_ingredient_to_burger()

    @allure.step("Оформление заказа")
    def place_order(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self):
        count = self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)
        return int(count)
    
    @allure.step("Получение номера заказа из модалки")
    def get_order_number(self):
        return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Закрытие модалки заказа и ожидание её исчезновения")
    def close_order_modal_and_wait(self):
        self.click_element(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        self.wait_until_invisible(MainPageLocators.MODAL_OVERLAY)


class ProfilePage(BasePage):

    @allure.step("Переход в историю заказов")
    def go_to_order_history(self):
        self.click_element(MainPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click_element(MainPageLocators.LOGOUT_BUTTON)

    
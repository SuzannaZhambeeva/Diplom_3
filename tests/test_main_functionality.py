import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from pages.main_page import MainPage


@allure.feature("Проверка основного функционала")
class TestMainFunctionality:

    @allure.story("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)

        main_page.go_to_constructor()
        main_page.wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))

        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    @allure.story("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)

        main_page.go_to_order_feed()
        main_page.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_FEED_LINK))

        assert driver.find_element(*MainPageLocators.ORDER_FEED_LINK).is_displayed()

    @allure.story("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_open_ingredient_modal(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)

        main_page.click_first_ingredient()
        main_page.wait.until(EC.visibility_of_element_located(MainPageLocators.MODAL_INGREDIENT_DETAILS))

        assert driver.find_element(*MainPageLocators.MODAL_INGREDIENT_DETAILS).is_displayed()

    @allure.story("Закрытие всплывающего окна кликом по крестику")
    def test_close_ingredient_modal(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)

        main_page.click_first_ingredient()
        close_button = main_page.wait.until(EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON))
        close_button.click()

        main_page.wait.until(EC.invisibility_of_element_located(MainPageLocators.MODAL_INGREDIENT_DETAILS))

    @allure.story("При добавлении ингредиента увеличивается каунтер")
    def test_add_ingredient_increases_counter(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)

        before = main_page.get_first_ingredient_counter()
        main_page.drag_first_ingredient_to_constructor()
        after = main_page.get_first_ingredient_counter()

        assert after == before + 1, f"Ожидалось {before+1}, но получено {after}"

    @allure.story("Залогиненный пользователь может оформить заказ")
    @pytest.mark.usefixtures("user")
    def test_logged_in_user_can_make_order(self, driver, user):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)

        # Логин
        main_page.login(user["email"], user["password"])

        # Добавляем ингредиент в заказ
        main_page.drag_first_ingredient_to_constructor()

        # Оформляем заказ
        main_page.click_order_button()
        main_page.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL_WINDOW))

        assert driver.find_element(*MainPageLocators.ORDER_MODAL_WINDOW).is_displayed()

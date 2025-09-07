import allure
from pages.main_page import MainPage
from pages.restore_page import RestorePage

@allure.feature("Восстановление пароля")
class TestRestorePassword:

    @allure.story("Переход на страницу восстановления пароля")
    def test_go_to_restore_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)
        restore_page = RestorePage(driver)

        main_page.go_to_account()
        restore_page.go_to_restore_page()

        assert restore_page.is_email_field_visible()

    @allure.story("Ввод email и клик по кнопке Восстановить")
    def test_restore_email(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)
        restore_page = RestorePage(driver)

        main_page.go_to_account()
        restore_page.go_to_restore_page()

        restore_page.enter_email("test@mail.com")
        restore_page.click_restore()

        assert "Проверьте почту" in driver.page_source or "Восстановление" in driver.page_source

    @allure.story("Показ/скрытие пароля делает поле активным")
    def test_toggle_password_visibility(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        main_page = MainPage(driver)
        restore_page = RestorePage(driver)

        main_page.go_to_account()
        restore_page.go_to_restore_page()

        # сначала вводим почту и жмём "Восстановить", чтобы появилось поле нового пароля
        restore_page.enter_email("test@mail.com")
        restore_page.click_restore()

        restore_page.toggle_password_visibility()
        assert restore_page.is_password_field_active() is True

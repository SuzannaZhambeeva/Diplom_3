import allure
from pages.base_page import BasePage
from locators import LoginPageLocators, RestorePageLocators


class LoginPage(BasePage):

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.input_text(LoginPageLocators.LOGIN_EMAIL, email)
        self.input_text(LoginPageLocators.LOGIN_PASSWORD, password)
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Переход на страницу восстановления пароля")
    def restore_password(self):
        self.click_element(RestorePageLocators.PASSWORD_RESTORE)

class RestorePasswordPage(BasePage):

    @allure.step("Ввод email для восстановления")
    def enter_email(self, email):
        self.input_text(RestorePageLocators.EMAIL_FIELD, email)

    @allure.step("Нажатие по кнопке 'Восстановить'")
    def click_recover(self):
        self.click_element(RestorePageLocators.RESTORE_BUTTON)

    @allure.step("Нажатие по кнопке показать/скрыть пароль")
    def click_show_hide_password(self):
        self.click_element(RestorePageLocators.VISIBILITY_PASSWORD)

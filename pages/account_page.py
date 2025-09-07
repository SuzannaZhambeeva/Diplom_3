# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from locators import AccountPageLocators


# class AccountPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)

#     def go_to_order_history(self):
#         """Переход в раздел История заказов"""
#         order_history_tab = self.wait.until(
#             EC.element_to_be_clickable(AccountPageLocators.ORDER_HISTORY_TAB)
#         )
#         order_history_tab.click()
#         # Ждём, пока вкладка станет видимой
#         self.wait.until(
#             EC.visibility_of_element_located(AccountPageLocators.ORDER_HISTORY_TAB)
#         )

#     def logout(self):
#         """Выход из аккаунта"""
#         logout_button = self.wait.until(
#             EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
#         )
#         logout_button.click()
#         # Ждём, пока кнопка "Выход" исчезнет, что подтверждает выход
#         self.wait.until(
#             EC.invisibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
#         )
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AccountPageLocators

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_order_history(self):
        tab = self.wait.until(
            EC.element_to_be_clickable(AccountPageLocators.ORDER_HISTORY_TAB)
        )
        tab.click()
        # Ждём, пока вкладка активна
        self.wait.until(
            EC.visibility_of_element_located(AccountPageLocators.ORDER_HISTORY_TAB)
        )

    def logout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        button.click()
        # Ждём, пока кнопка "Выход" исчезнет
        self.wait.until(
            EC.invisibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        )

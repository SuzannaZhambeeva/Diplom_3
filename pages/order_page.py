import allure
from pages.base_page import BasePage
from locators import MainPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Клик по заказу")
    def click_order(self):
        self.click_element(MainPageLocators.ORDER_ITEM)

    @allure.step("Проверка открытия модального окна с деталями")
    def is_modal_open(self, locator):
        return self.wait_until_visible(locator).is_displayed()
    
    @allure.step("Получение значения счетчика 'Выполнено за всё время'")
    def get_total_completed(self):
        return int(self.get_element_text(MainPageLocators.TOTAL_COMPLETED))

    @allure.step("Получение номера заказа в разделе 'В работе'")
    def get_in_progress_order_number(self, locator):
        return self.get_element_text(locator)
    
    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_completed(self):
        return int(self.get_element_text(MainPageLocators.TODAY_COMPLETED))

    # @allure.step("Получение текста заказа из модального окна")
    # def get_order_number_from_modal(self):
    #     return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    # @allure.step("Список заказов 'В работе'")
    # def get_orders_in_progress(self):
    #     elements = self.driver.find_elements(*MainPageLocators.ORDER_NUMBER_IN_PROCCESS)
    #     return [el.text for el in elements]

    # @allure.step("Ожидание заказа в разделе 'В работе'")
    # def wait_for_order_in_progress(self, order_number, timeout=10):
    #     """Ждёт появления заказа с номером order_number в блоке 'В работе'"""
    #     self.wait.until(
    #         EC.text_to_be_present_in_element(MainPageLocators.ORDER_NUMBER_IN_PROCCESS, order_number)
    #     )
    #     return True

    @allure.step("Получение текста заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Список заказов 'В работе'")
    def get_orders_in_progress(self):
        elements = self.driver.find_elements(*MainPageLocators.ORDER_NUMBER_IN_PROCCESS)
        return [el.text for el in elements]

    @allure.step("Список заказов 'Готово'")
    def get_orders_ready(self):
        elements = self.driver.find_elements(*MainPageLocators.ORDER_ITEM)
        return [el.text for el in elements]
    
    @allure.step("Закрытие модалки заказа и ожидание её исчезновения")
    def close_order_modal_and_wait(self):
        self.click_element(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        self.wait_until_invisible(MainPageLocators.ORDER_WINDOW)
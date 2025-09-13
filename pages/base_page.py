from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        
    @allure.step("Поиск объекта")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_until_visible(locator)
        element.click()
    
    @allure.step("Ожидание появления элемента")
    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ввод текста в поле")
    def input_text(self, locator, text):
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator):
        element = self.wait_until_visible(locator)
        return element.text

    @allure.step("Получение значения атрибута элемента")
    def get_element_attribute(self, locator, attribute):
        element = self.wait_until_visible(locator)
        return element.get_attribute(attribute)
    
    @allure.step("Ожидание клика элемента")
    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

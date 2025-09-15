from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открытие страницы: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Поиск объекта")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_until_visible(locator)
        element.click()

    @allure.step("Клик по элементу через JS")
    def click_js(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание появления элемента")
    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание исчезновения элемента")
    def wait_until_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

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

    @allure.step("Закрытие модального окна через JS и ожидание исчезновения")
    def close_modal_js_and_wait(self, locator, overlay_locator):
        self.click_js(locator)
        self.wait_until_invisible(overlay_locator)

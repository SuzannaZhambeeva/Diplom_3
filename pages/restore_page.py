from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RestorePageLocators

class RestorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_restore_page(self):
        restore_link = self.wait.until(
            EC.element_to_be_clickable(RestorePageLocators.PASSWORD_RESTORE_LINK)
        )
        restore_link.click()

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located(RestorePageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

    def click_restore(self):
        restore_button = self.wait.until(
            EC.element_to_be_clickable(RestorePageLocators.RESTORE_BUTTON)
        )
        restore_button.click()

    def is_email_field_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(RestorePageLocators.EMAIL_FIELD)
        ).is_displayed()

    def toggle_password_visibility(self):
        # ждём появления поля "новый пароль"
        self.wait.until(EC.visibility_of_element_located(RestorePageLocators.NEW_PASSWORD_FIELD))
        visibility_button = self.wait.until(
            EC.element_to_be_clickable(RestorePageLocators.VISIBILITY_PASSWORD_BUTTON)
        )
        visibility_button.click()

    def is_password_field_active(self):
        new_password_field = self.wait.until(
            EC.visibility_of_element_located(RestorePageLocators.NEW_PASSWORD_FIELD)
        )
        return new_password_field.is_enabled()

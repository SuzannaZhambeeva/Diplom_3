from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageLocators:
    LOGIN_EMAIL_FIELD = (By.NAME, "name")
    LOGIN_PASSWORD_FIELD = (By.NAME, "Пароль")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://stellarburgers.nomoreparties.site/login"

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_EMAIL_FIELD)).send_keys(email)
        self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()

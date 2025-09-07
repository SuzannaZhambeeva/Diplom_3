import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

API_URL = "https://stellarburgers.nomoreparties.site/api/auth"


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def driver(request):
    """Фикстура для кроссбраузерного тестирования"""
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options, service=ChromeService())
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options, service=FirefoxService())
    else:
        raise ValueError(f"Неизвестный браузер: {browser}")

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def user():
    """Фикстура для регистрации и удаления пользователя"""
    email = "testuser_flow@yandex.ru"
    password = "123456"
    name = "TestUser"

    # Создание пользователя через API
    requests.post(f"{API_URL}/register", json={
        "email": email,
        "password": password,
        "name": name
    })

    yield {"email": email, "password": password}

    # Удаление пользователя после теста
    token_response = requests.post(f"{API_URL}/login", json={
        "email": email,
        "password": password
    })
    if token_response.status_code == 200:
        access_token = token_response.json()["accessToken"]
        requests.delete(f"{API_URL}/user", headers={"Authorization": access_token})


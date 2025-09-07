import pytest
from pages.main_page import MainPage
from pages.account_page import AccountPage
from locators import AccountPageLocators
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver", "user")
def test_account_full_flow(driver, user):
    """
    Интеграционный тест:
    1. Логинимся
    2. Переходим в Личный кабинет
    3. Переходим в Историю заказов
    4. Выходим из аккаунта
    """

    main_page = MainPage(driver)
    account_page = AccountPage(driver)

    # 1️⃣ Логинимся
    main_page.login(user["email"], user["password"])

    # 2️⃣ Переход в Личный кабинет
    main_page.go_to_account()
    account_page.wait.until(
        EC.visibility_of_element_located(AccountPageLocators.PROFILE_TAB)
    )

    # 3️⃣ Переход в Историю заказов
    account_page.go_to_order_history()

    # 4️⃣ Выход из учётки
    account_page.logout()

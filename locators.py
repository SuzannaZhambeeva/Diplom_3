from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_BUTTON = (
        By.XPATH, 
        "//button[text()='Войти']"
    )
    LOGIN_EMAIL = (
        By.XPATH, 
        "//div[contains(@class, 'input_type_text')]/input[contains(@class, 'text_type_main-default')]"
    )
    LOGIN_PASSWORD = (
        By.XPATH, 
        "//div[contains(@class, 'input_type_password')]/input[contains(@class, 'text_type_main-default')]"
    )
    
  
class MainPageLocators:
    ACCOUNT_LINK = (
        By.XPATH, 
        "//a[@href='/account']"
    )
    BURGER_CONSTRUCTOR = (
        By.XPATH, 
        "//div[contains(@class, 'constructor-element_pos_top')]"
    )
    CONSTRUCTOR_BUTTON = (
        By.XPATH, 
        "//p[text() = 'Конструктор']"
    )
    INGREDIENT_COUNTER = (
        By.XPATH, 
        "//div[contains (@class, 'counter_default__28sqi')]//p"
    )
    INGREDIENT_ITEM = (
        By.XPATH, 
        "//div[contains(@class, 'BurgerIngredient_ingredient')]"
    )
    LOGOUT_BUTTON = (
        By.XPATH, 
        "//nav[contains(@class, 'Account_nav')]/ul/li/button[text()='Выход']"
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH, 
        "//button[contains(@class, 'Modal_modal__close')]"
    )
    MODAL_INGREDIENT = (
        By.XPATH, 
        "//h2[text() = 'Детали ингредиента']"
    )
    MODAL_OVERLAY = (
        By.XPATH, 
        "//div[contains(@class, 'Modal_modal')]/img[contains(@src, 'loading')]"
    )
    ORDER_BUTTON = (
        By.XPATH, 
        f"//button[text()='Оформить заказ']"
    )
    ORDER_FEED_LINK = (
        By.XPATH, 
        "//a[@href='/feed']/p"
    )
    ORDER_HISTORY_BUTTON = (
        By.XPATH, 
        "//a[@href = '/account/order-history']"
    )
    ORDER_ITEM_IN_HISTORY = (
        By.XPATH, 
        "//div/ul/li[contains(@class, 'OrderHistory_listItem')][last()]/a/div/p"
    )
    ORDER_ITEM = (
        By.XPATH, 
        "//div[contains(@class, 'OrderFeed_contentBox')]/ul/li/a/div/p"
    )
    ORDER_MODAL_WINDOW = (
        By.XPATH, 
        "//div[contains (@class, 'Modal_modal__contentBox__sCy8X')]"
    )
    ORDER_NUMBER = (
        By.XPATH, 
        "//div[contains(@class, 'Modal_modal__contentBox')]/h2"
    )
    ORDER_NUMBER_IN_PROCCESS = (
        By.XPATH, 
        "//ul[contains(@class, 'OrderFeed_orderListInWork')]/li"
    )

    ORDER_WINDOW = (
        By.XPATH, 
        "//div[contains(@class, 'Modal_modal__container')]/div/h2[text() ='Флюоресцентный бургер']"
    )
    ORDER_WINDOW_CLOSE_BUTTON = (
        By.XPATH, 
        "//div[contains(@class, 'Modal_modal__container')]/button[contains(@class, 'Modal_modal__close')]"
    )
    TODAY_COMPLETED = (
        By.XPATH, 
        "//p[text()='Выполнено за сегодня:']//following-sibling::p"
    )
    TOTAL_COMPLETED = (
        By.XPATH, 
        "//p[text()='Выполнено за все время:']//following-sibling::p"
    )

    
class RestorePageLocators:
    EMAIL_FIELD = (
        By.XPATH,
        "//div[contains(@class, 'input_size_default')]/input[@name = 'name']"
    )
    NEW_PASSWORD_FIELD = (
        By.XPATH, 
        "//input[@name = 'Введите новый пароль']"
    )
    
    NEW_PASSWORD = (
        By.XPATH, 
        "//div[@class = 'input__container']/div[contains(@class, 'input_size_default')]"
    )
    PASSWORD_RESTORE = (
        By.XPATH, 
        "//a[text()='Восстановить пароль']"
    )
    RESTORE_BUTTON = (
        By.XPATH, 
        "//button[text()='Восстановить']"
    )
    VISIBILITY_PASSWORD = (
        By.XPATH, 
        "//div[contains(@class, 'input__icon-action')]/*[local-name()='svg']"
        )
    
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL_FIELD = (By.NAME, "name")
    LOGIN_PASSWORD_FIELD = (By.NAME, "Пароль")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
  
class MainPageLocators:
    ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']/p")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains (@class, 'counter_default__28sqi')]//p")
    ORDER_BUTTON = (By.XPATH, f"//button[text()='Оформить заказ']")
    MODAL_INGREDIENT_DETAILS = (By.XPATH, "//h2[text() = 'Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_MODAL_WINDOW = (By.XPATH, "//div[contains (@class, 'Modal_modal__contentBox__sCy8X')]")
    ORDER_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]/div/h2[text() ='Флюоресцентный бургер']")
    ORDER_WINDOW_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]/button[contains(@class, 'Modal_modal__close')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal')]/img[contains(@src, 'loading')]")
    BURGER_CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    ORDER_ITEM_IN_HISTORY = (By.XPATH, "//div/ul/li[contains(@class, 'OrderHistory_listItem')][last()]/a/div/p")
    TOTAL_COMPLETED = (By.XPATH, "//p[text()='Выполнено за все время:']//following-sibling::p")
    TODAY_COMPLETED = (By.XPATH, "//p[text()='Выполнено за сегодня:']//following-sibling::p")
    ORDER_ITEM = (By.XPATH, "//div[contains(@class, 'OrderFeed_contentBox')]/ul/li/a/div/p")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]/h2")
    ORDER_NUMBER_IN_PROCCESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text')]")
    
# class MainPageLocators:
#     ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
#     ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']/p")
#     CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")
#     INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
#     INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class,'counter_default__28sqi')]//p")
#     ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
#     MODAL_INGREDIENT_DETAILS = (By.XPATH, "//h2[text() = 'Детали ингредиента']")
#     MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
#     ORDER_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]/div/h2[text() ='Флюоресцентный бургер']")
#     ORDER_WINDOW_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]/button[contains(@class,'Modal_modal__close')]")
#     MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal')]/img[contains(@src, 'loading')]")
#     BURGER_CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
#     ORDER_ITEM_IN_HISTORY = (By.XPATH, "//div/ul/li[contains(@class, 'OrderHistory_listItem')][last()]/a/div/p")
#     TOTAL_COMPLETED = (By.XPATH, "//p[text()='Выполнено за все время:']//following-sibling::p")
#     TODAY_COMPLETED = (By.XPATH, "//p[text()='Выполнено за сегодня:']//following-sibling::p")
#     ORDER_ITEM = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem')]")
#     ORDER_MODAL_WINDOW_FEED = (By.CSS_SELECTOR, "div.OrderFeed_modal__content__3R-3G")
#     ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]/h2")
#     ORDER_NUMBER_IN_PROCCESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]/li[contains(@class,'text')]")

# class MainPageLocators:
#     ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
#     ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']/p")
#     CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
#     INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
#     INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class,'counter_default__28sqi')]//p")
#     ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
#     MODAL_INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
#     MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    
#     # Универсальное модальное окно заказа
#     ORDER_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]//h2")
#     ORDER_WINDOW_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]//button[contains(@class,'Modal_modal__close')]")
#     MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//img[contains(@src, 'loading')]")
    
#     BURGER_CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class,'constructor-element_pos_top')]")
    
#     # История заказов
#     ORDER_ITEM_IN_HISTORY = (By.XPATH, "//div/ul/li[contains(@class,'OrderHistory_listItem')][last()]/a/div/p")
    
#     # Счётчики в ленте заказов
#     TOTAL_COMPLETED = (By.XPATH, "//p[text()='Выполнено за все время:']//following-sibling::p")
#     TODAY_COMPLETED = (By.XPATH, "//p[text()='Выполнено за сегодня:']//following-sibling::p")
    
#     # Заказы в ленте
#     ORDER_ITEM = (By.XPATH, "//div[contains(@class,'OrderFeed_contentBox')]/ul/li")
    
#     ORDER_NUMBER = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]/h2")
#     ORDER_NUMBER_IN_PROCCESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]/li[contains(@class,'text')]")

class RestorePageLocators:
    PASSWORD_RESTORE_LINK = (By.LINK_TEXT, "Восстановить пароль")
    ACCOUNT_LINK = (By.LINK_TEXT, "Личный Кабинет")
    #ACCOUNT_LINK = (By.XPATH, "//a[@href='/account' and .//p[text()='Личный Кабинет']]")
    EMAIL_FIELD = (By.XPATH, "//div[contains(@class, 'input_size_default')]/input[@name = 'name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    NEW_PASSWORD_FIELD = (By.XPATH, "//input[@name = 'Введите новый пароль']")
    NEW_PASSWORD = (By.XPATH, "//div[@class = 'input__container']/div[contains(@class, 'input_size_default')]")
    VISIBILITY_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]/*[local-name()='svg']")

class AccountPageLocators:
    PROFILE_TAB = (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY_TITLE = (By.XPATH, "//h2[contains(text(),'История заказов')]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ACCOUNT_LINK = (By.XPATH, "//a[@href='/account' and .//p[text()='Личный Кабинет']]")

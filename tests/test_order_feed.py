import allure
from urls import Urls
from locators import MainPageLocators
from data import get_existing_user
from pages.main_page import MainPage, ProfilePage
from pages.login_page import LoginPage
from pages.order_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Открытие деталей заказа")
    def test_order_details(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open(Urls.ROOT)
        main_page.open_account()
        login_page.login(email, password)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.open(Urls.ORDER_FEED)
        order_feed_page.click_order()
        assert order_feed_page.is_modal_open(MainPageLocators.ORDER_WINDOW)

    @allure.title("Заказы из истории отображаются в ленте заказов")
    def test_orders_in_feed(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open(Urls.ROOT)
        main_page.open_account()
        login_page.login(email, password)
        main_page.add_ingredient_to_order()
        main_page.place_order()

        main_page.close_modal_js(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        main_page.wait_until_invisible(MainPageLocators.MODAL_OVERLAY)

        main_page.open_account()
        profile_page.go_to_order_history()
        history_order = profile_page.get_element_text(MainPageLocators.ORDER_ITEM_IN_HISTORY)

        main_page.open_order_feed()
        in_progress_orders = order_feed_page.get_in_progress_order_number(MainPageLocators.ORDER_ITEM)
        assert history_order == in_progress_orders, \
            f"Номер заказа {history_order} не найден в ленте заказов"

    @allure.title("Увеличение счетчика 'Выполнено за всё время'")
    def test_total_completed_counter(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open(Urls.ROOT)
        main_page.open_account()
        login_page.login(email, password)
        main_page.open_order_feed()
        initial_total = order_feed_page.get_total_completed()

        main_page.open(Urls.ROOT)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_modal_js(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        main_page.wait_until_invisible(MainPageLocators.MODAL_OVERLAY)

        main_page.open_order_feed()
        assert order_feed_page.get_total_completed() > initial_total

    @allure.title("Увеличение счетчика 'Выполнено за сегодня'")
    def test_today_completed_counter(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open(Urls.ROOT)
        main_page.open_account()
        login_page.login(email, password)
        main_page.open_order_feed()
        initial_today = order_feed_page.get_today_completed()

        main_page.open(Urls.ROOT)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_modal_js(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        main_page.wait_until_invisible(MainPageLocators.MODAL_OVERLAY)

        main_page.open_order_feed()
        assert order_feed_page.get_today_completed() > initial_today

    @allure.title("Номер заказа в разделе 'В работе'") 
    def test_order_in_progress(self, driver): 
        email, password = get_existing_user() 
        main_page = MainPage(driver) 
        login_page = LoginPage(driver) 
        order_feed_page = OrderFeedPage(driver) 
        main_page.open(Urls.ROOT) 
        main_page.open_account() 
        login_page.login(email, password) 
        main_page.add_ingredient_to_order() 
        main_page.place_order() 
        order_number = main_page.get_order_number() 
        main_page.close_order_modal_and_wait() 
        main_page.open_order_feed() 
        in_progress_number = order_feed_page.get_in_progress_order_number(MainPageLocators.ORDER_NUMBER_IN_PROCCESS) 
        assert in_progress_number == f"0{order_number}", f"Ожидался {order_number}, найден {in_progress_number}"

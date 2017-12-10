from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from locators import SearchPageLocators
from locators import LocationPageLocators
from locators import HomePageLocators
from selenium.webdriver.common.keys import Keys
from locators import URLS
import time

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):

    def is_balance_zero(self):
        order_total = self.driver.find_element(*HomePageLocators.order_total).text
        return "$0.00" == order_total

    def is_language_french(self):
        language_select = self.driver.find_element(*HomePageLocators.french_button)
        language_select.click()
        not_current_language = self.driver.find_element(*HomePageLocators.change_language_button).text
        return  not_current_language == 'EN'

    def can_search_for_item(self):
        search_bar = self.driver.find_element(*HomePageLocators.search_bar)
        search_bar.clear()
        search_bar.send_keys('APPLES')
        search_bar.send_keys(Keys.RETURN)
        search_results = self.driver.find_element(*HomePageLocators.search_results).text
        return 'APPLES' in search_results

class SearchPage(BasePage):

    def is_home_page(self):
        home_button = self.driver.find_element(*SearchPageLocators.home_button)
        home_button.click()
        return self.driver.current_url == 'https://www.loblaws.ca/'

    def is_item_list_sorted(self):
        sort_prices_desc = self.driver.find_element(*SearchPageLocators.sort_prices_desc)
        sort_prices_desc.click()
        list_of_prices = []
        all_prices = self.driver.find_elements(*SearchPageLocators.all_prices)
        for price in all_prices:
            list_of_prices.append(float(price.text.replace("$", "")))
        return sorted(list_of_prices, reverse=True) == list_of_prices

    def is_item_in_cart(self):
        add_to_cart = self.driver.find_element(*SearchPageLocators.add_to_cart)
        add_to_cart.click()
        pick_store = self.driver.find_element(*SearchPageLocators.pick_store)
        pick_store.click()
        location_button = self.driver.find_element(*SearchPageLocators.location_button)
        location_button.click()
        add_to_cart = self.driver.find_element(*SearchPageLocators.add_to_cart)
        add_to_cart.click()
        my_item_price = self.driver.find_element(*SearchPageLocators.my_item).text
        order_total = self.driver.find_element(*SearchPageLocators.order_total).text
        return my_item_price in order_total

    def is_checkout_working(self):
        checkout_button = self.driver.find_element(*SearchPageLocators.checkout_button)
        checkout_button.click()
        shopping_cart_status = self.driver.find_element(*HomePageLocators.shopping_cart_status).text
        return 'YOUR CART IS EMPTY' in shopping_cart_status

class LocationPage(BasePage):

    def is_location_correct(self):
        location_button = self.driver.find_element(*LocationPageLocators.location_button)
        store_address = self.driver.find_element(*LocationPageLocators.store_address).text
        location_button.click()
        my_store = self.driver.find_element(*LocationPageLocators.my_store).text
        return my_store in store_address

    def can_search_for_store(self):
        store_search_bar = self.driver.find_element(*LocationPageLocators.store_search_bar)
        store_search_bar.send_keys('EDMONTON')
        store_search_bar.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(LocationPageLocators.store_address))
        store_address = self.driver.find_element(*LocationPageLocators.store_address).text
        return 'EDMONTON' in store_address
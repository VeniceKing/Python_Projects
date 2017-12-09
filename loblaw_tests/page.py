from locators import SearchPageLocators
from locators import LocationPageLocators
from locators import HomePageLocators
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

class SearchPage(BasePage):

    def is_balance_zero(self):
        element = self.driver.find_element(*SearchPageLocators.order_total)
        element = element.text
        return "$0.00" == element

    def is_item_list_sorted(self):
        element = []
        list_of_prices = self.driver.find_elements(*SearchPageLocators.all_prices)
        for price in list_of_prices:
            element.append(float(price.text.replace("$", "")))
        return sorted(element, reverse=True) == element

    def is_item_in_cart(self):
        item_select = self.driver.find_element(*SearchPageLocators.add_to_cart)
        item_select.click()
        check_map = self.driver.find_element(*SearchPageLocators.pick_store)
        check_map.click()
        location_select = self.driver.find_element(*SearchPageLocators.location_button)
        location_select.click()
        item_select = self.driver.find_element(*SearchPageLocators.add_to_cart)
        item_select.click()
        item_price = self.driver.find_element(*SearchPageLocators.my_item).text
        order_total = self.driver.find_element(*SearchPageLocators.order_total).text
        return item_price in order_total      

class LocationPage(BasePage):

    def is_location_correct(self):
        location_select = self.driver.find_element(*LocationPageLocators.location_button)
        store_description = self.driver.find_element(*LocationPageLocators.store_address).text
        location_select.click()
        my_store = self.driver.find_element(*LocationPageLocators.store_display).text
        return my_store in store_description

class HomePage(BasePage):

    def is_language_french(self):
        language_select = self.driver.find_element(*HomePageLocators.french_button)
        language_select.click()
        not_current_language = self.driver.find_element(*HomePageLocators.change_language_button).text
        return  not_current_language == 'EN'

    def can_search_for_item(self):
        input_box = self.driver.find_element(*HomePageLocators.search_bar)
        input_box.clear()
        input_box.send_keys("APPLES")
        input_box.send_keys(Keys.RETURN)
        search_results = self.driver.find_element(*HomePageLocators.search_result).text
        return 'APPLES' in search_results
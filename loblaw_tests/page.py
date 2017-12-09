from locators import SearchPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

class SearchPage(BasePage):

    def is_balance_zero(self):
        element = self.driver.find_element_by_xpath(SearchPageLocators.order_total).text
        return "$0.00" == element

    def is_item_list_sorted(self):
        element = []
        list_of_prices = self.driver.find_elements_by_xpath(SearchPageLocators.all_prices)
        for price in list_of_prices:
            element.append(float(price.text.replace("$", "")))
        return sorted(element, reverse=True) == element

    def is_item_in_cart(self):
        item_select = self.driver.find_element_by_xpath(SearchPageLocators.add_to_cart)
        item_select.click()
        check_map = self.driver.find_element_by_xpath(SearchPageLocators.pick_store)
        check_map.click()
        location_select = self.driver.find_element_by_xpath(SearchPageLocators.location_button)
        location_select.click()
        item_select = self.driver.find_element_by_xpath(SearchPageLocators.add_to_cart)
        item_select.click()
        item_price = self.driver.find_element_by_xpath(SearchPageLocators.my_item).text
        order_total = self.driver.find_element_by_xpath(SearchPageLocators.order_total).text
        return item_price in order_total      

class LocationPage(BasePage):

    def is_location_correct(self):
        location_select = self.driver.find_element_by_xpath(LocationPageLocators.location_button)
        store_description = self.driver.find_element_by_xpath(LocationPageLocators.store_address).text
        location_select.click()
        my_store = self.driver.find_element_by_xpath(LocationPageLocators.store_display).text
        return my_store in store_description
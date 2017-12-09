from locators import SearchPageLocators

class SearchPageElement(self):
    list_of_prices = []
    item_prices = self.driver.find_element_by_xpath(SearchPageLocators.all_prices)
    for price in item_prices:
        list_of_prices.append(float(span.text.replace("$", "")))

    balance = self.driver.find_elements_by_xpath(SearchPageLocators.order_total)
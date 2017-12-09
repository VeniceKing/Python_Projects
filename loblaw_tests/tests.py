import selenium.webdriver as webdriver
import unittest
import page

class WebSiteCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')       
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.loblaws.ca/search/1512686396308/page/~item/apples/~selected/true/~sort/price-desc")
        
    def tearDown(self):
        self.driver.quit()

    def test_can_search(self):
        self.driver.get('https://www.loblaws.ca')
        home_page = page.HomePage(self.driver)
        home_page = page.HomePage(self.driver)
        assert home_page.can_search_for_item()

    def test_can_change_language(self):
        self.driver.get('https://www.loblaws.ca')
        home_page = page.HomePage(self.driver)
        assert home_page.is_language_french()

    def test_shopping_cart_starts_empty(self):
        search_page = page.SearchPage(self.driver)
        assert search_page.is_balance_zero()		

    def test_can_add_item_to_cart(self):
        search_page = page.SearchPage(self.driver)
        assert search_page.is_item_in_cart()

    def test_can_display_correct_store(self):
        self.driver.get('https://www.loblaws.ca/store-locator')
        location_page = page.LocationPage(self.driver)
        assert location_page.is_location_correct()

    def test_can_sort_items_by_price(self):
        search_page = page.SearchPage(self.driver)
        assert search_page.is_item_list_sorted()

if __name__ == "__main__":
    unittest.main()
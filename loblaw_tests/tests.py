import selenium.webdriver as webdriver
import unittest
import page

class WebSiteCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')       
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.loblaws.ca')

    def tearDown(self):
        self.driver.quit()

    def test_checkout_has_threshold(self):
        search_page = page.SearchPage(self.driver)
        assert search_page.is_checkout_working()
        
    def test_can_redirect_to_homepage(self):
        search_page = page.SearchPage(self.driver)
        assert search_page.is_home_page()
    
    def test_can_sort_items_by_price(self):
        search_page = page.SearchPage(self.driver)
        assert search_page.is_item_list_sorted()

    def test_can_search(self):
        home_page = page.HomePage(self.driver)
        assert home_page.can_search_for_item()

    def test_can_change_language(self):
        home_page = page.HomePage(self.driver)
        assert home_page.is_language_french()

    def test_shopping_cart_starts_empty(self):
        home_page = page.HomePage(self.driver)
        assert home_page.is_balance_zero()		

    def test_can_add_item_to_cart(self):
        search_page = page.SearchPage(self.driver)
        assert search_page.is_item_in_cart()

    def test_can_display_correct_store(self):
        location_page = page.LocationPage(self.driver)
        assert location_page.is_location_correct()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
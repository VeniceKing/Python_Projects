import selenium.webdriver as webdriver
import unittest
import page
from locators import URLS

class WebSiteCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')       
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def home_page_url(self):
        self.driver.get(URLS.home_page_url)

    def search_page_url(self):
        self.driver.get(URLS.search_page_url)

    def location_page_url(self):
        self.driver.get(URLS.location_page_url)

#HomePageTests
    def test_shopping_cart_starts_empty(self):
        WebSiteCase.home_page_url(self)
        home_page = page.HomePage(self.driver)
        assert home_page.is_balance_zero()	

    def test_can_search(self):
        WebSiteCase.home_page_url(self)
        home_page = page.HomePage(self.driver)
        assert home_page.can_search_for_item()

    def test_can_change_language(self):
        WebSiteCase.home_page_url(self)
        home_page = page.HomePage(self.driver)
        assert home_page.is_language_french()

#SearchPageTests
    def test_can_redirect_to_homepage(self):
        WebSiteCase.search_page_url(self)
        search_page = page.SearchPage(self.driver)
        assert search_page.is_home_page()
    
    def test_can_sort_items_by_price(self):
        WebSiteCase.search_page_url(self)
        search_page = page.SearchPage(self.driver)
        assert search_page.is_item_list_sorted()

    def test_can_add_item_to_cart(self):
        WebSiteCase.search_page_url(self)
        search_page = page.SearchPage(self.driver)
        assert search_page.is_item_in_cart()

    def test_checkout_has_threshold(self):
        WebSiteCase.location_page_url(self)
        search_page = page.SearchPage(self.driver)
        assert search_page.is_checkout_working()

#LocationPageTests
    def test_can_display_correct_store(self):
        WebSiteCase.location_page_url(self)
        location_page = page.LocationPage(self.driver)
        assert location_page.is_location_correct()

    def test_can_search_for_stores(self):
        WebSiteCase.location_page_url(self)
        location_page = page.LocationPage(self.driver)
        assert location_page.can_search_for_store()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
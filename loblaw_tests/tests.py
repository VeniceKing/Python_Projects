import selenium.webdriver as webdriver
import unittest

class WebSiteCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_can_add_item_to_cart(self):
        self.driver.get("https://www.loblaws.ca/search/1512686396308/page/~item/apples/~selected/true/~sort/price-desc")
        item_select = self.driver.find_element_by_xpath('//span[@class="add-to-cart-text"][1]')
        item_select.click()
        check_map = self.driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/button')
        check_map.click()
        store_select = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[3]/a/span[1]')
        store_description = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[2]/div/h4').text
        store_select.click()
        item_select = self.driver.find_element_by_xpath('//span[@class="add-to-cart-text"][1]')
        item_select.click()
        item_price = self.driver.find_element_by_xpath('//span[@class="reg-price-text"][1]').text
        order_total = self.driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/span[2]/span').text
        self.assertEqual(item_price, order_total)

    def test_can_sort_items_by_price(self):
        all_prices = []
        self.driver.get("https://www.loblaws.ca/search/1512686396308/page/~item/apples/~selected/true/~sort/price-desc")
        all_spans = self.driver.find_elements_by_xpath('//span[@class="reg-price-text"]')
        for span in all_spans:
            all_prices.append(float(span.text.replace("$", "")))
        self.assertEqual(sorted(all_prices, reverse=True), all_prices)

    def test_can_display_correct_store(self):
        self.driver.get('https://www.loblaws.ca/store-locator')
        store_select = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[3]/a/span[1]')
        store_description = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[2]/div/h4').text
        store_select.click()
        web_location = self.driver.find_element_by_xpath('//*[@id="siteheader"]/div[1]/div[5]/button[1]/span[2]').text
        self.assertIn(web_location, store_description, "The correct location is NOT being displayed")

if __name__ == "__main__":
    unittest.main()

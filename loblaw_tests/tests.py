import selenium.webdriver as webdriver
from time import sleep
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.implicitly_wait(5)

def test_can_display_correct_store():
	driver.get('https://www.loblaws.ca/store-locator')
	store_select = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[3]/a/span[1]')
	store_description = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[2]/div/h4').text
	store_select.click()
	web_location = driver.find_element_by_xpath('//*[@id="siteheader"]/div[1]/div[5]/button[1]/span[2]').text
	if web_location in store_description:
		print("The correct location is being displayed")
	else:
		print("The correct location is NOT being displayed")

def test_can_add_item_to_cart():
    driver.get("https://www.loblaws.ca/search/1512686396308/page/~item/apples/~selected/true/~sort/price-desc")
    item_select = driver.find_element_by_xpath('//span[@class="add-to-cart-text"][1]')
    item_select.click()
    item_price = driver.find_element_by_xpath('//span[@class="reg-price-text"][1]').text
    order_total = driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/span[2]/span').text
    if item_price == order_total:
        print("The item was succesfully added to shopping cart")
    else:
        print("The item was NOT succesfully added to shopping cart")
    
def test_can_sort_items_by_price():
	all_prices = []
	driver.get("https://www.loblaws.ca/search/1512686396308/page/~item/apples/~selected/true/~sort/price-desc")
	all_spans = driver.find_elements_by_xpath('//span[@class="reg-price-text"]')
	for span in all_spans:
		all_prices.append(float(span.text.replace("$", "")))
	if sorted(all_prices, reverse=True) == all_prices:
		print("The items are sorted from highest to lowest")
	else:
		print("The items are NOT sorted from highest to lowest")

test_can_display_correct_store()
test_can_sort_items_by_price()
test_can_add_item_to_cart()
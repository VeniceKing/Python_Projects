class SearchPageLocators(object):
	order_total = '//*[@id="navigation"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/span[2]/span'
	all_prices = '//span[@class="reg-price-text"]'
	add_to_cart = '//span[@class="add-to-cart-text"][1]'
	my_item = '//span[@class="reg-price-text"][1]'
	pick_store = '//*[@id="navigation"]/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/button'

class LocationPageLocators(object):
	location_button = '//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[3]/a/span[1]'
	store_address = '//*[@id="content"]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/div/div/div[2]/div/h4'
	store_display = '//*[@id="siteheader"]/div[1]/div[5]/button[1]/span[2]'
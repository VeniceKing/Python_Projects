from selenium.webdriver.common.by import By

class URLS(object):
    home_page_url = 'https://www.loblaws.ca'
    location_page_url = 'https://www.loblaws.ca/store-locator'
    search_page_url = 'https://www.loblaws.ca/search/1512686396308/page/~item/apples/~selected/true/~sort/price-desc'
    cart_review_url = 'https://www.loblaws.ca/quickshop'

class SearchPageLocators(object):
    all_prices = (By.CSS_SELECTOR, 'div.page-search-results.container > span.reg-price-text')
    add_to_cart = (By.CSS_SELECTOR, '.add-to-cart-text')
    my_item = (By.CSS_SELECTOR, '.reg-price-text')
    pick_store = (By.CSS_SELECTOR, '.select-button-container > div > button')
    location_button = (By.CSS_SELECTOR, 'li.row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > a:nth-child(1)')
    sort_prices_desc = (By.CSS_SELECTOR, 'li:nth-child(4) > button')
    order_total = (By.CSS_SELECTOR, '.cart-total-text > span')
    home_button = (By.CSS_SELECTOR, '#siteheader > div.row.top-bar > div.wrapper-logo > a')
    checkout_button = (By.CSS_SELECTOR, '.component-wrapper > button')

class LocationPageLocators(object):
    location_button = (By.CSS_SELECTOR, '.wrapper-button.pull-left > a > span:nth-child(1)')
    store_address = (By.CSS_SELECTOR, '.wrapper-content > div > h4')
    my_store = (By.CSS_SELECTOR, '.store-name-text.visible-lg.visible-inline-block')
    store_search_bar = (By.CSS_SELECTOR, '#enter-new-search-term')

class HomePageLocators(object):
    store_locator_button = (By.CSS_SELECTOR, '#siteheader > div.row.top-bar > div.left-header-links > div.wrapper-our-stores.hidden-sm-inline-block.hidden-sm > a > span')    
    order_total = (By.CSS_SELECTOR, ".cart-total-text > span")
    french_button = (By.CSS_SELECTOR, '.btn.btn-inline-link.language-link')
    change_language_button = (By.CSS_SELECTOR, 'body > div.header-bar > ul > li:nth-child(3) > a')
    search_bar = (By.CSS_SELECTOR, '#search-bar')
    search_results = (By.CSS_SELECTOR, '.term-result-found')
    shopping_cart_status = (By.CSS_SELECTOR, '#content > div > div.wrapper-empty-cart > h1')
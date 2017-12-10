from selenium.webdriver.common.by import By

class URLS(object):
    home_page_url = 'https://www.loblaws.ca'
    location_page_url = 'https://www.loblaws.ca/store-locator'
    search_page_url = 'https://www.loblaws.ca/search/1512686396308/page/~item/apples/~selected/true/~sort/price-desc'

class SearchPageLocators(object):
    all_prices = (By.CSS_SELECTOR, '#content > div.page-search-results.container > div:nth-child(2) > div > div > div.wrapper-module-result.multiple > div > div.row.result-products > div.module-product-group.product-group-type-false > div > div.row.row-content.row-products.first-row-products.content-tile-container.has-content-tile-animation.loaded > div > div:nth-child(1) > div > div > div.product-info > div.price > div > span.reg-price > span.reg-price-text')
    add_to_cart = (By.CSS_SELECTOR, '#content > div.page-search-results.container > div:nth-child(2) > div > div > div.wrapper-module-result.multiple > div > div.row.result-products > div.module-product-group.product-group-type-false > div > div.row.row-content.row-products.first-row-products.content-tile-container.has-content-tile-animation.loaded > div > div:nth-child(1) > div > form > div.module-add-to-cart > div > div > button.btn.btn-secondary.btn-add-to-cart > span.add-to-cart-text')
    my_item = (By.CSS_SELECTOR, '#content > div.page-search-results.container > div:nth-child(2) > div > div > div.wrapper-module-result.multiple > div > div.row.result-products > div.module-product-group.product-group-type-false > div > div.row.row-content.row-products.first-row-products.content-tile-container.has-content-tile-animation.loaded > div > div:nth-child(1) > div > div > div.product-info > div.price > div > span.reg-price > span.reg-price-text')
    pick_store = (By.CSS_SELECTOR, '#navigation > div.module-primary-navigation.container > div.temp-notification-alert-container > div.module-flyout-pick-a-store > div.message-and-button.col-sm-12.col-md-12.col-lg-6.col-xl-6 > div > div.button-container.col-md-12.col-sm-12.col-lg-12 > div.select-button-container > div > button')
    location_button = (By.CSS_SELECTOR, 'li.row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > a:nth-child(1)')
    sort_prices_desc = (By.CSS_SELECTOR, '#content > div.page-search-results.container > div:nth-child(2) > div > div > div.wrapper-module-result.multiple > div > div.row.result-header.primary-result-header > div.wrapper-sort-results > div > ul > li:nth-child(4) > button')
    order_total = (By.CSS_SELECTOR, '#navigation > div.module-primary-navigation.container > div.navbar.navbar-default.primary-navbar-wrap > div.module-mini-cart.abtest-25057-hide > div.module-cart-container.wrapper-cart-shortcut > div > div.component-wrapper > div > div > span.cart-total-text > span')
    home_button = (By.CSS_SELECTOR, '#siteheader > div.row.top-bar > div.wrapper-logo > a')
    checkout_button = (By.CSS_SELECTOR, '#navigation > div.module-primary-navigation.container > div.navbar.navbar-default.primary-navbar-wrap > div.module-mini-cart.abtest-25057-hide > div.module-cart-container.wrapper-cart-shortcut > div > div.component-wrapper > button')

class LocationPageLocators(object):
    location_button = (By.CSS_SELECTOR, '#content > div.page-store-locator.container > div > div > div.wrapper-search-result.row > div > div:nth-child(3) > div > div.wrapper-list > div > ul > li:nth-child(1) > div > div > div.wrapper-button.pull-left > a > span:nth-child(1)')
    store_address = (By.CSS_SELECTOR, '#content > div.page-store-locator.container > div > div > div.wrapper-search-result.row > div > div:nth-child(3) > div > div.wrapper-list > div > ul > li:nth-child(1) > div > div > div.wrapper-content > div > h4')
    my_store = (By.CSS_SELECTOR, '#siteheader > div.row.top-bar > div.wrapper-order-info.hidden-sm > button.btn-link.button-store-name.shoppable-stores.trigger-store-selector-modal > span.store-name-text.visible-lg.visible-inline-block')
    store_search_bar = (By.CSS_SELECTOR, '#enter-new-search-term')

class HomePageLocators(object):
    store_locator_button = (By.CSS_SELECTOR, '#siteheader > div.row.top-bar > div.left-header-links > div.wrapper-our-stores.hidden-sm-inline-block.hidden-sm > a > span')    
    order_total = (By.CSS_SELECTOR, "#navigation > div.module-primary-navigation.container > div.navbar.navbar-default.primary-navbar-wrap > div.module-mini-cart.abtest-25057-hide > div.module-cart-container.wrapper-cart-shortcut > div > div.component-wrapper > div > div > span.cart-total-text > span")
    french_button = (By.CSS_SELECTOR, '#page > div:nth-child(3) > div > div:nth-child(2) > div > div.footer-terms > a.btn.btn-inline-link.language-link')
    change_language_button = (By.CSS_SELECTOR, 'body > div.header-bar > ul > li:nth-child(3) > a')
    search_bar = (By.CSS_SELECTOR, '#search-bar')
    search_results = (By.CSS_SELECTOR, '#content > div.page-search-results.container > div:nth-child(2) > div > div > div.wrapper-module-result.multiple > div > div.row.result-header.primary-result-header > div.result-header-content > h3 > span.term-result-found')
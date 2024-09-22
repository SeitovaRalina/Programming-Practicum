class Market:
    LOGO = "//span[contains(text(),'Products')]"
    NAV_BAR = "//button[@id='react-burger-menu-btn']"
    ADD_TO_CART = "button.btn"

    ITEMS_SORTER = "[data-test ='product-sort-container']"
    ITEM_PRICE = "[data-test = 'inventory-item-price']"
    ITEM_NAME = "[data-test = 'inventory-item-name']"

    CART_BADGE = "[data-test = 'shopping-cart-badge']"
    FOLLOW_TO_CART = "[id='shopping_cart_container']"

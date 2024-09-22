class Market:
    LOGO = "//span[contains(text(),'Products')]"

    ITEMS_SORTER = "[data-test ='product-sort-container']"
    ITEM_PRICE = "[data-test = 'inventory-item-price']"
    ITEM_NAME = "[data-test = 'inventory-item-name']"
    
    ADD_TO_CART_BTN = "//button[@id='add-to-cart-item-name']"
    FOLLOW_TO_CART_BTN = "[id='shopping_cart_container']"

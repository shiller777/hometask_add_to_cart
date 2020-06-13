def test_cart_button_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.implicitly_wait(30)

    browser.get(link)
    
    buttons = browser.find_elements_by_css_selector("button.btn-add-to-basket")

    assert len(buttons) == 1

    
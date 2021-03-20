from selenium import webdriver
import time

def test_basketbtn(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    is_button_present = browser.find_element_by_css_selector("button.btn-add-to-basket")
    time.sleep(10)
    assert None != is_button_present, "Oops. There is no button here."
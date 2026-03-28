from playwright.sync_api import Page, sync_playwright
from Locators.Generic.Login import loginLocators
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    def login_function():
        page.goto("https://tbs-secure1.stsstage.com/")
        page.fill(loginLocators.Object_SitePassword, "spanqatesting")
        page.click(loginLocators.Object_SitePasswordContinue)
        page.fill(loginLocators.Object_Username, "santhosh.s+048@spantechnologyservices.com")
        page.fill(loginLocators.Object_Password, "Test@123")
        Page.click(loginLocators.Object_signin)
        print("Logged in successfully")  
    login_function() 
    browser.close() 

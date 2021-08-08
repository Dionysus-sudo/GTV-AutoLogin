from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pytest
import logging, time

'''
configuring the logger for logging warnings which will be displayed in the html-report
Setting the logger lvl as DEBUG to allow logging all the exceptions/false returns as warnings.

*In order to generate the html-report with logs of Passed cases without logging them as a WARNING or < priority on the test cases,
using print() to update that info and using '-s' with pytest to establish this functionality.


'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


'''
Login class contains methods that executes the following:
    1. Launch the app and checks the login page by checking the login options available.
    2. Find the twitter icon and clicks on the same.
    3. Targets the credential fields, populate the same and Authorize with Twitter.
    4. Login to the next page where twitter account info is asked again.
    5. Checks whether we've reached the home page by targeting the page title icon.
'''

class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login_page_visibility(self):
        try:
            login_page = self.driver.find_element_by_xpath('//android.widget.ImageView[starts-with(@content-desc, "google_login")]')
            if login_page is None:
                return False
        except NoSuchElementException:
            logger.warning('Login Page not found!')
            return False
        print('Success: Login Page found!')
        return True


    def find_twitter_login_option(self):
        try:
            twitter_icon = self.driver.find_element_by_accessibility_id('AuthoriseWithTwitter_593')
            if twitter_icon is None:
                return False
        except NoSuchElementException:
            logger.warning('Twitter icon not found! ') 
            return False  
        print('Success: Twitter icon found!') 
        twitter_icon.click()
        return True


    def authorize_twitter(self, email, password):
        self.email = email
        self.password = password
        try:
            username_or_email_field = self.driver.find_element_by_xpath('//android.widget.EditText[@resource-id="username_or_email"]')
            if username_or_email_field is None:
                logger.warning('Username field not found!')
                return False
            username_or_email_field.send_keys(email)
            print('Success: Username field found! Email entered.')

            password_field = self.driver.find_element_by_xpath('//android.widget.EditText[@resource-id="password"]')
            if password_field is None:
                logger.warning('Password field  not found!')
                return False
            password_field.send_keys(password)
            print('Success: Password field found! Password entered.')

            authorize_twitter = self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="allow"]')
            if authorize_twitter is None:
                logger.warning('Twitter auth failed!')
                return False
            authorize_twitter.click()
            print('Success: Twitter auth deployed!')
        except NoSuchElementException:
            return False
        return True


    def login_with_twitter(self, email, password):
        self.email = email
        self.password = password
        try:
            username_or_email_field = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')
            if username_or_email_field is None:
                return False
            logger.warning('Username field not found!')
            username_or_email_field.send_keys(email)
            print('Success: Username field found! Email entered!')

            password_field = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')
            if password_field is None:
                return False
            logger.warning('Password field not found!')
            password_field.send_keys(password)
            print('Success: Password field found! Password entered.')

            login_button = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.widget.Button')
            if login_button is None:
                logger.warning('Log in button not found!')
                return False
            login_button.click()
            print('Success: Log in button clicked.')

        except NoSuchElementException:
            logger.warning(f'Element not found while running {self.login_with_twitter.__name__}')
            return False
        return True


    def home_page_visibility(self):
        try:
            home_page = self.driver.find_element_by_accessibility_id('Play_Page_Title_503')
            if home_page is None:
                logger.warning('Home page not visible!')
                return False
        except NoSuchElementException:
            return False
        print('Success: Successful Login! Home page visible now')
        return True

    
    def exit(self):
        self.driver.quit()





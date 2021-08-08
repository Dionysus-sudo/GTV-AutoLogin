from gtv_login import Login
from appium import webdriver
import pytest

'''
Configuring the Appium webdriver with desired capabilities for game.tv
Creating the instance of the same and setting implicit wait of 30 seconds to handling the content-loading.
'''

desired_capabilities = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "platformVersion": "11.0",
  "appPackage": "tv.game",
  "app": "D:\\Down-Loads\\game_tv.apk",
  "appActivity": "tv.game.MainActivity",
  'udid': 'emulator-5554'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)
automate = Login(driver)

''''
Initiate test cases with pytest using below command in terminal to genetate html-report:
     pytest tests.py -s --html test_results.html --capture=tee-sys

'''

#Test1
def test_login_screen_visibility():
    assert automate.login_page_visibility() == True

#Test2
def test_twitter_login_presence():
    assert automate.find_twitter_login_option() == True

#Test3
def test_twitter_auth():
    assert automate.authorize_twitter('tes1.auto1@gmail.com', 'game@twitter') == True

#Test3
def test_twitter_login():
    assert automate.login_with_twitter('tes1.auto1@gmail.com', 'game@twitter') == True

def test_home_page_visibility():
    assert automate.home_page_visibility == True

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def one():
    while True:    
        browser = webdriver.Chrome("/Users/jd/Drive J/Python Projects/chromedriver")
        browser.get('https://www.sonyliv.com/live-sport/india-tour-of-england-2022-1700000765/cricket-5th-test-day-4-4-jul-2022-1000177435?watch=true')
        time.sleep(20)
        browser.delete_all_cookies()
        browser.close()

def two():
    browser = webdriver.Chrome("/Users/jd/Drive J/Python Projects/chromedriver")
    browser.get('https://www.sonyliv.com/live-sport/india-tour-of-england-2022-1700000765/cricket-5th-test-day-4-4-jul-2022-1000177435?watch=true')
    actions = ActionChains(browser)
    while True:
        time.sleep(300)
        browser.delete_all_cookies()
        browser.get("chrome://settings/clearBrowserData")
        for i in range(0,7):
            time.sleep(.25)
            actions.send_keys(Keys.TAB)
            actions.perform()
        time.sleep(.5)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(.5)
        browser.get('https://www.sonyliv.com/live-sport/india-tour-of-england-2022-1700000765/cricket-5th-test-day-4-4-jul-2022-1000177435?watch=true')
    

two()
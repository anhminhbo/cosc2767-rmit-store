import sys
import datetime
import rmit_store_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)


# Fixture method - to open web browser
def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(15)

    # Navigating to the RMIT Store Development app website
    driver.get(locators.rmit_store_dev_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.title == 'RMIT Store':
        print(f'We\'re at RMIT Store Development homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "RMIT Store"')
    else:
        print(f'We\'re not at the RMIT Store Development homepage. Check your code!')
        driver.close()
        driver.quit()


# Fixture method - to close web browser
def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

# Check if text Database connection error appear
def checkDatabaseErrorAppear():
    try:
        content = driver.find_element(By.CLASS_NAME, 'error-content')
        if content:
            print(f'Unsuccessfully, Database connection error occurs. Please check your code again DEVs.')
            driver.close()
            driver.quit()
            raise Exception("Database connection error, please check your code again DEVs.")
    except NoSuchElementException:
        print(f'Successfully, Database connection error not occur. Proceed to deploy the website to Production Server at {locators.rmit_store_prod_url}.')
        pass

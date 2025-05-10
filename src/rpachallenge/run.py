from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from bs4 import BeautifulSoup
from requests import get
import time
import os
import pandas as pd

def setup_browser():
    """Initializes the webdriver."""
    service = Service(ChromeDriverManager().install())
    browser_driver = webdriver.Chrome(service=service)
    return browser_driver

def teardown_browser(driver):
    """Closes the current browser session."""
    driver.quit()

def handle_file(name, path):
    """Check if folder and file exist."""
    if not (os.path.exists(path)):
    # create a new directory if not exist already
        os.makedirs(path)
    if os.path.isfile(name):
    # make sure to remove any old versions
        os.remove(name)

# download the file and read the excel file into dataframe
FILE_URL = "https://rpachallenge.com/assets/downloadFiles/challenge.xlsx"
FILE_PATH = os.path.join(os.getcwd(), "test_data")
FILE_NAME = os.path.join(FILE_PATH, "challenge.xlsx")
handle_file(FILE_NAME, FILE_PATH)
file_response = get(FILE_URL, timeout=10)
with open(FILE_NAME, mode="wb") as file:
    file.write(file_response.content)
df = pd.read_excel(FILE_NAME)

# open the page
SITE_URL = "https://www.rpachallenge.com/"
driver = setup_browser()
web_form = driver.get(SITE_URL).content

# loop through excel rows, input info and submit
if driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]"):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]").click()
for row in (df.to_dict(orient="records")):
    print("Handling row:")
    print(row['First Name'], row['Last Name '], row['Company Name'], row['Role in Company'], row['Address'], row['Email'], row['Phone Number'])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']").send_keys(row['First Name'])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']").send_keys(row['Last Name '])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']").send_keys(row['Company Name'])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']").send_keys(row['Role in Company'])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']").send_keys(row['Address'])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']").send_keys(row['Email'])
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']").send_keys(row['Phone Number'])
    #time.sleep(5)
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()
time.sleep(5)

#remove the existing file
handle_file(FILE_NAME, FILE_PATH)

# close the browser
teardown_browser(driver)

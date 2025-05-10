from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from data_handler import handle_file, read_file_to_dataframe
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

SITE_URL = "https://www.rpachallenge.com/"
FILE_URL = "https://rpachallenge.com/assets/downloadFiles/challenge.xlsx"
FILE_PATH = os.path.join(os.getcwd(), "test_data")
FILE_NAME = os.path.join(FILE_PATH, "challenge.xlsx")

def setup_browser():
    """Initializes the webdriver."""
    service = Service(ChromeDriverManager().install())
    browser_driver = webdriver.Chrome(service=service)
    return browser_driver

def teardown_browser(driver):
    """Closes the current browser session."""
    driver.quit()

def fill_the_form(driver, row):
    """Fill the form with row information from excel."""
    fields = {"labelFirstName": row['First Name'], 
              "labelLastName": row['Last Name '], 
              "labelCompanyName": row['Company Name'], 
              "labelRole": row['Role in Company'], 
              "labelAddress": row['Address'], 
              "labelEmail": row['Email'], 
              "labelPhone": row['Phone Number']
              }
    for field, value in fields.items():
        xpath = f"//input[@ng-reflect-name='{field}']"
        driver.find_element(By.XPATH, xpath).send_keys(str(value))
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()

# fetch the input from excel
handle_file(FILE_NAME, FILE_PATH)
df = read_file_to_dataframe(FILE_NAME, FILE_URL)

# open the page
driver = setup_browser()
driver.get(SITE_URL)

# iterate and fill the input form
if driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]"):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]").click()
for row in (df.to_dict(orient="records")):
    logging.info(f"Handling row: {row}")
    fill_the_form(driver, row)

#remove the existing file
handle_file(FILE_NAME, FILE_PATH)

# close the browser
teardown_browser(driver)

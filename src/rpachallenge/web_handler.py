import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_browser():
    """Initializes the webdriver."""
    service = Service(ChromeDriverManager().install())
    browser_driver = webdriver.Chrome(service=service)
    return browser_driver


def teardown_browser(driver):
    """Closes the current browser session."""
    driver.quit()


def start_submit(driver):
    """Finds and clicks Start for beginning the process."""
    try:
        start_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Start')]"
        )
        start_button.click()
    except Exception as e:
        logging.error(f"Unexpected error occurred! Error message: {e}")


def fill_the_form(driver, row):
    """Fill the form with row information from excel."""
    fields = {
        "labelFirstName": row["First Name"],
        "labelLastName": row["Last Name "],
        "labelCompanyName": row["Company Name"],
        "labelRole": row["Role in Company"],
        "labelAddress": row["Address"],
        "labelEmail": row["Email"],
        "labelPhone": row["Phone Number"],
    }
    for field, value in fields.items():
        xpath = f"//input[@ng-reflect-name='{field}']"
        try:
            driver.find_element(By.XPATH, xpath).send_keys(str(value))
        except Exception as e:
            logging.error(
                f"Exception occurred with customer {row['First Name']} {row['Last Name ']}, error message: {e}!"
            )
            continue
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()

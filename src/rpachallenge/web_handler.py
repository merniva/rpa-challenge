import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def setup_browser(headless=False):
    """Initializes the webdriver."""
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    browser_driver = webdriver.Chrome(service=service, options=options)
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
        logging.error("Unexpected error occurred! Error message: %s", e)


def fill_the_form(driver, row):
    """Fill the form with row information from excel."""
    xpath_root = "//input[@ng-reflect-name="
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
        try:
            element = driver.find_element(By.XPATH, f"{xpath_root}'{field}']")
            element.send_keys(str(value))
        except Exception as e:
            logging.error(
                "Exception occurred with customer %s %s, error message: %s!",
                row["First Name"],
                row["Last Name "],
                e,
            )
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()

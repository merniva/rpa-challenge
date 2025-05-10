import logging
import os
import time

from data_handler import initialize_data_folder, read_file_to_dataframe
from web_handler import setup_browser, teardown_browser, fill_the_form, start_submit

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

SITE_URL = "https://www.rpachallenge.com/"
FILE_URL = f"{SITE_URL}/assets/downloadFiles/challenge.xlsx"
FILE_PATH = os.path.join(os.getcwd(), "test_data")
FILE_NAME = os.path.join(FILE_PATH, "challenge.xlsx")


def main():
    """Main function for reading input file and submit information to web form."""
    try:
        # get the info from excel
        initialize_data_folder(FILE_NAME, FILE_PATH)
        df = read_file_to_dataframe(FILE_NAME, FILE_URL)
        # open the page and start processing
        driver = setup_browser()
        driver.get(SITE_URL)
        start_submit(driver)
        # iterate and fill the input form
        for row in df.to_dict(orient="records"):
            logging.info(f"Handling row: {row}")
            try:
                fill_the_form(driver, row)
            except Exception as e:
                logging.error(
                    f"Unexpected error occurred on row: {row}! Error message: {e}"
                )
    except Exception as e:
        logging.error(f"Critical error occurred! Error message: {e}")
    finally:
        # remove the existing file
        initialize_data_folder(FILE_NAME, FILE_PATH)
        teardown_browser(driver)

if __name__ == "__main__":
    main()

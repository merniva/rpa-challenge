import logging
import os
import time
import argparse

from data_handler import initialize_data_folder, read_file_to_dataframe
from web_handler import setup_browser, teardown_browser, fill_the_form, start_submit

logging.basicConfig(level=logging.INFO)

SITE_URL = "https://www.rpachallenge.com/"
FILE_URL = f"{SITE_URL}/assets/downloadFiles/challenge.xlsx"
FILE_PATH = os.path.join(os.getcwd(), "input_data")
FILE_NAME = os.path.join(FILE_PATH, "challenge.xlsx")


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the RPAChallenge script.")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run the browser in headless mode, default is False.",
    )
    return parser.parse_args()


def main():
    """Main function for reading input file and submit information to web form."""
    args = parse_arguments()
    try:
        # get the info from excel
        initialize_data_folder(FILE_NAME, FILE_PATH)
        df = read_file_to_dataframe(FILE_NAME, FILE_URL)
        # open the page and start processing
        driver = setup_browser(headless=args.headless)
        driver.get(SITE_URL)
        start_submit(driver)
        # iterate and fill the input form
        success_count = 0
        for row in df.to_dict(orient="records"):
            start_time = time.time()
            logging.info("Handling row: %s", row)
            try:
                fill_the_form(driver, row)
                success_count += 1
            except Exception as e:
                logging.error(
                    "Unexpected error occurred on row: %s! Error message: %s", row, e
                )
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        logging.info(
            "%d/%d rows successfully executed and forms filled in %.2f ms.",
            success_count, len(df), execution_time
        )
    except Exception as e:
        logging.error("Critical error occurred! Error message: %s", e)
    finally:
        # remove the existing file
        initialize_data_folder(FILE_NAME, FILE_PATH)
        teardown_browser(driver)


if __name__ == "__main__":
    main()

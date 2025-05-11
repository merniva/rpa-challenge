import logging
import os
import time
import argparse

from data_handler import initialize_data_folder, read_file_to_dataframe
from web_handler import setup_browser, teardown_browser, fill_the_form, start_submit

SITE_URL = "https://www.rpachallenge.com/"
FILE_URL = f"{SITE_URL}/assets/downloadFiles/challenge.xlsx"
FILE_PATH = os.path.join(os.getcwd(), "input_data")
FILE_NAME = os.path.join(FILE_PATH, "challenge.xlsx")

def limit_iterations(value):
    """A helper function for checking that iteration amount is between 1 and 10."""
    iteration_value = int(value)
    if iteration_value <= 0:
        raise argparse.ArgumentTypeError(f"Invalid value: {value}. Value must be a positive integer!")
    if iteration_value > 10:
        raise argparse.ArgumentTypeError(f"Invalid value: {value}. Maximum allowed iterations is 10!")
    return iteration_value

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the RPAChallenge script.")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run the browser in headless mode, default is False.",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set the logging level to INFO, WARNING or ERROR, default is INFO.",
    )
    parser.add_argument(
        "--iterations",
        type=limit_iterations,
        default=None,
        help="Give optional amount of iterations, default is 1.",
    )
    return parser.parse_args()


def main():
    """Main function for reading input file and submit information to web form."""
    args = parse_arguments()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))
    try:
        for iteration in range(args.iterations or 1):
            logging.info("Starting iteration %d", iteration + 1)
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
            # remove the existing file
            initialize_data_folder(FILE_NAME, FILE_PATH)
            teardown_browser(driver)
    except Exception as e:
            logging.error("Critical error occurred! Error message: %s", e)
    finally:
        logging.info("All iterations completed!")
            


if __name__ == "__main__":
    main()

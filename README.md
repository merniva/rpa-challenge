# rpachallenge

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [Project Structure](#project_structure)
- [License](#license)

## Features

This project automatically downloads the Excel file from the RPAChallenge website. It reads and processes the Excel data using Pandas, and fills out the web form dynamically using Selenium.

## Installation

1. Clone the repository using
   git clone https://github.com/merniva/rpachallenge.git

2. Create a virtual environment using Python 3.10 or higher:
    `py -3.10 -m venv .venv`
    Activate on Windows with 
    `.venv\Scripts\activate`

3. Install the required dependencies using
    `python -m pip install -r requirements.txt`

4. Install the project in editable mode for your usage with
    `python -m pip install -e .`

## Usage

- Run the main script from run.py:
    `python src/rpachallenge/run.py`
- To run in headless mode:
    `python src/rpachallenge/run.py --headless`

Use `--headless` option for faster execution and running the script where a graphical interface is not available.

## Acknowledgements

- [Selenium](https://www.selenium.dev/) for browser automation.
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) for automatically managing browser drivers.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [RPAChallenge](https://www.rpachallenge.com/) for providing the challenge.

## Project Structure

rpachallenge/
├── src/
│   ├── rpachallenge/
│   │   ├── __about__.py
│   │   ├── __init__.py
│   │   ├── run.py
│   │   ├── data_handler.py
│   │   ├── web_handler.py
├── tests
│   ├── __init.py__
│   ├── test_web_handler.py
├── README.md
├── requirements.txt
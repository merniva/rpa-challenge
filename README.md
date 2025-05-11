# rpachallenge

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [Project Structure](#project_structure)
- [License](#license)

## Features

This project automatically downloads the Excel file from the RPAChallenge website. It reads and processes the Excel data using Pandas, and fills out the web form dynamically using Selenium.

## Requirements

- Python 3.10 or higher
- Chrome browser

## Installation

1. Clone the repository using
   git clone https://github.com/merniva/rpa-challenge.git

2. Create a virtual environment using Python 3.10 or higher (adjust the command to your preferred Python version):
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
- To adjust the logging level, set --log-level parameter as INFO, WARNING or ERROR (default being INFO):
    `python src/rpachallenge/run.py --log-level ERROR` 
- To adjust the amount of iterations, set --iterations parameter from 1 to 10 (default being 1):
    `python src/rpachallenge/run.py --iterations 4`

You can also give multiple parameters, for example:
    `python src/rpachallenge/run.py --headless --log-level ERROR --iterations 3`.

Use `--headless` option for running the script where a graphical interface is not available.
To see all available options, run:
    `python src/rpachallenge/run.py --help`

## Acknowledgements

- [Selenium](https://www.selenium.dev/) for browser automation.
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) for automatically managing browser drivers.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [RPAChallenge](https://www.rpachallenge.com/) for providing the challenge.
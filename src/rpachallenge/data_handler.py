import os
import pandas as pd
from requests import get


def initialize_data_folder(name, path):
    """Check if folder and file exist."""
    if not os.path.exists(path):
        # create a new directory if not exist already
        os.makedirs(path)
    if os.path.isfile(name):
        # make sure to remove any old file versions
        os.remove(name)


def read_file_to_dataframe(name, url):
    """Get excel and read it as dataframe."""
    file_response = get(url, timeout=10)
    with open(name, mode="wb") as file:
        file.write(file_response.content)
    dataframe = pd.read_excel(name)
    return dataframe

import sys

import pandas
import numpy


def load_data(file_path):
    try:
        data = pandas.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while loading the data: {e!s}")
        sys.exit(1)

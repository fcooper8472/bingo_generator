from pathlib import Path


def get_data_dir():
    # Get the directory of the current script file
    current_dir = Path(__file__).resolve().parent

    # Construct a path to the data directory
    data_dir = current_dir / 'data'

    return data_dir

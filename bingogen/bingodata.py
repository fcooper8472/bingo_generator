import pathlib
import random
import warnings

from typing import List


class BingoData:

    def __init__(self, file_path: str):

        # Instance variables:
        self._file_path = pathlib.Path(file_path)
        self._data = []

        self._check_file()
        self._read_file()
        self._check_data()

    def _check_file(self):
        if not self._file_path.exists():
            raise FileNotFoundError(f'file {self._file_path} does not exist')

    def _read_file(self):
        with open(self._file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    self._data.append(stripped_line)

    def _check_data(self):
        if not self._data:
            raise ValueError(f'no data found in {self._file_path}')

        for line in self._data:
            if len(line) > 50:
                warnings.warn(f'text "{line}" is longer than 50 characters and might not format nicely')

    @property
    def data(self) -> List[str]:
        return self._data

    @property
    def num_data_items(self) -> int:
        return len(self._data)

    def get_random_n(self, n: int) -> List[str]:
        if n > self.num_data_items:
            raise ValueError(f'requested a sample of size {n}, but there are only {self.num_data_items} entries')
        return random.sample(self._data, n)

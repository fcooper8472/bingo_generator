import pathlib


class BingoData:

    def __init__(self, file_path: str):

        # Instance variables:
        self._file_path = pathlib.Path(file_path)
        self._data = []

        self._check_file()
        self._read_file()

    def _check_file(self):
        if not self._file_path.exists():
            raise FileNotFoundError(f'file {self._file_path} does not exist')

    def _read_file(self):
        with open(self._file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    self._data.append(stripped_line)

    @property
    def data(self):
        return self._data

    @property
    def num_data_items(self):
        return len(self._data)

import pathlib


class BingoData:
    def __init__(self, file_path: str):

        self.file_path = pathlib.Path(file_path)

        assert self.file_path.is_file(), f'file {file_path} does not exist'

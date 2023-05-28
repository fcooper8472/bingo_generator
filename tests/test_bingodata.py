import pathlib
import tempfile

from bingogen.bingodata import BingoData


def test_bingo_data_init():
    with tempfile.NamedTemporaryFile() as temp:
        bd = BingoData(temp.name)
        assert bd.file_path == pathlib.Path(temp.name)


def test_bingo_data_init_invalid_path():
    # This path should not exist
    invalid_file_path = '/path/to/invalid/file'
    try:
        BingoData(invalid_file_path)
    except AssertionError:
        assert True
    else:
        assert False

import pathlib
import pytest
import tempfile

from bingogen.bingodata import BingoData


def test_bingo_data_init():
    with tempfile.NamedTemporaryFile() as temp:
        bd = BingoData(temp.name)
        assert bd.file_path == pathlib.Path(temp.name)


def test_bingo_data_init_invalid_path():
    # This path should not exist
    invalid_file_path = '/path/to/invalid/file'

    with pytest.raises(AssertionError) as assertion_error:
        BingoData(invalid_file_path)

    assert str(assertion_error.value) == 'file /path/to/invalid/file does not exist'
